from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
PNG_PATH = ROOT / "images" / "methodology" / "fig_12_01_sistemas_identificacion.png"
SVG_PATH = ROOT / "diagrams" / "methodology" / "fig_12_01_sistemas_identificacion.svg"

WIDTH = 2600
HEIGHT = 1450
MARGIN = 95
LANE_GAP = 42
LANE_WIDTH = WIDTH - 2 * MARGIN

WHITE = "#ffffff"
LANE_FILL = "#f4f4f4"
CHIP_FILL = "#ffffff"
BORDER = "#4d4d4d"
TEXT = "#111111"
MUTED = "#333333"


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/segoeuib.ttf" if bold else "C:/Windows/Fonts/segoeui.ttf",
    ]
    for candidate in candidates:
        path = Path(candidate)
        if path.exists():
            return ImageFont.truetype(str(path), size=size)
    return ImageFont.load_default()


FONT_TITLE = load_font(34, bold=True)
FONT_BODY = load_font(31)
FONT_CHIP = load_font(29)
FONT_SMALL = load_font(27)


class Svg:
    def __init__(self) -> None:
        self.parts: list[str] = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
            f'<rect width="{WIDTH}" height="{HEIGHT}" fill="{WHITE}"/>',
        ]

    def rect(self, xy: tuple[int, int, int, int], fill: str, stroke: str = BORDER, radius: int = 8, width: int = 3) -> None:
        x0, y0, x1, y1 = xy
        self.parts.append(
            f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" rx="{radius}" ry="{radius}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'
        )

    def text(self, x: int, y: int, value: str, size: int, bold: bool = False, anchor: str = "start") -> None:
        weight = "700" if bold else "400"
        self.parts.append(
            f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{TEXT}" text-anchor="{anchor}">{escape(value)}</text>'
        )

    def line(self, x0: int, y0: int, x1: int, y1: int) -> None:
        self.parts.append(
            f'<line x1="{x0}" y1="{y0}" x2="{x1}" y2="{y1}" stroke="{TEXT}" stroke-width="3" marker-end="url(#arrow)"/>'
        )

    def finish(self) -> str:
        defs = (
            '<defs><marker id="arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" '
            'orient="auto" markerUnits="strokeWidth"><path d="M0,0 L10,4 L0,8 Z" fill="#111111"/></marker></defs>'
        )
        self.parts.insert(2, defs)
        self.parts.append("</svg>")
        return "\n".join(self.parts)


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def draw_text(draw: ImageDraw.ImageDraw, svg: Svg, xy: tuple[int, int], text: str, font: ImageFont.FreeTypeFont, size: int, bold: bool = False) -> None:
    draw.text(xy, text, font=font, fill=TEXT)
    svg.text(xy[0], xy[1] + size, text, size=size, bold=bold)


def draw_chip(draw: ImageDraw.ImageDraw, svg: Svg, x: int, y: int, label: str, font: ImageFont.FreeTypeFont = FONT_CHIP) -> tuple[int, int, int, int]:
    tw, th = text_size(draw, label, font)
    pad_x, pad_y = 18, 10
    box = (x, y, x + tw + 2 * pad_x, y + th + 2 * pad_y)
    draw.rounded_rectangle(box, radius=5, fill=CHIP_FILL, outline=BORDER, width=3)
    draw.text((x + pad_x, y + pad_y - 2), label, font=font, fill=TEXT)
    svg.rect(box, fill=CHIP_FILL, radius=5, width=3)
    svg.text(x + pad_x, y + pad_y + 25, label, size=29)
    return box


def draw_arrow(draw: ImageDraw.ImageDraw, svg: Svg, start: tuple[int, int], end: tuple[int, int]) -> None:
    draw.line((start, end), fill=TEXT, width=4)
    x, y = end
    draw.polygon([(x, y), (x - 16, y - 9), (x - 16, y + 9)], fill=TEXT)
    svg.line(start[0], start[1], end[0], end[1])


def draw_lane(draw: ImageDraw.ImageDraw, svg: Svg, y: int, height: int, title: str) -> tuple[int, int, int, int]:
    box = (MARGIN, y, MARGIN + LANE_WIDTH, y + height)
    draw.rounded_rectangle(box, radius=12, fill=LANE_FILL, outline=BORDER, width=3)
    svg.rect(box, fill=LANE_FILL, radius=12, width=3)
    draw_text(draw, svg, (MARGIN + 36, y + 26), title, FONT_TITLE, 34, bold=True)
    return box


