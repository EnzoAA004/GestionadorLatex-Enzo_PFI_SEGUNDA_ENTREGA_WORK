"""Primitivas de dibujo para las figuras de arquitectura del Capitulo 10.

Genera SVG con posiciones explicitas (sin motor de layout automatico) para que
las figuras conserven la misma retorica visual que las Figuras 10.1, 10.2, 10.3
y 10.7 del capitulo: fondo blanco, tipografia sans-serif, alto contraste, paleta
sobria y relaciones legibles al imprimir en A4.

Reglas de estilo que este modulo impone por construccion:
  - fondo blanco opaco (no se depende de transparencia: los PNG deben poder
    pegarse en Google Docs sin halos);
  - sin gradientes, sin sombras, sin iconos decorativos;
  - ningun titulo de figura ni caption dentro del bitmap (los aporta LaTeX).

Uso: ver fig_10_04_modelo_datos.py, fig_10_05_clases_dominio.py y
fig_10_06_flujo_end_to_end.py. Regeneracion: ./render.sh
"""

from __future__ import annotations

from xml.sax.saxutils import escape

FONT = "Liberation Sans, DejaVu Sans, Arial, Helvetica, sans-serif"

INK = "#1D2530"
MUTED = "#6B7480"
RULE = "#C3CAD3"
PANEL_BG = "#FBFCFD"
PANEL_RULE = "#DDE2E8"

# (acento, relleno claro, borde)
PALETTE = {
    "slate": ("#44546A", "#EDEFF3", "#BFC7D1"),
    "teal": ("#0F5E52", "#E4EFEC", "#9FC3BB"),
    "navy": ("#1F4E79", "#E7EEF6", "#A9C0D8"),
    "purple": ("#4A3A80", "#ECE9F6", "#B4AAD4"),
    "amber": ("#7A5C1E", "#F7F1E4", "#CFC2A4"),
    "crimson": ("#7A3B3B", "#F5EAEA", "#CBB4B4"),
    "grey": ("#5E6A63", "#EFF1F0", "#C2C9C5"),
}

# Ancho medio de glifo por unidad de font-size, medido sobre Liberation Sans.
_AVG = 0.512
_AVG_BOLD = 0.556


def text_width(s: str, size: float, bold: bool = False) -> float:
    return len(s) * size * (_AVG_BOLD if bold else _AVG)


def check_layout(canvas, boxes, pad=6):
    """Verificacion de maquetado: solapamientos, desbordes y salidas de lienzo.

    Se ejecuta al generar cada figura para que un ajuste manual de coordenadas no
    pueda dejar dos cajas superpuestas sin que salte a la vista.
    """
    problems = []
    names = list(boxes)
    for i, a in enumerate(names):
        A = boxes[a]
        if A["left"] < 0 or A["top"] < 0 or A["right"] > canvas.w or A["bottom"] > canvas.h:
            problems.append(f"{a} se sale del lienzo ({canvas.w}x{canvas.h})")
        for b in names[i + 1:]:
            B = boxes[b]
            if (A["left"] < B["right"] - pad and B["left"] < A["right"] - pad
                    and A["top"] < B["bottom"] - pad and B["top"] < A["bottom"] - pad):
                problems.append(f"solapamiento: {a} <-> {b}")
    problems.extend(dict.fromkeys(canvas.warnings))
    if problems:
        for p in problems:
            print("  PROBLEMA:", p)
    else:
        print("  maquetado verificado: sin solapamientos ni desbordes")
    return problems


