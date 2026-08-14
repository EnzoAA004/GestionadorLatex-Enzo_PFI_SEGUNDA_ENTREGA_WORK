"""Figura 10.6 - Flujo de interaccion end-to-end (carriles por actor).

Verificado contra el codigo en:
  Frontend  9f9d1c1 : NewAnalysisDrawer.tsx (patientReady + caseIdReady),
            patientStudyAssociation.ts (associated | conflict | error),
            retryPatientAssociation(), productAnalysisApi.ts (siempre /api/ai/…)
  Backend   646f4a1 : StudyPatientController PUT /api/studies/{caseId}/patient
  AI Module ea8d91b : POST /inputs/study -> classify_study_series(),
            /v2/series-segmentation/run, /v2/degenerative-findings/disc-multitask

Regla arquitectonica: el Frontend nunca invoca al AI Module de forma directa.
El lienzo es deliberadamente angosto (1430 unidades) para que el texto siga
siendo legible cuando la figura se inserta a 0.92\\textwidth en A4.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pfi_diagram import (  # noqa: E402
    BLUE, FILL, GREEN, GREY, INK_SOFT, ORANGE, PURPLE, RED, TEAL, Scene,
)

W, H = 1430, 1046
s = Scene(W, H)

s.title(
    "Recorrido end-to-end por actor",
    "Autenticacion → Patient → Study → corrida → persistencia → asociacion → revision",
    size=23,
)

LANES = [
    ("PROFESIONAL / FRONTEND", BLUE, 100, 250),
    ("BACKEND", GREEN, 362, 128),
    ("AI MODULE", PURPLE, 502, 258),
    ("POSTGRESQL / ASSETS", TEAL, 772, 100),
]
LX, LW, BAND = 20, 104, 1390
X0, PITCH, BW = 132, 209, 190
F1, F2 = 16.0, 14.5


def col(i: int) -> float:
    return X0 + i * PITCH


for name, color, y, h in LANES:
    s.rect(LX, y, BAND, h, fill="#fbfcfe", stroke="#e2e8f1", width=1.0, rx=3)
    s.rect(LX, y, LW, h, fill=FILL.get(color, "#eef2f7"), stroke=color,
           width=1.2, rx=3)
    words = name.split(" / ")
    cy = y + h / 2 - (len(words) - 1) * 11 + 6
    for wd in words:
        s.text(LX + LW / 2, cy, wd, size=13, weight="bold", color=color,
               anchor="middle")
        cy += 22

# --------------------------------------------------------------- frontend
auth = s.node("auth", col(0), 112, BW, 58,
              ["1. Autenticacion", "sesion y rol"], color=BLUE, font=F1)
pat = s.node("patient", col(0), 180, BW, 82,
             ["2. Patient", "seleccionar o crear", "patientReference"],
             color=BLUE, font=F1)
study = s.node("study", col(1), 180, BW, 82,
               ["3. Datos del Study", "caseId y metadata"], color=BLUE, font=F1)
upload = s.node("upload", col(1), 272, BW, 68,
                ["4. Carga del ZIP", "DICOM completo"], color=BLUE,
                font=F1)
reopen = s.node("reopen", col(5), 112, BW, 58,
                ["13. Reapertura", "e historial"], color=BLUE, font=F1)
work = s.node("work", col(5), 180, BW, 82,
              ["12. Espacio de", "revision", "profesional"], color=BLUE, font=F1)

# ---------------------------------------------------------------- backend
api_pat = s.node("api_pat", col(0), 376, BW, 100,
                 ["API de pacientes", "POST · GET", "/api/patients"],
                 color=GREEN, font=F1)
valid = s.node("valid", col(1), 376, BW, 100,
               ["5. Validacion", "y autorizacion", "del Study"], color=GREEN,
               font=F1)
norm = s.node("norm", col(4), 376, BW, 100,
              ["9. Validacion y", "normalizacion", "de contratos"],
              color=GREEN, font=F1)
assign = s.node("assign", col(5), 376, BW, 100,
                ["11. Asociar Study", "→ Patient", "PUT /api/studies/",
                 "{caseId}/patient"], color=GREEN, font=F1)

# -------------------------------------------------------------- ai module
ingest = s.node("ingest", col(2), 514, BW, 92,
                ["6. Ingesta del ZIP", "clasificacion", "de series"],
                color=PURPLE, font=F1)
inputs = s.node("inputs", col(2), 620, BW, 110,
                ["7. Inputs", "registrados", "Sagital T1 · T2", "Axial"],
                color=PURPLE, font=F1)
runbox = s.node("run", col(3), 514, BW, 92,
                ["8. Corrida", "segmentacion", "y mediciones"], color=PURPLE,
                font=F1)
ext1 = s.node("ext1", col(3), 620, BW, 58,
              ["8a. Segmentacion", "full-series"], color=PURPLE, font=F2)
ext2 = s.node("ext2", col(3), 692, BW, 58,
              ["8b. Hallazgos P10.7", "disc multitask"], color=PURPLE, font=F2)

# ------------------------------------------------------------- persistencia
db_pat = s.node("db_pat", col(0), 786, BW, 72,
                ["domain_patients", "identidad longitudinal"], color=TEAL,
                font=F1)
db_run = s.node("db_run", col(4), 786, BW, 72,
                ["10. Persistencia", "PostgreSQL y assets"], color=TEAL,
                font=F1)


# ---------------------------------------------------------------- conectores
def flow(d, color=GREY, width=1.8, dash=None, marker="arrow"):
    s.path(d, color=color, width=width, dash=dash, marker=marker)


flow(f"M {auth.cx} {auth.bottom} L {auth.cx} {pat.y - 3}", color=BLUE)
flow(f"M {pat.right} {pat.cy} L {study.x - 3} {pat.cy}", color=BLUE)
flow(f"M {pat.cx} {pat.bottom} L {pat.cx} {api_pat.y - 3}", color=BLUE)
flow(f"M {api_pat.cx} {api_pat.bottom} L {api_pat.cx} {db_pat.y - 3}",
     color=TEAL)
flow(f"M {study.cx} {study.bottom} L {study.cx} {upload.y - 3}", color=BLUE)
flow(f"M {upload.cx} {upload.bottom} L {upload.cx} {valid.y - 3}", color=BLUE)
flow(f"M {valid.right} {valid.cy} L {ingest.cx} {valid.cy} "
     f"L {ingest.cx} {ingest.y - 3}", color=GREEN)
flow(f"M {ingest.cx} {ingest.bottom} L {ingest.cx} {inputs.y - 3}", color=PURPLE)
flow(f"M {inputs.right} {inputs.cy} L {inputs.right + 10} {inputs.cy} "
     f"L {inputs.right + 10} {runbox.cy} L {runbox.x - 3} {runbox.cy}",
     color=PURPLE)
flow(f"M {runbox.cx} {runbox.bottom} L {runbox.cx} {ext1.y - 3}", color=PURPLE,
     dash="6 4", width=1.4)
flow(f"M {ext1.cx} {ext1.bottom} L {ext1.cx} {ext2.y - 3}", color=PURPLE,
     dash="6 4", width=1.4)
s.text(ext2.x, ext2.bottom + 22, "extensiones compatibles del contrato",
       size=13.5, weight="italic", color=INK_SOFT)

# convergencia AI -> Backend
flow(f"M {runbox.right} {runbox.cy} L {norm.cx - 48} {runbox.cy} "
     f"L {norm.cx - 48} {norm.bottom + 3}", color=PURPLE)
flow(f"M {ext1.right} {ext1.cy} L {norm.cx} {ext1.cy} "
     f"L {norm.cx} {norm.bottom + 3}", color=PURPLE, dash="6 4", width=1.4)
flow(f"M {ext2.right} {ext2.cy} L {norm.cx + 48} {ext2.cy} "
     f"L {norm.cx + 48} {norm.bottom + 3}", color=PURPLE, dash="6 4", width=1.4)

# Backend -> persistencia -> asociacion -> revision
flow(f"M {norm.cx + 72} {norm.bottom} L {norm.cx + 72} {db_run.y - 3}",
     color=GREEN)
flow(f"M {db_run.right} {db_run.cy} L {assign.cx} {db_run.cy} "
     f"L {assign.cx} {assign.bottom + 3}", color=TEAL)
flow(f"M {assign.right} {assign.cy} L {W - 42} {assign.cy} "
     f"L {W - 42} {work.cy} L {work.right + 3} {work.cy}", color=GREEN)
s.text(assign.right - 6, 348, "asociacion correcta", size=13.5,
       weight="italic", color=GREEN, anchor="end")
flow(f"M {work.cx} {work.y} L {work.cx} {reopen.bottom + 3}", color=BLUE)

# --------------------------------------------------------- rama de excepcion
s.rect(LX, 886, BAND, 130, fill="#fdf8f5", stroke="#e8d3c6", width=1.1, rx=4)
s.text(LX + 18, 914, "RAMA DE EXCEPCION DE LA ASOCIACION", size=14,
       weight="bold", color=ORANGE, letter_spacing=0.8)
for i, ln in enumerate([
        "El analisis ya fue persistido",
        "antes de asociar el Study:",
        "ninguna de las dos salidas",
        "repite la inferencia.",
]):
    s.text(LX + 18, 942 + i * 20, ln, size=13.5, color=INK_SOFT)

err1 = s.node("err1", 470, 902, 440, 98,
              ["Error de asociacion",
               "el Frontend ofrece reintentar",
               "la operacion sobre el Study",
               "ya persistido"], color=ORANGE, font=F1)
err2 = s.node("err2", 940, 902, 450, 98,
              ["Conflicto HTTP 409",
               "el Study fue asociado a otro",
               "Patient: requiere revision manual",
               "y no se reasigna automaticamente"], color=RED, font=F1)

flow(f"M {assign.cx - 34} {assign.bottom} L {assign.cx - 34} 866 "
     f"L {err1.cx} 866 L {err1.cx} {err1.y - 3}", color=ORANGE, dash="6 4",
     width=1.5)
flow(f"M {assign.cx + 34} {assign.bottom} L {assign.cx + 34} 882 "
     f"L {err2.cx} 882 L {err2.cx} {err2.y - 3}", color=RED, dash="6 4",
     width=1.5)

# ------------------------------------------------------------------ leyenda
s.text(LX, 1036,
       "La frontera publica es Frontend → Backend → AI Module: el Frontend nunca "
       "invoca al AI Module de forma directa y el retorno vuelve por el Backend.",
       size=14, weight="italic", color=INK_SOFT)

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", "..", "images", "architecture",
                       "fig_10_06_flujo_end_to_end.png")
    s.render(os.path.normpath(out), scale=2.6)