def main() -> None:
    PNG_PATH.parent.mkdir(parents=True, exist_ok=True)
    SVG_PATH.parent.mkdir(parents=True, exist_ok=True)

    image = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(image)
    svg = Svg()

    y = MARGIN

    draw_lane(draw, svg, y, 235, "Nivel académico / producto")
    chip_y = y + 100
    x = MARGIN + 50
    boxes = []
    for label in ["E1", "E2", "...", "E10"]:
        box = draw_chip(draw, svg, x, chip_y, label)
        boxes.append(box)
        x = box[2] + 28
    draw_text(
        draw,
        svg,
        (boxes[-1][2] + 70, chip_y + 15),
        "Épicas derivadas del user research y los requerimientos",
        FONT_BODY,
        31,
    )

    y += 235 + LANE_GAP
    draw_lane(draw, svg, y, 330, "Backlogs técnicos por repositorio")
    row_y = y + 105
    x = MARGIN + 50
    for prefix, label in [
        ("AI Module:", "AI-*"),
        ("Backend:", "BE-*"),
        ("Frontend:", "FE-* / FE-RD-* / FE-P1...FE-P8"),
        ("Infraestructura:", "DEV-*"),
    ]:
        draw_text(draw, svg, (x, row_y + 10), prefix, FONT_BODY, 31)
        prefix_w, _ = text_size(draw, prefix, FONT_BODY)
        box = draw_chip(draw, svg, x + prefix_w + 14, row_y, label, FONT_SMALL)
        x = box[2] + 34

    note_y = y + 225
    note1 = draw_chip(draw, svg, MARGIN + 50, note_y, "E experimental ≠ épica académica E", FONT_SMALL)
    draw_chip(draw, svg, note1[2] + 45, note_y, "FE-P8 ≠ checkpoint P8", FONT_SMALL)

    y += 330 + LANE_GAP
    draw_lane(draw, svg, y, 330, "Checkpoints coordinados de producto")
    chip_y = y + 103
    labels = ["P8", "P9", "P10", "P10.5", "P10.6", "P10.7", "P10.8", "P10.9"]
    x = MARGIN + 50
    checkpoint_boxes = []
    for index, label in enumerate(labels):
        box = draw_chip(draw, svg, x, chip_y, label)
        checkpoint_boxes.append(box)
        x = box[2] + 54
        if index < len(labels) - 1:
            start = (box[2] + 10, (box[1] + box[3]) // 2)
            end = (x - 12, (box[1] + box[3]) // 2)
            draw_arrow(draw, svg, start, end)

    sub_y = y + 226
    draw_text(draw, svg, (MARGIN + 50, sub_y + 12), "Dentro de P10.5:", FONT_BODY, 31)
    left_w, _ = text_size(draw, "Dentro de P10.5:", FONT_BODY)
    sub1 = draw_chip(draw, svg, MARGIN + 50 + left_w + 22, sub_y, "P10.5-A", FONT_SMALL)
    draw_text(draw, svg, (sub1[2] + 24, sub_y + 15), "...", FONT_BODY, 31)
    sub2 = draw_chip(draw, svg, sub1[2] + 82, sub_y, "P10.5-F", FONT_SMALL)
    draw_text(draw, svg, (sub2[2] + 70, sub_y + 14), "Objetivos compartidos entre repositorios", FONT_BODY, 31)

    y += 330 + LANE_GAP
    draw_lane(draw, svg, y, 225, "Convención auxiliar")
    aux_y = y + 105
    aux1 = draw_chip(draw, svg, MARGIN + 50, aux_y, "EN-01", FONT_SMALL)
    draw_text(draw, svg, (aux1[2] + 24, aux_y + 15), "...", FONT_BODY, 31)
    aux2 = draw_chip(draw, svg, aux1[2] + 82, aux_y, "EN-05", FONT_SMALL)
    draw_text(draw, svg, (aux2[2] + 70, aux_y + 14), "Profesionales entrevistados", FONT_BODY, 31)

    image.save(PNG_PATH, optimize=True)
    SVG_PATH.write_text(svg.finish(), encoding="utf-8")
    print(f"Wrote {PNG_PATH} ({WIDTH}x{HEIGHT})")
    print(f"Wrote {SVG_PATH}")


if __name__ == "__main__":
    main()
