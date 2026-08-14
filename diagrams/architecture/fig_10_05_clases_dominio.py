"""Figura 10.5 - Diagrama de clases del dominio y servicios.

Conceptual (no es un volcado de todas las clases Java). Verificado contra el
Backend en el commit 646f4a1:

  domain/Patient.java, domain/Study.java, domain/StudyRun.java,
  service/PatientService.java (PatientRepository + StudyRepository + AuditService),
  controller/PatientController.java   -> /api/patients
  controller/StudyPatientController.java -> PUT /api/studies/{caseId}/patient
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pfi_diagram import (  # noqa: E402
    BLUE, GREEN, GREY, INK, INK_SOFT, ORANGE, PURPLE, RED, TEAL, Scene,
)

W, H = 1560, 962
s = Scene(W, H)

s.title(
    "Clases del dominio, servicios de aplicacion y contratos de acceso",
    "Patient como identidad longitudinal; la asociacion Study–Patient es explicita y auditable",
)

# ------------------------------------------------------------------ dominio
s.text(40, 92, "DOMINIO", size=12.5, weight="bold", color=INK_SOFT,
       letter_spacing=1.2)
s.text(600, 92, "CONTROLADORES REST", size=12.5, weight="bold", color=INK_SOFT,
       letter_spacing=1.2)
s.text(920, 92, "SERVICIOS DE APLICACION", size=12.5, weight="bold",
       color=INK_SOFT, letter_spacing=1.2)
s.text(1240, 92, "REPOSITORIOS Y CLIENTES", size=12.5, weight="bold",
       color=INK_SOFT, letter_spacing=1.2)
s.line(585, 105, 585, 880, color="#dbe2ec", width=1.2, dash="6 5")

patient = s.uml(
    "Patient", 40, 120, 250, "Patient",
    ["- id : UUID",
     "- patientReference : String",
     "- createdAt : Instant",
     "- updatedAt : Instant"],
    color=GREEN,
)

study = s.uml(
    "Study", 40, 290, 250, "Study",
    ["- id : UUID",
     "- caseId : String",
     "- status : String",
     "- patientId : UUID [0..1]",
     "- subjectRef : String [0..1]",
     "- studyDate : LocalDate",
     "- modality : String",
     "- description : String",
     "- reviewPriority : String",
     "- createdAt : Instant",
     "- updatedAt : Instant"],
    color=GREEN,
)

run = s.uml(
    "StudyRun", 40, 600, 250, "StudyRun",
    ["- id : UUID",
     "- studyId : UUID",
     "- multiplanarRunId : String",
     "- traceId : String",
     "- effectiveInferenceMode",
     "- metricsSnapshot : JSON",
     "- status, reviewStatus"],
    color=PURPLE,
)

inputres = s.uml(
    "InputResource", 320, 120, 250, "InputResource",
    ["- studyId : UUID",
     "- inputId : String",
     "- plane : {sagittal|axial}",
     "- weighting : {t1|t2}",
     "- sliceCount : int",
     "- analyzable : boolean"],
    color=TEAL,
)

artifact = s.uml(
    "RunArtifact", 320, 330, 250, "RunArtifact",
    ["- studyRunId : UUID",
     "- plane : String",
     "- assetName : String",
     "- contentType : String",
     "- artifactRef : String",
     "- sha256 : String"],
    color=ORANGE,
)

annotation = s.uml(
    "ReviewerAnnotation", 320, 560, 250, "ReviewerAnnotation",
    ["- studyRunId : UUID",
     "- kind, measurementKind",
     "- plane, sliceIndex, level",
     "- points : JSON",
     "- value : double, unit",
     "- author : String"],
    color=RED,
)

review = s.uml(
    "RunReview", 320, 740, 250, "RunReview",
    ["- studyRunId : UUID",
     "- status : {pendiente…}",
     "- reviewer, comments",
     "- reviewedAt : Instant"],
    color=RED,
)

# ------------------------------------------------------------- controladores
pat_ctrl = s.uml(
    "PatientController", 600, 120, 270, "PatientController",
    [],
    ["+ create()", "+ search(query, limit)", "+ get(patientId)",
     "+ update(patientId)", "+ studies(patientId)"],
    color=BLUE, stereotype="«REST»  /api/patients",
)

sp_ctrl = s.uml(
    "StudyPatientController", 600, 320, 270, "StudyPatientController",
    [],
    ["+ assign(caseId, request)"],
    color=BLUE, stereotype="«REST»  PUT /api/studies/{caseId}/patient", font=13.2,
)

study_ctrl = s.uml(
    "StudyController", 600, 450, 270, "StudyController",
    [],
    ["+ worklist()", "+ detail(caseId)"],
    color=BLUE, stereotype="«REST»  /api/studies",
)

ai_ctrl = s.uml(
    "AiMultiplanarController", 600, 600, 270, "AiMultiplanarController",
    [],
    ["+ run(request)", "+ productAnalysis()"],
    color=BLUE, stereotype="«REST»  /api/ai/…",
)

rev_ctrl = s.uml(
    "AiRunReviewController", 600, 750, 270, "AiRunReviewController",
    [],
    ["+ review(runId, decision)"],
    color=BLUE, stereotype="«REST»  /api/ai/runs/…",
)

# ---------------------------------------------------------------- servicios
pat_srv = s.uml(
    "PatientService", 920, 120, 250, "PatientService",
    ["- patientRepository",
     "- studyRepository",
     "- auditService"],
    ["+ create() / update()",
     "+ search() / get()",
     "+ studies(patientId)",
     "+ assignStudy(caseId, req)"],
    color=GREEN, stereotype="«service»",
)

audit_srv = s.uml(
    "AuditService", 920, 380, 250, "AuditService",
    [],
    ["+ record(actor, action,", "   entityId, traceId)"],
    color=GREY, stereotype="«service»",
)

run_srv = s.uml(
    "StudyRunService", 920, 500, 250, "StudyRunService",
    [],
    ["+ registerRun()", "+ latestRun(caseId)"],
    color=PURPLE, stereotype="«service»",
)

pers_srv = s.uml(
    "MultiplanarRunPersistence", 920, 630, 250, "MultiplanarRunPersistenceService",
    [],
    ["+ persist(canonicalRun)"],
    color=PURPLE, stereotype="«service»", font=11.0,
)

rev_srv = s.uml(
    "RunReviewService", 920, 750, 250, "RunReviewService",
    [],
    ["+ saveReview()", "+ corrections(runId)"],
    color=RED, stereotype="«service»",
)

# ------------------------------------------------------ repositorios y cliente
pat_repo = s.uml(
    "PatientRepository", 1240, 120, 290, "PatientRepository",
    [],
    ["+ save(patient)", "+ findById(patientId)",
     "+ searchByReferencePrefix()", "+ updateReference()"],
    color=GREEN, stereotype="«interface»",
)
s.text(1244, pat_repo.bottom + 18, "impl.: PostgresPatientRepository /",
       size=12.5, color=INK_SOFT)
s.text(1244, pat_repo.bottom + 36, "InMemoryPatientRepository", size=11,
       color=INK_SOFT)

study_repo = s.uml(
    "StudyRepository", 1240, 330, 290, "StudyRepository",
    [],
    ["+ findStudyByCaseId(caseId)",
     "+ findStudiesByPatientId(id)",
     "+ updatePatientIfExpected(caseId,",
     "    patientId, expectedPatientId)",
     "+ saveRun() / saveReview()"],
    color=GREEN, stereotype="«interface»",
)
s.text(1244, study_repo.bottom + 18, "impl.: PostgresStudyRepository /",
       size=12.5, color=INK_SOFT)
s.text(1244, study_repo.bottom + 36, "InMemoryStudyRepository", size=11,
       color=INK_SOFT)

ai_client = s.uml(
    "AiServiceClient", 1240, 640, 290, "AiServiceClient",
    [],
    ["+ runPipeline(request)",
     "+ seriesSegmentation()",
     "+ discDegenerativeFindings()"],
    color=PURPLE, stereotype="«interface» AiServiceOperations",
)
s.text(1244, ai_client.bottom + 18, "unica frontera hacia el AI Module:", size=12.5,
       weight="italic", color=INK_SOFT)
s.text(1244, ai_client.bottom + 36, "el Frontend nunca lo invoca directamente.",
       size=12.5, weight="italic", color=INK_SOFT)


# ---------------------------------------------------------------- relaciones
def dep(d, color=GREY):
    s.path(d, color=color, width=1.25, dash="5 4", marker="arrowopen")


def assoc(d, color=GREY, marker=None, width=1.4):
    s.path(d, color=color, width=width, marker=marker)


# Patient 1 -- 0..* Study (asociacion opcional del lado Study)
cx = patient.cx
assoc(f"M {cx} {patient.bottom} L {cx} {study.y}", color=GREEN, width=1.9)
s.text(cx + 8, patient.bottom + 20, "1", size=14, weight="bold", color=GREEN)
s.text(cx + 8, study.y - 8, "0..*", size=14, weight="bold", color=GREEN)
s.text(205, 268, "patientId : opcional", size=12.5, weight="italic",
       color=GREEN)

# Study 1 -- 0..* StudyRun (composicion)
assoc(f"M {cx} {study.bottom} L {cx} {run.y}", color=PURPLE, width=1.6,
      marker="diamond")
s.text(cx + 10, run.y - 14, "0..*", size=12.5, color=INK_SOFT)

# Study -- InputResource ; StudyRun -- RunArtifact / ReviewerAnnotation / RunReview
assoc(f"M {study.right} 330 L 305 330 L 305 200 L {inputres.x} 200")
s.text(297, 195, "0..*", size=11.5, color=INK_SOFT)
assoc(f"M {run.right} 640 L 305 640 L 305 400 L {artifact.x} 400")
s.text(297, 395, "0..*", size=11.5, color=INK_SOFT)
assoc(f"M {run.right} 620 L {annotation.x} 620")
s.text(297, 615, "0..*", size=11.5, color=INK_SOFT)
assoc(f"M {cx} {run.bottom} L {cx} 820 L {review.x} 820")
s.text(297, 815, "0..*", size=11.5, color=INK_SOFT)

# Controladores -> servicios
dep(f"M {pat_ctrl.right} 170 L {pat_srv.x} 170", color=BLUE)
dep(f"M {sp_ctrl.right} 360 L 895 360 L 895 250 L {pat_srv.x} 250", color=BLUE)
dep(f"M {study_ctrl.right} 530 L {run_srv.x} 530", color=BLUE)
dep(f"M {ai_ctrl.right} 665 L {pers_srv.x} 665", color=BLUE)
dep(f"M {rev_ctrl.right} 790 L {rev_srv.x} 790", color=BLUE)

# Servicios -> repositorios / auditoria
dep(f"M {pat_srv.right} 160 L {pat_repo.x} 160", color=GREEN)
dep(f"M {pat_srv.right} 300 L 1200 300 L 1200 370 L {study_repo.x} 370",
    color=GREEN)
dep(f"M {pat_srv.cx} {pat_srv.bottom} L {pat_srv.cx} {audit_srv.y}", color=GREY)
s.text(pat_srv.cx + 8, pat_srv.bottom + 22, "audita la asociacion", size=12.5,
       weight="italic", color=INK_SOFT)
dep(f"M {run_srv.right} 540 L 1185 540 L 1185 405 L {study_repo.x} 405",
    color=PURPLE)
dep(f"M {rev_srv.right} 800 L 1215 800 L 1215 440 L {study_repo.x} 440",
    color=RED)
dep(f"M {pers_srv.cx} {pers_srv.y} L {pers_srv.cx} {run_srv.bottom}",
    color=PURPLE)
dep(f"M {pers_srv.right} 700 L {ai_client.x} 700", color=PURPLE)

# Servicios <-> dominio (referencias conceptuales)
s.text(600, 908, "PatientService concentra la creacion y busqueda de Patient, "
       "el listado de Studies asociados y la asociacion o reasignacion "
       "Study → Patient.", size=13, color=INK_SOFT)
s.text(600, 930, "assignStudy() exige INITIAL_ASSIGNMENT en la primera "
       "asociacion y CORRECTION en una reasignacion; no permite desasociar.",
       size=13, color=INK_SOFT)

# ---------------------------------------------------------------- leyenda
s.rect(40, 890, 530, 56, fill="#f7f9fc", stroke="#dbe2ec", width=1.0, rx=4)
s.text(56, 914, "Notacion UML simplificada:", size=13, weight="bold", color=INK)
s.text(56, 934, "linea llena = asociacion · rombo = composicion · linea "
       "punteada = dependencia (usa).", size=12.5, color=INK_SOFT)

s.text(40, 882, "Las mediciones automaticas no son una clase persistida: se "
       "conservan en StudyRun.metricsSnapshot.", size=12.5, weight="italic",
       color=INK_SOFT)

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "..", "..", "images", "architecture",
                       "fig_10_05_clases_dominio.png")
    s.render(os.path.normpath(out), scale=2.4)
