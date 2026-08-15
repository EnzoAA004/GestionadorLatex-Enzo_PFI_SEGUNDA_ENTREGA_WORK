#!/usr/bin/env python3
"""Figura 10.4 - Modelo de datos relacional (PostgreSQL).

Fuente editable de images/architecture/fig_10_04_modelo_datos.png.

Contrastado contra el esquema real del Backend (EnzoAA004/PFI_MVPTest_Enzo_Backend
@ 646f4a1):
  docs/postgres_schema.sql
  docs/migrations/V20260716_005_study_input_run_model.sql
  docs/migrations/V20260725_008_study_worklist_metadata.sql
  docs/migrations/V20260726_009_run_asset_payloads.sql
  docs/migrations/V20260730_013_reviewer_annotations.sql
  docs/migrations/V20260803_014_annotation_measurement_kind.sql
  docs/migrations/V20260805_015_study_series_catalog.sql
  docs/migrations/V20260812_016_patient_domain_foundation.sql

Decisiones que el diagrama refleja y que provienen del codigo, no del enunciado:
  - la identidad longitudinal es domain_patients; la asociacion es
    domain_studies.patient_id (UUID NULL, fk_domain_studies_patient,
    ON DELETE RESTRICT);
  - subject_ref sobrevive como atributo opcional de domain_studies: no es PK de
    ningun Subject, no es FK hacia ninguna entidad y no se usa para inferir
    identidad longitudinal;
  - no existe entidad SUBJECT en el esquema.

El bitmap no lleva titulo ni caption: los aporta LaTeX.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pfi_diagram import Canvas, INK, MUTED, check_layout  # noqa: E402

W, H = 1500, 920
BOX = 250
COL = [28, 323, 618, 913, 1208]
ROW = 16
TITLE = 18

c = Canvas(W, H)


def group_label(x, y, s, color):
    c.text(x, y, s, size=13, fill=color, bold=True)


# ---------------------------------------------------------------- identidad
group_label(COL[0], 46, "IDENTIDAD Y ACCESO", "#44546A")

usuario = c.entity(
    COL[0], 60, BOX, "USUARIO", "doctor_accounts",
    [
        {"key": "PK", "text": "id", "fill": "tint", "port": "pk"},
        {"key": "UQ", "text": "email"},
        {"text": "password_hash"},
        {"text": "roles", "note": "{ADMIN | DOCTOR | REVIEWER}"},
        {"text": "verified, approved"},
    ],
    palette="slate", title_size=TITLE, row_size=ROW,
)

auditoria = c.entity(
    COL[0], 340, BOX, "EVENTO DE AUDITORIA", "domain_audit_events",
    [
        {"key": "PK", "text": "id", "fill": "tint"},
        {"text": "actor, action",
         "note": "PATIENT_CREATED, PATIENT_UPDATED,\nSTUDY_PATIENT_ASSIGNED,\nSTUDY_PATIENT_REASSIGNED"},
        {"text": "entity_id, trace_id"},
        {"text": "metadata : JSONB"},
        {"text": "created_at"},
    ],
    palette="crimson", title_size=TITLE, row_size=ROW,
)

# ------------------------------------------------- identidad longitudinal
group_label(COL[1], 46, "IDENTIDAD LONGITUDINAL", "#0F5E52")

patient = c.entity(
    COL[1], 150, BOX, "PATIENT", "domain_patients",
    [
        {"key": "PK", "text": "id : UUID", "fill": "tint", "port": "pk"},
        {"key": "UQ", "text": "patient_reference",
         "note": "unicidad normalizada:\nlower(btrim(patient_reference))"},
        {"text": "created_at"},
        {"text": "updated_at"},
        {"text": "sin identificadores directos",
         "note": "del paciente (Ley 25.326)"},
    ],
    palette="teal", title_size=TITLE, row_size=ROW,
)

# ------------------------------------------------------------------ estudio
group_label(COL[2], 46, "ESTUDIOS Y SERIES", "#1F4E79")

study = c.entity(
    COL[2], 60, BOX, "STUDY", "domain_studies",
    [
        {"key": "PK", "text": "id : UUID", "fill": "tint", "port": "pk"},
        {"key": "UQ", "text": "case_id"},
        {"key": "FK", "text": "patient_id : UUID NULL", "fill": "tint", "port": "patient_id"},
        {"text": "subject_ref : TEXT NULL",
         "note": "referencia opcional de compatibilidad;\nno es identidad longitudinal"},
        {"text": "status"},
        {"text": "study_date, modality"},
        {"text": "description"},
        {"text": "review_priority", "note": "{low | medium | high}"},
        {"text": "created_at, updated_at"},
    ],
    palette="navy", title_size=TITLE, row_size=ROW,
)

serie = c.entity(
    COL[2], 530, BOX, "CATALOGO DE SERIES", "domain_input_resources",
    [
        {"key": "PK", "text": "id", "fill": "tint"},
        {"key": "FK", "text": "study_id", "fill": "tint", "port": "fk"},
        {"key": "UQ", "text": "input_id"},
        {"text": "plane, weighting, slices",
         "note": "{sagittal | axial | coronal | unknown}"},
        {"text": "analyzable, derived",
         "note": "multiplanar, format, size_bytes"},
    ],
    palette="amber", title_size=TITLE, row_size=ROW,
)

# ------------------------------------------------------------------ corrida
group_label(COL[3], 46, "CORRIDA DE ANALISIS", "#4A3A80")

run = c.entity(
    COL[3], 60, BOX, "CORRIDA (RUN)", "domain_study_runs",
    [
        {"key": "PK", "text": "id", "fill": "tint", "port": "pk"},
        {"key": "FK", "text": "study_id", "fill": "tint", "port": "fk"},
        {"key": "UQ", "text": "multiplanar_run_id"},
        {"text": "trace_id"},
        {"text": "sagittal/axial_model_key\nsagittal/axial_artifact_hash"},
        {"text": "requested_inference_mode\neffective_inference_mode"},
        {"text": "metrics_snapshot : JSONB",
         "note": "mediciones y landmarks de la corrida"},
        {"text": "assets : JSONB, status"},
        {"text": "review_status, reviewer",
         "note": "{pending | accepted | observed |\nrejected | edited}"},
        {"text": "reviewed_at, comments"},
        {"text": "created_at, updated_at"},
    ],
    palette="purple", title_size=TITLE, row_size=ROW,
)

modelo = c.entity(
    COL[3], 640, BOX, "MODELO / ARTIFACT", "registro de artifacts verificables",
    [
        {"text": "model_key", "fill": "tint"},
        {"text": "plano, version"},
        {"text": "artifact_hash"},
        {"text": "manifest_uri, arquitectura"},
    ],
    palette="grey", title_size=TITLE, row_size=ROW, dashed=True,
)

# ---------------------------------------------------------------- evidencia
group_label(COL[4], 46, "EVIDENCIA DE LA CORRIDA", "#7A5C1E")

medicion = c.entity(
    COL[4], 60, BOX, "MEDICION / ANOTACION", "domain_reviewer_annotations",
    [
        {"key": "PK", "text": "id", "fill": "tint"},
        {"key": "FK", "text": "study_run_id", "fill": "tint", "port": "fk"},
        {"text": "scope, kind",
         "note": "{study | level | slice}\n{measurement | marker | note}"},
        {"text": "measurement_kind",
         "note": "{distance | angle | listhesis | roi}"},
        {"text": "plane, series_id, slice"},
        {"text": "points : JSONB, value, unit"},
    ],
    palette="amber", title_size=TITLE, row_size=ROW,
)

revision = c.entity(
    COL[4], 400, BOX, "REVISION / CORRECCION", "domain_review_corrections",
    [
        {"key": "PK", "text": "id", "fill": "tint"},
        {"key": "FK", "text": "study_run_id", "fill": "tint", "port": "fk"},
        {"text": "measurement_id, label"},
        {"text": "before_value : JSONB\nafter_value : JSONB",
         "note": "no sobrescribe el resultado automatico"},
    ],
    palette="amber", title_size=TITLE, row_size=ROW,
)

asset = c.entity(
    COL[4], 650, BOX, "ASSET", "domain_run_artifacts",
    [
        {"key": "PK", "text": "id", "fill": "tint"},
        {"key": "FK", "text": "study_run_id", "fill": "tint", "port": "fk"},
        {"text": "asset_name, plane",
         "note": "content_type, artifact_ref"},
        {"text": "storage_status, sha256",
         "note": "payload opcional en\ndomain_run_asset_payloads"},
    ],
    palette="amber", title_size=TITLE, row_size=ROW,
)

# ------------------------------------------------------------------ aristas
TEAL = "#0F5E52"
NAVY = "#1F4E79"
GREY = "#54606E"


def h_rel(src, src_port, dst, dst_port, color=GREY, sw=1.5, one="1", many="0..*",
          bias=0.5):
    """Relacion horizontal 1 -> muchos entre dos cajas contiguas."""
    y1 = src["ports"][src_port]
    y2 = dst["ports"][dst_port]
    x1, x2 = src["right"], dst["left"]
    xm = x1 + (x2 - x1) * bias
    c.path(f"M {x1} {y1} H {xm} V {y2} H {x2 - 12}", stroke=color, sw=sw)
    c.crow(x2, y2, "r", stroke=color, sw=sw)
    c.one_tick(x1 + 11, y1, stroke=color, sw=sw)
    c.text(x1 + 6, y1 - 10, one, size=13, fill=color)
    c.text(x2 - 12, y2 - 10, many, size=13, fill=color, anchor="end")


def v_rel(src, dst, x, color=GREY, sw=1.5, one="1", many="1..*"):
    y1, y2 = src["bottom"], dst["top"]
    c.path(f"M {x} {y1} V {y2 - 12}", stroke=color, sw=sw)
    c.crow(x, y2, "d", stroke=color, sw=sw)
    c.one_tick(x, y1 + 12, vertical=True, stroke=color, sw=sw)
    c.text(x + 9, y1 + 22, one, size=13, fill=color)
    c.text(x + 9, y2 - 14, many, size=13, fill=color)


# PATIENT 1 -> 0..* STUDY : la relacion estructural del capitulo.
h_rel(patient, "pk", study, "patient_id", color=TEAL, sw=2.2, bias=0.45)
c.rect(COL[1], 470, BOX, 96, fill="#F3F8F7", stroke="#9FC3BB", sw=1.1, rx=6)
c.text(COL[1] + 14, 496, "ASOCIACION EXPLICITA", size=12, fill=TEAL, bold=True)
c.text(COL[1] + 14, 522, "PATIENT.id  →  STUDY.patient_id", size=14, fill=INK)
c.text(COL[1] + 14, 546, "fk_domain_studies_patient", size=12, fill=MUTED)
c.text(COL[1] + BOX - 14, 546, "ON DELETE RESTRICT", size=12, fill=MUTED, anchor="end")

# STUDY 1 -> 1..* RUN
h_rel(study, "pk", run, "fk", color=NAVY, sw=1.8, many="1..*", bias=0.45)

# STUDY 1 -> 1..* CATALOGO DE SERIES (vertical)
v_rel(study, serie, COL[2] + 62)

# RUN 1 -> 0..* evidencia (abanico con corredores separados)
for dst, bias in ((medicion, 0.26), (revision, 0.52), (asset, 0.78)):
    h_rel(run, "pk", dst, "fk", bias=bias)

# RUN -> MODELO / ARTIFACT (referencia logica, sin FK en la base)
c.path(f"M {COL[3] + 62} {run['bottom']} V {modelo['top'] - 4}", stroke="#8A929C",
       sw=1.4, dash="6 5", marker="arrowMuted")
c.text(COL[3] + 72, run["bottom"] + 34, "model_key / artifact_hash", size=12, fill=MUTED)

# USUARIO -> AUDITORIA (actor)
c.path(f"M {COL[0] + 62} {usuario['bottom']} V {auditoria['top'] - 4}", stroke="#7A3B3B",
       sw=1.4, dash="6 5", marker="arrowCrimson")
c.text(COL[0] + 72, usuario["bottom"] + 40, "actor", size=13, fill="#7A3B3B")

# ------------------------------------------------------------------ leyenda
LX, LY, LW, LH = 28, 700, 545, 158
c.rect(LX, LY, LW, LH, fill="#FAFBFC", stroke="#C3CAD3", sw=1.2, rx=8)
c.text(LX + 16, LY + 28, "NOTACION", size=13, fill="#44546A", bold=True)
c.text(LX + 16, LY + 56, "PK clave primaria  ·  FK clave foranea  ·  UQ unicidad", size=14)
c.line(LX + 16, LY + 80, LX + 52, LY + 80, GREY, 1.5)
c.crow(LX + 63, LY + 80, "r", stroke=GREY, sw=1.5)
c.text(LX + 80, LY + 85, "lado “muchos” de la cardinalidad", size=14)
c.line(LX + 16, LY + 108, LX + 63, LY + 108, "#8A929C", 1.4, dash="6 5")
c.text(LX + 80, LY + 113, "referencia logica, sin clave foranea en la base", size=14)
c.text(LX + 16, LY + 142,
       "Los estudios historicos permanecen con patient_id = NULL: no se infieren "
       "pacientes desde subject_ref.", size=12, fill=MUTED)

BOXES = {
    "USUARIO": usuario, "AUDITORIA": auditoria, "PATIENT": patient,
    "STUDY": study, "CATALOGO": serie, "RUN": run, "MODELO": modelo,
    "MEDICION": medicion, "REVISION": revision, "ASSET": asset,
    "leyenda": {"left": LX, "right": LX + LW, "top": LY, "bottom": LY + LH},
    "nota-asociacion": {"left": COL[1], "right": COL[1] + BOX, "top": 470, "bottom": 566},
}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(os.path.dirname(here))
    check_layout(c, BOXES)
    c.save(
        os.path.join(here, "fig_10_04_modelo_datos.svg"),
        os.path.join(repo, "images", "architecture", "fig_10_04_modelo_datos.png"),
        scale=2.4,
    )
