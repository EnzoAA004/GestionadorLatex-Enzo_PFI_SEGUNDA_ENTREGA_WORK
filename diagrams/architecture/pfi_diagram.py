"""Primitivas SVG para las figuras de arquitectura del Capitulo 10 (PFI).

Genera SVG deterministas con posiciones explicitas y los rasteriza a PNG.
Incluye check_layout(), que verifica solapamiento de cajas, desborde de texto
dentro de las cajas y salidas del lienzo antes de escribir el archivo.

Uso:  python3 fig_10_0X_*.py   (cada figura importa este modulo)

Dependencias: cairosvg, pillow (solo para medir texto).
"""

from __future__ import annotations

import html
import os
import subprocess
import sys
from dataclasses import dataclass, field

from PIL import ImageFont

FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_ITALIC = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"
FONT_FAMILY = "DejaVu Sans, Helvetica, Arial, sans-serif"

# Paleta sobria alineada con las Figuras 10.1/10.2/10.3/10.7 del capitulo.
INK = "#1f2937"          # texto principal
INK_SOFT = "#4b5563"     # texto secundario
LINE = "#94a3b8"         # lineas auxiliares
CANVAS = "#ffffff"

BLUE = "#1f4e9c"
GREEN = "#2f7d5f"
PURPLE = "#5b3f8f"
ORANGE = "#b07316"
TEAL = "#1f7a7a"
RED = "#9b2c2c"
GREY = "#5a6472"

FILL = {
    BLUE: "#eef3fb",
    GREEN: "#eaf4ef",
    PURPLE: "#f2eefa",
    ORANGE: "#fdf3e3",
    TEAL: "#e8f5f5",
    RED: "#fbeeee",
    GREY: "#f1f3f6",
}

_font_cache: dict[tuple[str, int], ImageFont.FreeTypeFont] = {}


def _font(path: str, size: int) -> ImageFont.FreeTypeFont:
    key = (path, size)
    if key not in _font_cache:
        _font_cache[key] = ImageFont.truetype(path, size)
    return _font_cache[key]


def text_width(text: str, size: float, weight: str = "normal") -> float:
    """Ancho aproximado del texto en unidades de usuario del SVG."""
    path = FONT_BOLD if weight == "bold" else (
        FONT_ITALIC if weight == "italic" else FONT_REGULAR)
    ref = 100
    f = _font(path, ref)
    return f.getlength(text) * size / ref


def esc(text: str) -> str:
    return html.escape(text, quote=True)


# --------------------------------------------------------------------------
# Modelo de la escena
# --------------------------------------------------------------------------

@dataclass
class Box:
    """Caja rectangular con contenido tabular opcional."""

    key: str
    x: float
    y: float
    w: float
    h: float
    color: str = BLUE
    fill: str | None = None
    solid_header: bool = False

    def __post_init__(self) -> None:
        if self.fill is None:
            self.fill = FILL.get(self.color, "#f5f7fa")

    @property
    def cx(self) -> float:
        return self.x + self.w / 2

    @property
    def cy(self) -> float:
        return self.y + self.h / 2

    @property
    def right(self) -> float:
        return self.x + self.w

    @property
    def bottom(self) -> float:
        return self.y + self.h

    def port(self, side: str, t: float = 0.5) -> tuple[float, float]:
        if side == "l":
            return (self.x, self.y + self.h * t)
        if side == "r":
            return (self.right, self.y + self.h * t)
        if side == "t":
            return (self.x + self.w * t, self.y)
        if side == "b":
            return (self.x + self.w * t, self.bottom)
        raise ValueError(side)


