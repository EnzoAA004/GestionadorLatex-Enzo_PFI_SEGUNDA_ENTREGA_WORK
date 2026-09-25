"""Figura 12.2 - Automatizacion de integracion y publicacion en Google Cloud.

Muestra el flujo validado GitHub -> GitHub Actions -> autenticacion federada
(OIDC/WIF) -> Artifact Registry, y lo distingue visualmente de la promocion
hacia Cloud Run, que se mantiene como una accion controlada y separada (no
un despliegue automatico).

Fuente del workflow real: cloud-03-publish-image.yml en los repositorios
Backend (PFI_MVPTest_Enzo_Backend), Frontend (PFI_MVPTest_Enzo_Frontend) y
AI Module (PFI_MVPTest_Enzo_AImodule). Backend y Frontend se ejecutan sobre
ramas Cloud aisladas o mediante workflow_dispatch; AI Module publica su
imagen mediante workflow_dispatch manual.

Uso:  python fig_12_02_publicacion_cloud_wif.py
Dependencias: cairosvg, pillow (reutiliza diagrams/architecture/pfi_diagram.py).
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "..", "architecture"))

import pfi_diagram  # noqa: E402

# El modulo compartido referencia fuentes DejaVu por ruta absoluta de Linux.
# En un entorno sin esas rutas (p. ej. Windows) se reutilizan las mismas
# fuentes DejaVu ya empaquetadas con matplotlib, sin modificar el modulo
# compartido en disco (no se toca ninguna figura del Capitulo 10).
if not os.path.exists(pfi_diagram.FONT_REGULAR):
    import matplotlib
    _ttf = os.path.join(os.path.dirname(matplotlib.__file__), "mpl-data",
                         "fonts", "ttf")
    pfi_diagram.FONT_REGULAR = os.path.join(_ttf, "DejaVuSans.ttf")
    pfi_diagram.FONT_BOLD = os.path.join(_ttf, "DejaVuSans-Bold.ttf")
    pfi_diagram.FONT_ITALIC = os.path.join(_ttf, "DejaVuSans-Oblique.ttf")

from pfi_diagram import (  # noqa: E402
    BLUE, FILL, GREEN, GREY, INK, INK_SOFT, ORANGE, PURPLE, RED, TEAL, Scene,
)

W, H = 1430, 1180
s = Scene(W, H)

s.title(
    "Automatizacion de integracion y publicacion en Google Cloud",
    "GitHub -> GitHub Actions -> autenticacion federada (OIDC/WIF) -> Artifact Registry -> promocion controlada a Cloud Run",
    size=20,
)

LX, LW, BAND = 20, 118, 1390

LANES = [
    ("CODIGO\nFUENTE", BLUE, 90, 130),
    ("GITHUB\nACTIONS", GREEN, 240, 170),
    ("AUTENTICACION\nFEDERADA", PURPLE, 430, 190),
    ("ARTIFACT\nREGISTRY", TEAL, 640, 190),
    ("CLOUD RUN", ORANGE, 850, 130),
]

for name, color, y, h in LANES:
    s.rect(LX, y, BAND, h, fill="#fbfcfe", stroke="#e2e8f1", width=1.0, rx=3)
    s.rect(LX, y, LW, h, fill=FILL.get(color, "#eef2f7"), stroke=color,
           width=1.2, rx=3)
    words = name.split("\n")
    cy = y + h / 2 - (len(words) - 1) * 11 + 6
    for wd in words:
        s.text(LX + LW / 2, cy, wd, size=13, weight="bold", color=color,
               anchor="middle")
        cy += 22

# --------------------------------------------------------------- bloque 1
CODE_X = [140, 550, 960]
CODE_W = 380
be = s.node("be_repo", CODE_X[0], 110, CODE_W, 90,
            ["Backend repository", "PFI_MVPTest_Enzo_Backend"],
            color=BLUE, font=14)
fe = s.node("fe_repo", CODE_X[1], 110, CODE_W, 90,
            ["Frontend repository", "PFI_MVPTest_Enzo_Frontend"],
            color=BLUE, font=14)
ai = s.node("ai_repo", CODE_X[2], 110, CODE_W, 90,
            ["AI Module repository", "PFI_MVPTest_Enzo_AImodule"],
            color=BLUE, font=14)

# --------------------------------------------------------------- bloque 2
s.text(140, 262, "Workflow: cloud-03-publish-image.yml", size=14,
       weight="bold", color=GREEN)
STEP_X = [165, 475, 785, 1095]
STEP_W = 290
trig = s.node("trigger", STEP_X[0], 280, STEP_W, 80,
              ["Disparo", "push a rama Cloud aislada", "o workflow_dispatch"],
              color=GREEN, font=13)
chk = s.node("checkout", STEP_X[1], 280, STEP_W, 80,
             ["checkout", "codigo del repositorio"], color=GREEN, font=13)
bx = s.node("buildx", STEP_X[2], 280, STEP_W, 80,
            ["Docker Buildx", "build multi-plataforma"], color=GREEN,
            font=13)
build = s.node("build", STEP_X[3], 280, STEP_W, 80,
               ["Build de imagen", "contenedor versionado"], color=GREEN,
               font=13)

# --------------------------------------------------------------- bloque 3
AUTH_X = [140, 550, 960]
oidc = s.node("oidc", AUTH_X[0], 452, CODE_W, 80,
              ["GitHub OIDC token", "identidad temporal de", "corta duracion"],
              color=PURPLE, font=13)
wif = s.node("wif", AUTH_X[1], 452, CODE_W, 80,
             ["Workload Identity", "Federation", "vincula el token al proyecto GCP"],
             color=PURPLE, font=13)
sa = s.node("sa", AUTH_X[2], 452, CODE_W, 80,
            ["Service account de", "publicacion", "permisos acotados a Artifact Registry"],
            color=PURPLE, font=13)
s.rect(140, 546, 1200, 54, fill="#f2eefa", stroke=PURPLE, width=1.0, rx=4)
s.text(140 + 600, 578,
       "Sin clave JSON permanente de cuenta de servicio almacenada en el repositorio",
       size=13.5, weight="italic", color=PURPLE, anchor="middle")

# --------------------------------------------------------------- bloque 4
REG_X = [140, 550, 960]
r_be = s.node("r_be", REG_X[0], 662, CODE_W, 80,
              ["backend:<git SHA>"], color=TEAL, font=14)
r_fe = s.node("r_fe", REG_X[1], 662, CODE_W, 80,
              ["frontend:<git SHA>"], color=TEAL, font=14)
r_ai = s.node("r_ai", REG_X[2], 662, CODE_W, 80,
              ["ai:<git SHA>"], color=TEAL, font=14)
s.rect(140, 756, 1200, 54, fill="#e8f5f5", stroke=TEAL, width=1.0, rx=4)
s.text(140 + 600, 788,
       "Imagenes versionadas por commit: no se utiliza la etiqueta :latest",
       size=13.5, weight="italic", color=TEAL, anchor="middle")

# --------------------------------------------------------------- bloque 5
RUN_X = [140, 550, 960]
cr_fe = s.node("cr_fe", RUN_X[0], 880, CODE_W, 80,
               ["Cloud Run", "Frontend"], color=ORANGE, font=14)
cr_be = s.node("cr_be", RUN_X[1], 880, CODE_W, 80,
               ["Cloud Run", "Backend (Green)"], color=ORANGE, font=14)
cr_ai = s.node("cr_ai", RUN_X[2], 880, CODE_W, 80,
               ["Cloud Run", "AI Module"], color=ORANGE, font=14)


# ------------------------------------------------------------- conectores
def flow(d, color=GREY, width=1.8, dash=None):
    s.path(d, color=color, width=width, dash=dash, marker="arrow")


SPINE1 = 715  # entre bloque 1 y 2
SPINE2 = 715  # entre bloque 2 y 3
SPINE3 = 715  # entre bloque 3 y 4
SPINE4 = 715  # entre bloque 4 y 5 (promocion)

# bloque 1 -> spine -> trigger (bloque 2)
for node in (be, fe, ai):
    flow(f"M {node.cx} {node.bottom} L {node.cx} 232 L {SPINE1} 232", color=BLUE)
flow(f"M {SPINE1} 232 L {trig.cx} 232 L {trig.cx} {trig.y - 3}", color=BLUE)

# cadena de pasos dentro de GitHub Actions
flow(f"M {trig.right} {trig.cy} L {chk.x - 3} {chk.cy}", color=GREEN)
flow(f"M {chk.right} {chk.cy} L {bx.x - 3} {bx.cy}", color=GREEN)
flow(f"M {bx.right} {bx.cy} L {build.x - 3} {build.cy}", color=GREEN)

# bloque 2 -> spine -> bloque 3 (abanico)
flow(f"M {build.cx} {build.bottom} L {build.cx} 422 L {SPINE2} 422", color=GREEN)
for node in (oidc, wif, sa):
    flow(f"M {SPINE2} 422 L {node.cx} 422 L {node.cx} {node.y - 3}", color=GREEN)

# bloque 3 -> spine -> bloque 4 (abanico), automatizacion (linea continua)
flow(f"M {sa.cx} {sa.bottom} L {sa.cx} 632 L {SPINE3} 632", color=PURPLE)
for node in (r_be, r_fe, r_ai):
    flow(f"M {SPINE3} 632 L {node.cx} 632 L {node.cx} {node.y - 3}", color=PURPLE)

# bloque 4 -> bloque 5: promocion / despliegue controlado (linea punteada)
flow(f"M {r_be.cx} {r_be.bottom} L {r_be.cx} 842 L {SPINE4} 842",
     color=ORANGE, dash="7 5")
for node in (cr_fe, cr_be, cr_ai):
    flow(f"M {SPINE4} 842 L {node.cx} 842 L {node.cx} {node.y - 3}",
         color=ORANGE, dash="7 5")
s.text(SPINE4 + 14, 838, "promocion / despliegue controlado", size=13.5,
       weight="italic", color=ORANGE, anchor="start")

# ------------------------------------------------------------------ leyenda
LEG_Y = 1000
s.rect(LX, LEG_Y, BAND, 150, fill="#fbfcfe", stroke="#e2e8f1", width=1.0, rx=3)
s.line(140, LEG_Y + 30, 210, LEG_Y + 30, color=GREY, width=2.2)
s.text(222, LEG_Y + 35, "Flujo automatizado validado: GitHub -> Actions -> "
       "autenticacion federada -> Artifact Registry", size=13.5, color=INK)
s.line(140, LEG_Y + 58, 210, LEG_Y + 58, color=ORANGE, width=2.2, dash="7 5")
s.text(222, LEG_Y + 63, "Promocion / despliegue controlado hacia Cloud Run "
       "(no es un despliegue automatico)", size=13.5, color=INK)
s.text(140, LEG_Y + 100,
       "Backend y Frontend: rama Cloud aislada o workflow_dispatch. "
       "AI Module: publicacion mediante workflow_dispatch manual.",
       size=13, weight="italic", color=INK_SOFT)
s.text(140, LEG_Y + 124,
       "Cloud Run consume imagenes ya publicadas en Artifact Registry; "
       "un push a GitHub no despliega Cloud Run automaticamente.",
       size=13, weight="italic", color=INK_SOFT)

def _render_windows_fallback(scene: Scene, png_path: str, scale: float = 2.6) -> None:
    """Rasteriza sin depender de la libreria nativa libcairo (no disponible
    en este entorno Windows). Usa resvg_py, que trae su propio motor de
    render (sin dependencias externas), en lugar de modificar
    pfi_diagram.render() (compartido con las figuras del Capitulo 10)."""
    issues = scene.check_layout()
    if issues:
        raise SystemExit("Layout invalido: se aborta el render.\n" +
                          "\n".join(issues))

    import resvg_py

    svg_path = os.path.splitext(png_path)[0] + ".svg"
    os.makedirs(os.path.dirname(os.path.abspath(png_path)), exist_ok=True)
    with open(svg_path, "w", encoding="utf-8") as fh:
        fh.write(scene.svg())

    png_bytes = resvg_py.svg_to_bytes(
        svg_path=svg_path,
        background="#ffffff",
        width=int(scene.width * scale),
        height=int(scene.height * scale),
        font_family="DejaVu Sans",
        sans_serif_family="DejaVu Sans",
        font_files=[pfi_diagram.FONT_REGULAR, pfi_diagram.FONT_BOLD,
                    pfi_diagram.FONT_ITALIC],
    )
    with open(png_path, "wb") as fh:
        fh.write(bytes(png_bytes))
    size = os.path.getsize(png_path)
    print(f"PNG: {png_path}  {int(scene.width * scale)}x{int(scene.height * scale)} px "
          f"({size / 1024:.0f} kB)")


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "..", "..", "images", "methodology",
                        "fig_12_02_publicacion_cloud_wif.png")
    try:
        s.render(os.path.normpath(out), scale=2.6)
    except OSError:
        _render_windows_fallback(s, os.path.normpath(out), scale=2.6)