class Canvas:
    """Lienzo SVG de coordenadas explicitas."""

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.body: list[str] = []
        self.warnings: list[str] = []

    # ---------------------------------------------------------------- basicos
    def rect(self, x, y, w, h, fill="white", stroke=RULE, sw=1.2, rx=0, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.body.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
        )

    def text(self, x, y, s, size=15, fill=INK, bold=False, anchor="start", italic=False):
        st = f' font-style="italic"' if italic else ""
        fw = ' font-weight="600"' if bold else ""
        self.body.append(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONT}" font-size="{size}" '
            f'fill="{fill}" text-anchor="{anchor}"{fw}{st}>{escape(s)}</text>'
        )

    def line(self, x1, y1, x2, y2, stroke=INK, sw=1.4, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.body.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round"{d}/>'
        )

    def path(self, d, stroke=INK, sw=1.4, fill="none", dash=None, marker=None):
        da = f' stroke-dasharray="{dash}"' if dash else ""
        mk = f' marker-end="url(#{marker})"' if marker else ""
        self.body.append(
            f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" '
            f'stroke-linejoin="round" stroke-linecap="round"{da}{mk}/>'
        )

    # ----------------------------------------------------------------- paneles
    def panel(self, x, y, w, h, label, accent="#44546A"):
        self.rect(x, y, w, h, fill=PANEL_BG, stroke=PANEL_RULE, sw=1.2, rx=10)
        if label:
            self.text(x + 18, y + 26, label, size=15, fill=accent, bold=True)

    # ----------------------------------------------------- caja tipo "entidad"
    def entity(self, x, y, w, title, subtitle, rows, palette="slate",
               title_size=17, row_size=15, dashed=False):
        """Caja tabular: cabecera con nombre + nombre fisico, y filas de atributos.

        rows: lista de dicts {key, text, note, fill}
        Devuelve dict con geometria util para conectar aristas.
        """
        accent, tint, border = PALETTE[palette]
        head_h = 40 if not subtitle else 56
        # altura de cada fila
        heights = []
        for r in rows:
            if r.get("sep") is not None:
                heights.append(24)
                continue
            h = 30 if row_size >= 15 else 26
            if r.get("note"):
                h += 17 * len(r["note"].split("\n"))
            if r.get("text") and "\n" in r["text"]:
                h += 21 * (len(r["text"].split("\n")) - 1)
            heights.append(h)
        total = head_h + sum(heights)

        dash = "5 4" if dashed else None
        self.rect(x, y, w, total, fill="white", stroke=border, sw=1.3, dash=dash)
        # cabecera
        self.body.append(
            f'<path d="M {x:.1f} {y + 8:.1f} a 8 8 0 0 1 8 -8 h {w - 16:.1f} '
            f'a 8 8 0 0 1 8 8 v {head_h - 8:.1f} h {-w:.1f} Z" fill="{accent}"/>'
        )
        cx = x + w / 2
        self.text(cx, y + (25 if subtitle else 27), title, size=title_size,
                  fill="white", bold=True, anchor="middle")
        if subtitle:
            self.text(cx, y + 45, subtitle, size=12, fill="#DCE4EA", anchor="middle")

        ports = {}
        cy = y + head_h
        for r, rh in zip(rows, heights):
            if r.get("sep") is not None:
                self.rect(x, cy, w, rh, fill="#F4F6F8", stroke=border, sw=0.9)
                if r["sep"]:
                    self.text(x + 12, cy + 17, r["sep"], size=11, fill=accent, bold=True)
                cy += rh
                continue
            fill = r.get("fill") or "white"
            if fill == "tint":
                fill = tint
            self.rect(x, cy, w, rh, fill=fill, stroke=border, sw=0.9)
            tx = x + 12
            baseline = cy + 21
            key = r.get("key")
            if key:
                self.text(tx, baseline, key, size=row_size, fill=accent, bold=True)
                tx += text_width(key, row_size, bold=True) + 10
            for i, ln in enumerate((r.get("text") or "").split("\n")):
                self.text(tx if i == 0 else x + 12, baseline + 21 * i, ln, size=row_size, fill=INK)
                if text_width(ln, row_size) + (tx - x) > w - 8:
                    self.warnings.append(f"overflow: {ln!r} en caja {title!r}")
            if r.get("note"):
                ny = baseline + 21 * len((r.get("text") or "").split("\n")) - 4
                for i, ln in enumerate(r["note"].split("\n")):
                    self.text(x + 12, ny + 17 * i, ln, size=12, fill=MUTED)
            if r.get("port"):
                ports[r["port"]] = cy + rh / 2
            cy += rh

        return {
            "x": x, "y": y, "w": w, "h": total,
            "left": x, "right": x + w, "top": y, "bottom": y + total,
            "cx": x + w / 2, "cy": y + total / 2,
            "ports": ports,
        }

    # -------------------------------------------------------------- conectores
    def crow(self, x, y, direction, stroke=INK, sw=1.4, size=11):
        """Pata de gallo (lado 'muchos'). direction in {'r','l','d','u'}."""
        s = size
        if direction == "r":
            pts = [(x - s, y), (x, y - s * 0.62), (x, y), (x, y + s * 0.62)]
            self.line(x - s, y, x, y - s * 0.62, stroke, sw)
            self.line(x - s, y, x, y + s * 0.62, stroke, sw)
        elif direction == "l":
            self.line(x + s, y, x, y - s * 0.62, stroke, sw)
            self.line(x + s, y, x, y + s * 0.62, stroke, sw)
        elif direction == "d":
            self.line(x, y - s, x - s * 0.62, y, stroke, sw)
            self.line(x, y - s, x + s * 0.62, y, stroke, sw)
        else:
            self.line(x, y + s, x - s * 0.62, y, stroke, sw)
            self.line(x, y + s, x + s * 0.62, y, stroke, sw)

    def one_tick(self, x, y, vertical=False, stroke=INK, sw=1.4, size=7):
        if vertical:
            self.line(x - size, y, x + size, y, stroke, sw)
        else:
            self.line(x, y - size, x, y + size, stroke, sw)

    # ---------------------------------------------------------------- salida
    def svg(self) -> str:
        defs = (
            '<defs>'
            '<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" '
            'markerHeight="8" orient="auto-start-reverse">'
            '<path d="M 0 0 L 10 5 L 0 10 z" fill="#3C4650"/></marker>'
            '<marker id="arrowTeal" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" '
            'markerHeight="8" orient="auto-start-reverse">'
            '<path d="M 0 0 L 10 5 L 0 10 z" fill="#0F5E52"/></marker>'
            '<marker id="arrowMuted" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            'markerHeight="7" orient="auto-start-reverse">'
            '<path d="M 0 0 L 10 5 L 0 10 z" fill="#8A929C"/></marker>'
            '<marker id="arrowCrimson" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            'markerHeight="7" orient="auto-start-reverse">'
            '<path d="M 0 0 L 10 5 L 0 10 z" fill="#7A3B3B"/></marker>'
            '</defs>'
        )
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" '
            f'viewBox="0 0 {self.w} {self.h}">'
            f'{defs}'
            f'<rect x="0" y="0" width="{self.w}" height="{self.h}" fill="#FFFFFF"/>'
            + "".join(self.body)
            + "</svg>"
        )

    def save(self, svg_path, png_path, scale=2.0):
        import cairosvg

        with open(svg_path, "w", encoding="utf-8") as fh:
            fh.write(self.svg())
        cairosvg.svg2png(
            url=svg_path,
            write_to=png_path,
            scale=scale,
            background_color="#FFFFFF",
        )
        if self.warnings:
            for w in dict.fromkeys(self.warnings):
                print("  aviso:", w)
        print(f"  {png_path}  ({int(self.w * scale)}x{int(self.h * scale)} px)")
