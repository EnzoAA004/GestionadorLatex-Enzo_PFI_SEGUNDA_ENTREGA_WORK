"""Figura 10.4 - Modelo de datos relacional (PostgreSQL).

Contrastado con las migraciones reales del Backend (docs/migrations/*.sql,
docs/postgres_schema.sql) en el commit 646f4a1:

  - domain_patients (V20260812_016_patient_domain_foundation.sql)
  - domain_studies.patient_id UUID NULL -> domain_patients(id) ON DELETE RESTRICT
  - subject_ref permanece como atributo opcional, sin PK ni FK hacia un Subject

No existe tabla SUBJECT: no debe aparecer en el diagrama.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pfi_diagram import (  # noqa: E402
    BLUE, GREEN, GREY, INK, INK_SOFT, ORANGE, PURPLE, RED, TEAL, Scene,
)

W, H = 1560, 900
s = Scene(W, H)

s.title(
    "Entidades principales y relaciones del modelo de datos",
    "Identidad longitudinal de-identificada (Patient) → Study → corrida y evidencia del analisis",
)

COL_A, COL_B, COL_C, COL_D, COL_E = 25, 330, 635, 945, 1250
WA, WB, WC, WD, WE = 280, 280, 285, 270, 285

# ---------------------------------------------------------------- identidad
usuario = s.entity(
    "doctor_accounts", COL_A, 100, WA, "DOCTOR_ACCOUNTS",
    [
        ("PK", "id : TEXT"),
        ("UQ", "email"),
        ("", "password_hash"),
        ("", "roles {ADMIN|DOCTOR|REVIEWER}"),
        ("", "verified, approved"),
        ("", "created_at, updated_at"),
    ],
    color=BLUE,
)
s.text(COL_A, 92, "identidad y control de acceso", size=12.5, weight="italic",
       color=INK_SOFT)
auditoria = s.entity(
    "domain_audit_events", COL_A, 330, WA, "DOMAIN_AUDIT_EVENTS",
    [
        ("PK", "id : UUID"),
        ("", "actor, action"),
        ("", "entity_id : TEXT"),
        ("", "trace_id : TEXT"),
        ("", "metadata : JSONB"),
        ("", "created_at"),
    ],
    color=GREY,
)
for i, ln in enumerate([
        "los roles se almacenan como lista embebida;",
        "no existe tabla intermedia usuario-rol.",
        "acciones auditadas: PATIENT_CREATED,",
        "PATIENT_UPDATED, STUDY_PATIENT_ASSIGNED",
        "y STUDY_PATIENT_REASSIGNED.",
]):
    s.text(COL_A + 4, auditoria.bottom + 18 + i * 16, ln, size=12.5, color=INK_SOFT)

modelo = s.entity(
    "modelo_artifact", COL_A, 600, WA, "MODELO / ARTIFACT",
    [
        ("", "model_key, plano, version"),
        ("", "artifact_hash, manifest_uri"),
        ("", "registro fuera de PostgreSQL"),
    ],
    color=ORANGE,
)

# ---------------------------------------------------------------- longitudinal
patient = s.entity(
    "domain_patients", COL_B, 100, WB, "DOMAIN_PATIENTS",
    [
        ("PK", "id : UUID"),
        ("UQ", "patient_reference : TEXT"),
        ("", "created_at"),
        ("", "updated_at"),
    ],
    color=GREEN,
)
s.text(COL_B, 92, "identidad longitudinal de-identificada", size=12.5,
       weight="italic", color=INK_SOFT)
s.text(COL_B + 4, patient.bottom + 18,
       "UQ por indice funcional normalizado:", size=12.5, color=INK_SOFT)
s.text(COL_B + 4, patient.bottom + 36,
       "lower(btrim(patient_reference))", size=12.5, color=INK_SOFT)

study = s.entity(
    "domain_studies", COL_B, 330, WB, "DOMAIN_STUDIES",
    [
        ("PK", "id : UUID"),
        ("UQ", "case_id : TEXT"),
        ("FK", "patient_id : UUID NULL"),
        ("", "subject_ref : TEXT NULL (opcional)"),
        ("", "status"),
        ("", "study_date, modality"),
        ("", "description"),
        ("", "review_priority {low|medium|high}"),
        ("", "created_at, updated_at"),
    ],
    color=GREEN,
)
s.text(COL_B + 4, study.bottom + 18,
       "subject_ref: solo indice no unico; no es PK", size=12.5, color=INK_SOFT)
s.text(COL_B + 4, study.bottom + 36,
       "ni FK y no infiere identidad longitudinal.", size=12.5, color=INK_SOFT)

# ---------------------------------------------------------------- evidencia
inputs = s.entity(
    "domain_input_resources", COL_C, 100, WC, "DOMAIN_INPUT_RESOURCES",
    [
        ("PK", "id : UUID"),
        ("FK", "study_id : UUID"),
        ("UQ", "input_id : TEXT"),
        ("", "plane {sagittal|axial}"),
        ("", "format, size_bytes"),
        ("", "description, weighting"),
        ("", "slice_count, multiplanar"),
        ("", "derived, analyzable"),
        ("", "created_at"),
    ],
    color=TEAL,
)
s.text(COL_C, 92, "catalogo de series y cortes (P10.5)", size=12.5,
       weight="italic", color=INK_SOFT)

run = s.entity(
    "domain_study_runs", COL_C, 380, WC, "DOMAIN_STUDY_RUNS",
    [
        ("PK", "id : UUID"),
        ("FK", "study_id : UUID"),
        ("UQ", "multiplanar_run_id"),
        ("", "trace_id"),
        ("", "requested_inference_mode"),
        ("", "effective_inference_mode"),
        ("", "sagittal / axial_model_key"),
        ("", "sagittal / axial_artifact_hash"),
        ("", "metrics_snapshot : JSONB"),
        ("", "assets : JSONB"),
        ("", "status, review_status"),
        ("", "reviewer, reviewed_at, comments"),
    ],
    color=PURPLE,
)
s.text(COL_C + 4, run.bottom + 18,
       "las mediciones automaticas se conservan", size=12.5, color=INK_SOFT)
s.text(COL_C + 4, run.bottom + 36,
       "en metrics_snapshot (JSONB).", size=12.5, color=INK_SOFT)

assets = s.entity(
    "domain_run_artifacts", COL_D, 380, WD, "DOMAIN_RUN_ARTIFACTS",
    [
        ("PK", "id : UUID"),
        ("FK", "study_run_id : UUID"),
        ("UQ", "(run, plane, asset_name)"),
        ("", "run_id, plane"),
        ("", "asset_name, content_type"),
        ("", "artifact_ref"),
        ("", "storage_status, storage_kind"),
        ("", "size_bytes, sha256"),
        ("", "created_at"),
    ],
    color=ORANGE,
)
s.text(COL_D, 374, "assets del analisis", size=12.5, weight="italic",
       color=INK_SOFT)

payload = s.entity(
    "domain_run_asset_payloads", COL_D, 640, WD, "DOMAIN_RUN_ASSET_PAYLOADS",
    [
        ("PK", "artifact_id : UUID (FK)"),
        ("", "content : BYTEA"),
        ("", "size_bytes, storage_kind"),
        ("", "stored_at"),
    ],
    color=ORANGE,
)

anotaciones = s.entity(
    "domain_reviewer_annotations", COL_E, 100, WE, "DOMAIN_REVIEWER_ANNOTATIONS",
    [
        ("PK", "id : UUID"),
        ("FK", "study_run_id : UUID"),
        ("", "scope, kind, measurement_kind"),
        ("", "plane, series_id, slice_index"),
        ("", "level, points : JSONB"),
        ("", "value, unit, text"),
        ("", "author, created_at"),
    ],
    color=RED,
)
s.text(COL_E, 92, "mediciones y revision profesional", size=12.5,
       weight="italic", color=INK_SOFT)

correcciones = s.entity(
    "domain_review_corrections", COL_E, 350, WE, "DOMAIN_REVIEW_CORRECTIONS",
    [
        ("PK", "id : UUID"),
        ("FK", "study_run_id : UUID"),
        ("", "measurement_id, label"),
        ("", "before_value : JSONB"),
        ("", "after_value : JSONB"),
        ("", "comment, created_at"),
    ],
    color=RED,
)
s.text(COL_E + 4, correcciones.bottom + 18,
       "la correccion no sobrescribe el resultado", size=12.5, color=INK_SOFT)
s.text(COL_E + 4, correcciones.bottom + 36,
       "automatico original.", size=12.5, color=INK_SOFT)

# ---------------------------------------------------------------- relaciones
def rel(d, color=GREY, width=1.4, dash=None, marker="arrow"):
    s.path(d, color=color, width=width, dash=dash, marker=marker)


# PATIENT 1 --- 0..* STUDY  (relacion central de esta actualizacion)
px = patient.right - 22
rel(f"M {px} {patient.bottom} L {px} {study.y - 11}", color=GREEN, width=1.9,
    marker=None)
s.one_bar(px, patient.bottom + 13, orient="h", color=GREEN, width=1.9, size=13)
s.crowfoot(px, study.y - 11, direction="b", color=GREEN, width=1.9, size=11)
s.text(px + 8, patient.bottom + 20, "1", size=13, weight="bold", color=GREEN)
s.text(px + 8, study.y - 26, "0..*", size=13, weight="bold", color=GREEN)
s.pill(COL_B + 130, patient.bottom + 80,
       "patient_id · ON DELETE RESTRICT", font=11, color=GREEN)

# STUDY 1 --- 0..* INPUT_RESOURCES
rel(f"M {study.right} 380 L 622 380 L 622 250 L {inputs.x - 11} 250", marker=None)
s.one_bar(study.right + 12, 380, orient="v")
s.crowfoot(inputs.x - 11, 250, direction="r")

# STUDY 1 --- 0..* STUDY_RUNS
rel(f"M {study.right} 470 L {run.x - 11} 470", marker=None)
s.one_bar(study.right + 12, 470, orient="v")
s.crowfoot(run.x - 11, 470, direction="r")

# STUDY_RUNS 1 --- 0..* RUN_ARTIFACTS
rel(f"M {run.right} 470 L {assets.x - 11} 470", marker=None)
s.one_bar(run.right + 12, 470, orient="v")
s.crowfoot(assets.x - 11, 470, direction="r")

# RUN_ARTIFACTS 1 --- 0..1 PAYLOAD
rel(f"M {assets.cx} {assets.bottom} L {assets.cx} {payload.y}", marker=None)
s.one_bar(assets.cx, assets.bottom + 12, orient="h")
s.one_bar(assets.cx, payload.y - 12, orient="h")
s.text(assets.cx + 14, (assets.bottom + payload.y) / 2 + 4, "0..1", size=12,
       color=INK_SOFT)

# STUDY_RUNS 1 --- 0..* REVIEWER_ANNOTATIONS  y  REVIEW_CORRECTIONS
rel(f"M {run.x + 200} {run.y} L {run.x + 200} 352 L 1232 352 L 1232 200 "
    f"L {anotaciones.x - 11} 200", marker=None)
s.one_bar(run.x + 200, run.y - 12, orient="h")
s.crowfoot(anotaciones.x - 11, 200, direction="r")
rel(f"M 1232 352 L 1232 430 L {correcciones.x - 11} 430", marker=None)
s.crowfoot(correcciones.x - 11, 430, direction="r")


# Referencias logicas (sin FK)
rel(f"M {usuario.cx} {usuario.bottom} L {usuario.cx} {auditoria.y}",
    dash="5 4", width=1.2)
s.text(usuario.cx + 8, (usuario.bottom + auditoria.y) / 2 + 4, "actor", size=11,
       weight="italic", color=INK_SOFT)
rel(f"M {modelo.right} 640 L 622 640 L 622 600 L {run.x} 600",
    dash="5 4", width=1.2, color=ORANGE)
s.text(COL_B + 4, 632, "model_key + artifact_hash", size=11, weight="italic",
       color=INK_SOFT)

# ---------------------------------------------------------------- leyenda
s.rect(25, 796, 1510, 82, fill="#f7f9fc", stroke="#dbe2ec", width=1.0, rx=4)
s.text(45, 822, "Notacion:", size=13, weight="bold", color=INK)
s.text(122, 822,
       "PK = clave primaria · FK = clave foranea · UQ = restriccion de unicidad "
       "· linea continua = FK real en PostgreSQL · linea punteada = referencia "
       "logica sin FK · las relaciones hacia la evidencia usan ON DELETE CASCADE.",
       size=13, color=INK_SOFT)
s.text(45, 846,
       "Cardinalidad: la barra indica el lado 1 y la pata de gallo el lado 0..* "
       "· los nombres corresponden a las tablas fisicas de las migraciones "
       "(V20260716_005 … V20260812_016).",
       size=13, color=INK_SOFT)
s.text(45, 870,
       "Los estudios historicos permanecen con patient_id = NULL: la migracion es "
       "aditiva y no reconstruye pacientes a partir de subject_ref.",
       size=13, weight="italic", color=GREEN)

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", "..", "images", "architecture",
                       "fig_10_04_modelo_datos.png")
    s.render(os.path.normpath(out), scale=2.4)