@dataclass
class Scene:
    width: float
    height: float
    margin: float = 12.0
    elements: list[str] = field(default_factory=list)
    boxes: list[Box] = field(default_factory=list)
    _issues: list[str] = field(default_factory=list)
    # (x, y, w, h, texto) de cada bloque de texto, para verificar desbordes
    _texts: list[tuple[float, float, float, str]] = field(default_factory=list)

    # ---------------- primitivas basicas ----------------

    def raw(self, markup: str) -> None:
        self.elements.append(markup)

    def text(
        self,
        x: float,
        y: float,
        content: str,
        size: float = 15,
        weight: str = "normal",
        color: str = INK,
        anchor: str = "start",
        letter_spacing: float | None = None,
        check: bool = True,
    ) -> float:
        w = text_width(content, size, weight)
        style = "italic" if weight == "italic" else "normal"
        fw = "bold" if weight == "bold" else "normal"
        extra = f' letter-spacing="{letter_spacing}"' if letter_spacing else ""
        if letter_spacing:
            w += letter_spacing * max(len(content) - 1, 0)
        self.elements.append(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT_FAMILY}" '
            f'font-size="{size}" font-weight="{fw}" font-style="{style}" '
            f'fill="{color}" text-anchor="{anchor}"{extra}>{esc(content)}</text>'
        )
        if check:
            x0 = x if anchor == "start" else (x - w / 2 if anchor == "middle" else x - w)
            self._texts.append((x0, y, w, content))
        return w

    def line(self, x1, y1, x2, y2, color=LINE, width=1.0, dash: str | None = None) -> None:
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.elements.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{color}" stroke-width="{width}"{d} />'
        )

    def path(self, d: str, color=GREY, width=1.4, dash=None, marker="arrow", fill="none") -> None:
        dd = f' stroke-dasharray="{dash}"' if dash else ""
        mk = f' marker-end="url(#{marker})"' if marker else ""
        self.elements.append(
            f'<path d="{d}" fill="{fill}" stroke="{color}" stroke-width="{width}"'
            f' stroke-linejoin="round" stroke-linecap="round"{dd}{mk} />'
        )

    def rect(self, x, y, w, h, fill="#ffffff", stroke=None, width=1.0, rx=3.0, dash=None) -> None:
        s = f' stroke="{stroke}" stroke-width="{width}"' if stroke else ""
        dd = f' stroke-dasharray="{dash}"' if dash else ""
        self.elements.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" '
            f'rx="{rx}" fill="{fill}"{s}{dd} />'
        )

    # ---------------- componentes de alto nivel ----------------

    def title(self, text: str, subtitle: str | None = None, size: float = 21) -> None:
        self.text(self.width / 2, 34, text, size=size, weight="bold",
                  color="#16305c", anchor="middle")
        if subtitle:
            self.text(self.width / 2, 56, subtitle, size=size * 0.62,
                      color=INK_SOFT, anchor="middle")

    def entity(
        self,
        key: str,
        x: float,
        y: float,
        w: float,
        title: str,
        rows: list[tuple[str, str]],
        color: str = BLUE,
        row_h: float = 24.0,
        head_h: float = 27.0,
        font: float = 15.0,
        pad: float = 7.0,
        note: str | None = None,
    ) -> Box:
        """Caja tipo tabla: encabezado solido + filas (marcador, texto)."""
        h = head_h + row_h * len(rows)
        box = Box(key, x, y, w, h, color=color)
        self.boxes.append(box)

        self.rect(x, y, w, h, fill="#ffffff", stroke=color, width=1.2, rx=2.5)
        self.rect(x, y, w, head_h, fill=color, stroke=None, rx=2.5)
        self.rect(x, y + head_h - 4, w, 4, fill=color, rx=0)
        tf = font + 0.5
        while tf > 9 and text_width(title, tf, "bold") > w - 12:
            tf -= 0.5
        self.text(x + w / 2, y + head_h - 7.5, title, size=tf,
                  weight="bold", color="#ffffff", anchor="middle")
        if text_width(title, tf, "bold") > w - 10:
            self._issues.append(f"[{key}] el titulo '{title}' excede el encabezado")

        cy = y + head_h
        for i, (marker, label) in enumerate(rows):
            if i:
                self.line(x, cy, x + w, cy, color="#d6dce6", width=0.8)
            fill_row = FILL.get(color, "#f5f7fa") if marker in ("PK", "UQ") else None
            if fill_row:
                self.rect(x + 0.6, cy + 0.6, w - 1.2, row_h - 1.2, fill=fill_row, rx=0)
            tx = x + pad
            if marker:
                mw = self.text(tx, cy + row_h - 6.5, marker, size=font,
                               weight="bold", color=INK)
                tx += mw + 5
            self.text(tx, cy + row_h - 6.5, label, size=font, color=INK)
            used = (text_width(marker, font, "bold") + 5 if marker else 0) + \
                text_width(label, font)
            if used > w - 2 * pad:
                self._issues.append(
                    f"[{key}] fila '{marker} {label}' excede el ancho de la caja "
                    f"({used:.0f} > {w - 2 * pad:.0f})")
            cy += row_h

        if note:
            self.text(x, y - 6, note, size=font - 1.5, weight="italic", color=INK_SOFT)
        return box

    def uml(
        self,
        key: str,
        x: float,
        y: float,
        w: float,
        title: str,
        attrs: list[str],
        ops: list[str] | None = None,
        color: str = BLUE,
        stereotype: str | None = None,
        font: float = 14.5,
        row_h: float = 21.0,
        head_h: float = 27.0,
        pad: float = 7.0,
    ) -> Box:
        ops = ops or []
        head = head_h + (13 if stereotype else 0)
        h = head + row_h * len(attrs) + (6 if ops else 0) + row_h * len(ops) + 6
        box = Box(key, x, y, w, h, color=color)
        self.boxes.append(box)

        self.rect(x, y, w, h, fill="#ffffff", stroke=color, width=1.2, rx=2.5)
        self.rect(x, y, w, head, fill=color, rx=2.5)
        self.rect(x, y + head - 4, w, 4, fill=color, rx=0)
        ty = y + head - 8
        if stereotype:
            self.text(x + w / 2, y + 14, stereotype, size=font - 1.5,
                      color="#ffffff", anchor="middle")
            ty = y + head - 7
        self.text(x + w / 2, ty, title, size=font + 1, weight="bold",
                  color="#ffffff", anchor="middle")
        if text_width(title, font + 1, "bold") > w - 10:
            self._issues.append(f"[{key}] el titulo '{title}' excede el encabezado")
        if stereotype and text_width(stereotype, font - 1.5) > w - 8:
            self._issues.append(f"[{key}] el estereotipo '{stereotype}' excede el encabezado")

        cy = y + head + 4
        for a in attrs:
            self.text(x + pad, cy + row_h - 6, a, size=font, color=INK)
            if text_width(a, font) > w - 2 * pad:
                self._issues.append(f"[{key}] atributo '{a}' excede el ancho")
            cy += row_h
        if ops:
            cy += 3
            self.line(x, cy, x + w, cy, color=color, width=1.0)
            cy += 3
            for o in ops:
                self.text(x + pad, cy + row_h - 6, o, size=font, color=INK)
                if text_width(o, font) > w - 2 * pad:
                    self._issues.append(f"[{key}] operacion '{o}' excede el ancho")
                cy += row_h
        return box

    def node(
        self,
        key: str,
        x: float,
        y: float,
        w: float,
        h: float,
        lines: list[str],
        color: str = BLUE,
        font: float = 13.0,
        bold_first: bool = True,
        pad: float = 6.0,
        dash: str | None = None,
        rx: float = 4.0,
    ) -> Box:
        """Caja simple de flujo con texto centrado."""
        box = Box(key, x, y, w, h, color=color)
        self.boxes.append(box)
        self.rect(x, y, w, h, fill=FILL.get(color, "#f5f7fa"), stroke=color,
                  width=1.2, rx=rx, dash=dash)
        lh = font + 3.5
        total = lh * len(lines)
        cy = y + (h - total) / 2 + font
        for i, ln in enumerate(lines):
            weight = "bold" if (bold_first and i == 0) else "normal"
            col = INK if (bold_first and i == 0) else INK_SOFT
            fs = font if i == 0 else font - 1
            self.text(x + w / 2, cy, ln, size=fs,
                      weight=weight, color=col, anchor="middle")
            if text_width(ln, fs, weight) > w - 2 * pad:
                self._issues.append(f"[{key}] linea '{ln}' excede el ancho de la caja")
            cy += lh
        return box

    def pill(self, x: float, y: float, label: str, font: float = 11.0,
             color: str = INK_SOFT, bg: str = "#ffffff") -> None:
        w = text_width(label, font) + 10
        self.rect(x - w / 2, y - font / 2 - 4, w, font + 8, fill=bg,
                  stroke="#c9d2df", width=0.8, rx=(font + 8) / 2)
        self.text(x, y + font / 2 - 1.5, label, size=font, color=color, anchor="middle")

    def crowfoot(self, x: float, y: float, direction: str = "r", size: float = 9.0,
                 color: str = GREY, width: float = 1.3) -> None:
        """Pata de gallo (lado 'muchos'). direction: hacia donde apunta la caja."""
        s = size
        if direction == "r":   # patas abiertas hacia la derecha
            self.line(x, y, x + s, y - s * 0.62, color, width)
            self.line(x, y, x + s, y + s * 0.62, color, width)
            self.line(x, y, x + s, y, color, width)
        elif direction == "l":
            self.line(x, y, x - s, y - s * 0.62, color, width)
            self.line(x, y, x - s, y + s * 0.62, color, width)
            self.line(x, y, x - s, y, color, width)
        elif direction == "b":
            self.line(x, y, x - s * 0.62, y + s, color, width)
            self.line(x, y, x + s * 0.62, y + s, color, width)
            self.line(x, y, x, y + s, color, width)
        elif direction == "t":
            self.line(x, y, x - s * 0.62, y - s, color, width)
            self.line(x, y, x + s * 0.62, y - s, color, width)
            self.line(x, y, x, y - s, color, width)

    def one_bar(self, x: float, y: float, orient: str = "v", size: float = 9.0,
                color: str = GREY, width: float = 1.3) -> None:
        """Marca '1' de cardinalidad (barra perpendicular)."""
        if orient == "v":
            self.line(x, y - size / 2, x, y + size / 2, color, width)
        else:
            self.line(x - size / 2, y, x + size / 2, y, color, width)

    def legend(self, x: float, y: float, items: list[tuple[str, str]],
               font: float = 11.5, gap: float = 16.0, title: str | None = None) -> None:
        cy = y
        if title:
            self.text(x, cy, title, size=font, weight="bold", color=INK)
            cy += gap
        for color, label in items:
            self.rect(x, cy - font + 2.5, 11, 11, fill=FILL.get(color, "#eee"),
                      stroke=color, width=1.1, rx=2)
            self.text(x + 17, cy, label, size=font, color=INK_SOFT)
            cy += gap

    # ---------------- verificacion ----------------

    def check_layout(self, allow_overlap: set[frozenset[str]] | None = None,
                     tol: float = 0.0) -> list[str]:
        allow_overlap = allow_overlap or set()
        issues = list(self._issues)

        for b in self.boxes:
            if b.x < -tol or b.y < -tol or b.right > self.width + tol or \
                    b.bottom > self.height + tol:
                issues.append(f"[{b.key}] se sale del lienzo "
                              f"({b.x:.0f},{b.y:.0f},{b.right:.0f},{b.bottom:.0f})")

        for i, a in enumerate(self.boxes):
            for b in self.boxes[i + 1:]:
                if frozenset((a.key, b.key)) in allow_overlap:
                    continue
                ox = min(a.right, b.right) - max(a.x, b.x)
                oy = min(a.bottom, b.bottom) - max(a.y, b.y)
                if ox > tol and oy > tol:
                    issues.append(
                        f"solapamiento {a.key} <-> {b.key} ({ox:.0f}x{oy:.0f})")

        for x0, y, w, content in self._texts:
            if x0 < -tol or x0 + w > self.width + tol:
                issues.append(f"texto fuera del lienzo: '{content[:40]}'")
        return issues

    # ---------------- salida ----------------

    def svg(self) -> str:
        defs = (
            '<defs>'
            '<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" '
            'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
            '<path d="M 0 0 L 10 5 L 0 10 z" fill="context-stroke" /></marker>'
            '<marker id="arrowopen" viewBox="0 0 10 10" refX="9" refY="5" '
            'markerWidth="8" markerHeight="8" orient="auto-start-reverse">'
            '<path d="M 0 0 L 10 5 L 0 10" fill="none" stroke="context-stroke" '
            'stroke-width="1.6" /></marker>'
            '<marker id="diamond" viewBox="0 0 12 12" refX="11" refY="6" '
            'markerWidth="9" markerHeight="9" orient="auto-start-reverse">'
            '<path d="M 0 6 L 6 1 L 12 6 L 6 11 z" fill="context-stroke" /></marker>'
            '<marker id="triangle" viewBox="0 0 12 12" refX="11" refY="6" '
            'markerWidth="9" markerHeight="9" orient="auto-start-reverse">'
            '<path d="M 0 0 L 12 6 L 0 12 z" fill="#ffffff" stroke="context-stroke" '
            'stroke-width="1.3" /></marker>'
            '</defs>'
        )
        body = "\n".join(self.elements)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" '
            f'height="{self.height}" viewBox="0 0 {self.width} {self.height}">'
            f'{defs}'
            f'<rect width="{self.width}" height="{self.height}" fill="{CANVAS}" />'
            f'{body}</svg>'
        )

    def render(self, png_path: str, scale: float = 2.4, strict: bool = True,
               allow_overlap: set[frozenset[str]] | None = None) -> None:
        issues = self.check_layout(allow_overlap=allow_overlap)
        if issues:
            print(f"check_layout: {len(issues)} problema(s)", file=sys.stderr)
            for i in issues:
                print("  -", i, file=sys.stderr)
            if strict:
                raise SystemExit("Layout invalido: se aborta el render.")
        else:
            print("check_layout: OK (sin solapamientos ni desbordes)")

        svg_path = os.path.splitext(png_path)[0] + ".svg"
        os.makedirs(os.path.dirname(os.path.abspath(png_path)), exist_ok=True)
        with open(svg_path, "w", encoding="utf-8") as fh:
            fh.write(self.svg())

        import cairosvg  # import diferido: solo necesario al rasterizar
        cairosvg.svg2png(url=svg_path, write_to=png_path,
                         output_width=int(self.width * scale),
                         output_height=int(self.height * scale),
                         background_color="#ffffff")
        size = os.path.getsize(png_path)
        print(f"PNG: {png_path}  {int(self.width * scale)}x{int(self.height * scale)} px "
              f"({size / 1024:.0f} kB)")
        try:  # optimizacion opcional, no es una dependencia dura
            subprocess.run(["optipng", "-quiet", "-o2", png_path], check=False)
        except FileNotFoundError:
            pass
