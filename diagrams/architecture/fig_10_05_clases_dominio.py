#!/usr/bin/env python3
"""Figura 10.5 - Diagrama de clases del dominio y servicios.

Fuente editable de images/architecture/fig_10_05_clases_dominio.png.

Notacion UML simplificada y deliberadamente conceptual: no es un volcado de todas
las clases Java del Backend, sino el recorte que sostiene el capitulo.

Contrastado contra EnzoAA004/PFI_MVPTest_Enzo_Backend @ 646f4a1:
  domain/Patient.java, domain/Study.java, domain/StudyRun.java,
  domain/RunReview.java, domain/MeasurementCorrection.java,
  domain/ReviewerAnnotation.java
  repository/PatientRepository.java, repository/PostgresPatientRepository.java,
  repository/StudyRepository.java, repository/PostgresStudyRepository.java
  service/PatientService.java, service/StudyRunService.java,
  service/RunReviewService.java, service/AuditService.java
  controller/PatientController.java  -> /api/patients
  controller/StudyPatientController.java -> /api/studies/{caseId}/patient
  client/AiServiceOperations.java

No aparece ninguna clase Subject: subjectRef es un atributo opcional de Study y no
una identidad longitudinal.

El bitmap no lleva titulo ni caption: los aporta LaTeX.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pfi_diagram import Canvas, INK, MUTED, check_layout  # noqa: E402

W, H = 1480, 990
BOX = 250
L = [28, 298, 568]          # capas backend
R = [860, 1190]             # dominio (corredor de 80 px para las aristas)
ROW = 15
TITLE = 17

c = Canvas(W, H)


def group_label(x, y, s, color):
    c.text(x, y, s, size=13, fill=color, bold=True)


# ------------------------------------------------------------- controladores
group_label(L[0], 44, "CONTROLADORES REST", "#44546A")

patient_ctrl = c.entity(
    L[0], 58, BOX, "PatientController", "«REST»  /api/patients",
    [
        {"sep": "OPERACIONES"},
        {"key": "+", "text": "create()", "note": "POST /api/patients"},
        {"key": "+", "text": "search()", "note": "GET /api/patients?query"},
        {"key": "+", "text": "get()", "note": "GET /{patientId}"},
        {"key": "+", "text": "update()", "note": "PATCH /{patientId}"},
        {"key": "+", "text": "studies()", "note": "GET /{patientId}/studies"},
    ],
    palette="slate", title_size=TITLE, row_size=ROW,
)

study_patient_ctrl = c.entity(
    L[1], 58, BOX, "StudyPatientController", "«REST»  /api/studies",
    [
        {"sep": "OPERACIONES"},
        {"key": "+", "text": "assign()",
         "note": "PUT /{caseId}/patient\nexpectedPatientId (concurrencia\noptimista) + reason"},
    ],
    palette="slate", title_size=TITLE, row_size=ROW,
)

study_ctrl = c.entity(
    L[2], 58, BOX, "StudyController", "«REST»  /api/studies",
    [
        {"sep": "OPERACIONES"},
        {"key": "+", "text": "list(), get()"},
        {"key": "+", "text": "runs()", "note": "GET /{caseId}/runs"},
        {"key": "+", "text": "upsertMetadata()", "note": "PUT /{caseId}/metadata"},
    ],
    palette="slate", title_size=TITLE, row_size=ROW,
)

# ----------------------------------------------------------------- servicios
group_label(L[0], 396, "SERVICIOS DE APLICACION", "#4A3A80")

patient_svc = c.entity(
    L[0], 410, BOX, "PatientService", "«service»",
    [
        {"sep": "RESPONSABILIDADES"},
        {"key": "+", "text": "create(), get(), update()",
         "note": "alta y correccion de la referencia"},
        {"key": "+", "text": "search()"},
        {"key": "+", "text": "studies()",
         "note": "lista los Studies del Patient"},
        {"key": "+", "text": "assignStudy()",
         "note": "INITIAL_ASSIGNMENT | CORRECTION"},
    ],
    palette="purple", title_size=TITLE, row_size=ROW,
)

run_svc = c.entity(
    L[1], 410, BOX, "StudyRunService", "«service»",
    [
        {"sep": "RESPONSABILIDADES"},
        {"key": "+", "text": "createStudy()"},
        {"key": "+", "text": "upsertStudyMetadata()"},
        {"key": "+", "text": "createInput()"},
        {"key": "+", "text": "persistRun()",
         "note": "via MultiplanarRunPersistenceService"},
    ],
    palette="purple", title_size=TITLE, row_size=ROW,
)

review_svc = c.entity(
    L[2], 410, BOX, "RunReviewService", "«service»",
    [
        {"sep": "RESPONSABILIDADES"},
        {"key": "+", "text": "saveReview()"},
        {"key": "+", "text": "findReview()"},
        {"key": "", "text": "AuditService", "fill": "tint",
         "note": "record() : traza actor, accion,\nentityId y traceId"},
    ],
    palette="purple", title_size=TITLE, row_size=ROW,
)

# ------------------------------------------------------ repositorios/cliente
group_label(L[0], 686, "PERSISTENCIA Y CLIENTE DE IA", "#7A5C1E")

patient_repo = c.entity(
    L[0], 700, BOX, "PatientRepository", "«interface» · PostgresPatientRepository",
    [
        {"sep": "OPERACIONES"},
        {"key": "+", "text": "save()"},
        {"key": "+", "text": "findById()"},
        {"key": "+", "text": "searchByReferencePrefix()"},
        {"key": "+", "text": "updateReference()"},
    ],
    palette="amber", title_size=TITLE, row_size=ROW,
)

study_repo = c.entity(
    L[1], 700, BOX, "StudyRepository", "«interface» · PostgresStudyRepository",
    [
        {"sep": "OPERACIONES"},
        {"key": "+", "text": "saveStudy(), saveRun()"},
        {"key": "+", "text": "findStudyByCaseId()"},
        {"key": "+", "text": "findStudiesByPatientId()"},
        {"key": "+", "text": "updatePatientIfExpected()"},
        {"key": "+", "text": "saveReview()\nsaveAuditEvent()"},
    ],
    palette="amber", title_size=TITLE, row_size=ROW,
)

ai_client = c.entity(
    L[2], 700, BOX, "AiServiceOperations", "«client» · AiServiceClient",
    [
        {"sep": "OPERACIONES"},
        {"key": "+", "text": "uploadStudy()", "note": "ZIP DICOM completo"},
        {"key": "+", "text": "runMultiplanar()"},
        {"key": "+", "text": "predictSubarticular()"},
        {"key": "+", "text": "getAsset()"},
    ],
    palette="amber", title_size=TITLE, row_size=ROW,
)

# ------------------------------------------------------------------- dominio
group_label(R[0], 44, "MODELO DE DOMINIO", "#0F5E52")

patient = c.entity(
    R[0], 58, BOX, "Patient", "identidad longitudinal de-identificada",
    [
        {"sep": "ATRIBUTOS"},
        {"key": "-", "text": "id : UUID", "port": "id"},
        {"key": "-", "text": "patientReference : String"},
        {"key": "-", "text": "createdAt : Instant"},
        {"key": "-", "text": "updatedAt : Instant"},
    ],
    palette="teal", title_size=TITLE, row_size=ROW,
)

study = c.entity(
    R[1], 58, BOX, "Study",
    "contenedor logico de un caso",
    [
        {"sep": "ATRIBUTOS"},
        {"key": "-", "text": "id : String"},
        {"key": "-", "text": "caseId : String"},
        {"key": "-", "text": "status : String"},
        {"key": "-", "text": "patientId : String", "fill": "tint", "port": "patientId",
         "note": "asociacion opcional"},
        {"key": "-", "text": "subjectRef : String",
         "note": "referencia opcional; no es\nidentidad longitudinal"},
        {"key": "-", "text": "studyDate : LocalDate"},
        {"key": "-", "text": "modality : String"},
        {"key": "-", "text": "description : String"},
        {"key": "-", "text": "reviewPriority : String"},
        {"key": "-", "text": "createdAt, updatedAt"},
    ],
    palette="navy", title_size=TITLE, row_size=ROW,
)

study_run = c.entity(
    R[1], 590, BOX, "StudyRun", "corrida multiplanar persistida",
    [
        {"sep": "ATRIBUTOS"},
        {"key": "-", "text": "id, studyId", "port": "id"},
        {"key": "-", "text": "multiplanarRunId, traceId"},
        {"key": "-", "text": "requestedInferenceMode"},
        {"key": "-", "text": "effectiveInferenceMode"},
        {"key": "-", "text": "metricsSnapshot, assets"},
        {"key": "-", "text": "status, reviewStatus"},
    ],
    palette="purple", title_size=TITLE, row_size=ROW,
)

review = c.entity(
    R[0], 400, BOX, "RunReview", "decision profesional",
    [
        {"sep": "ATRIBUTOS"},
        {"key": "-", "text": "reviewStatus, reviewer"},
        {"key": "-", "text": "reviewedAt, comments"},
        {"key": "-", "text": "corrections : List", "port": "corr",
         "note": "MeasurementCorrection"},
    ],
    palette="crimson", title_size=TITLE, row_size=ROW,
)

medicion = c.entity(
    R[0], 660, BOX, "MeasurementCorrection", "ReviewerAnnotation",
    [
        {"sep": "ATRIBUTOS"},
        {"key": "-", "text": "measurementId, label", "port": "id"},
        {"key": "-", "text": "beforeValue, afterValue"},
        {"key": "-", "text": "scope, kind, points", "note": "ReviewerAnnotation"},
        {"key": "-", "text": "value, unit {mm | px}"},
    ],
    palette="crimson", title_size=TITLE, row_size=ROW,
)

# -------------------------------------------------------------------- enlaces
TEAL = "#0F5E52"
GREY = "#6B7480"
CORR = (R[0] + BOX + R[1]) / 2      # corredor vertical del bloque de dominio


def use(x1, y1, x2, y2, mid, label=None, lx=None, ly=None, vertical=True):
    """Dependencia «use»: linea punteada con punta abierta y un unico quiebre."""
    if vertical:
        c.path(f"M {x1} {y1} V {mid} H {x2} V {y2 - 4}", stroke=GREY, sw=1.3,
               dash="5 4", marker="arrowMuted")
    else:
        c.path(f"M {x1} {y1} H {mid} V {y2} H {x2 - 4}", stroke=GREY, sw=1.3,
               dash="5 4", marker="arrowMuted")
    if label:
        c.text(lx, ly, label, size=12, fill=MUTED)


# Controladores -> servicios
use(patient_ctrl["cx"], patient_ctrl["bottom"], patient_svc["cx"], patient_svc["top"],
    392, "usa", patient_ctrl["cx"] + 8, 388)
use(study_patient_ctrl["cx"], study_patient_ctrl["bottom"], patient_svc["cx"] + 70,
    patient_svc["top"], 378, "usa", study_patient_ctrl["cx"] + 8, 374)
use(study_ctrl["cx"] - 55, study_ctrl["bottom"], run_svc["cx"] + 70, run_svc["top"],
    364, "usa", study_ctrl["cx"] - 47, 360)
use(study_ctrl["cx"] + 55, study_ctrl["bottom"], review_svc["cx"] + 55,
    review_svc["top"], 392, "usa", study_ctrl["cx"] + 63, 388)

# Servicios -> repositorios y cliente
use(patient_svc["cx"] - 60, patient_svc["bottom"], patient_repo["cx"],
    patient_repo["top"], 682, "usa", patient_svc["cx"] - 52, 678)
use(patient_svc["cx"] + 60, patient_svc["bottom"], study_repo["cx"] - 70,
    study_repo["top"], 670, "usa StudyRepository", patient_svc["cx"] + 68, 666)
use(run_svc["cx"] + 40, run_svc["bottom"], study_repo["cx"] + 40, study_repo["top"],
    682, "usa", run_svc["cx"] + 48, 678)
use(review_svc["cx"], review_svc["bottom"], ai_client["cx"], ai_client["top"],
    682, "usa", review_svc["cx"] + 8, 678)

# Asociacion Patient "1" ---- "0..*" Study (la asociacion desde Study es opcional)
ya = patient["ports"]["id"]
yb = study["ports"]["patientId"]
c.path(f"M {patient['right']} {ya} H {CORR} V {yb} H {study['left']}", stroke=TEAL, sw=2.0)
c.text(patient["right"] + 6, ya - 9, "1", size=13, fill=TEAL)
c.text(study["left"] - 6, yb - 9, "0..*", size=13, fill=TEAL, anchor="end")

# Study "1" ---- "1..*" StudyRun
c.path(f"M {study['cx']} {study['bottom']} V {study_run['top']}", stroke="#1F4E79", sw=1.8)
c.text(study["cx"] + 9, study["bottom"] + 22, "1", size=13, fill="#1F4E79")
c.text(study["cx"] + 9, study_run["top"] - 12, "1..*", size=13, fill="#1F4E79")

# StudyRun "1" ---- "0..1" RunReview ---- "0..*" MeasurementCorrection
c.path(f"M {study_run['left']} {study_run['ports']['id']} H {CORR} "
       f"V {review['ports']['corr']} H {review['right']}", stroke="#7A3B3B", sw=1.6)
c.text(study_run["left"] - 8, study_run["ports"]["id"] - 9, "1", size=13,
       fill="#7A3B3B", anchor="end")
c.text(review["right"] + 6, review["ports"]["corr"] - 9, "0..1", size=13, fill="#7A3B3B")

c.path(f"M {CORR} {review['ports']['corr']} V {medicion['ports']['id']} "
       f"H {medicion['right']}", stroke="#7A3B3B", sw=1.6)
c.text(medicion["right"] + 6, medicion["ports"]["id"] - 9, "0..*", size=13, fill="#7A3B3B")

# ------------------------------------------------------------------- leyenda
LX, LY, LW, LH = 860, 918, 560, 46
c.rect(LX, LY, LW, LH, fill="#FAFBFC", stroke="#C3CAD3", sw=1.1, rx=6)
c.line(LX + 16, LY + 26, LX + 58, LY + 26, GREY, 1.3, dash="5 4")
c.text(LX + 68, LY + 31, "dependencia «use»", size=13)
c.line(LX + 230, LY + 26, LX + 272, LY + 26, TEAL, 2.0)
c.text(LX + 282, LY + 31, "asociacion con cardinalidad", size=13)

BOXES = {
    "PatientController": patient_ctrl, "StudyPatientController": study_patient_ctrl,
    "StudyController": study_ctrl, "PatientService": patient_svc,
    "StudyRunService": run_svc, "RunReviewService": review_svc,
    "PatientRepository": patient_repo, "StudyRepository": study_repo,
    "AiServiceOperations": ai_client, "Patient": patient, "Study": study,
    "StudyRun": study_run, "RunReview": review, "MeasurementCorrection": medicion,
    "leyenda": {"left": LX, "right": LX + LW, "top": LY, "bottom": LY + LH},
}

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    repo = os.path.dirname(os.path.dirname(here))
    check_layout(c, BOXES)
    c.save(
        os.path.join(here, "fig_10_05_clases_dominio.svg"),
        os.path.join(repo, "images", "architecture", "fig_10_05_clases_dominio.png"),
        scale=2.4,
    )
