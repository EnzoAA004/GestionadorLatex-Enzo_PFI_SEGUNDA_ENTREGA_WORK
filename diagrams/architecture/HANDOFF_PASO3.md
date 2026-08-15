# PASO 3 — Capítulo 10 · Estado del trabajo (handoff)

Sesión interrumpida a pedido del usuario. **No hay commit ni push todavía.**
Branch: `master`, HEAD sin tocar en `f0ccd18` (16avo).

---

## 1. Verificación de repositorios (COMPLETA)

Los tres repos fuente se clonaron y su HEAD **coincide exactamente** con la foto
técnica de referencia. No hay código más nuevo:

| Repo | HEAD real | Referencia del prompt |
|---|---|---|
| `PFI_MVPTest_Enzo_Backend` | `646f4a1` | `646f4a1` ✔ |
| `PFI_MVPTest_Enzo_Frontend` | `9f9d1c1` | `9f9d1c1` ✔ |
| `PFI_MVPTest_Enzo_AImodule` | `ea8d91b` | `ea8d91b` ✔ |

### Hallazgos confirmados contra el código (usar estos, no el prompt)

**Backend — nombres físicos reales**

- `domain_patients` (no `patient`): `id UUID PK`, `patient_reference TEXT NOT NULL`,
  `created_at`, `updated_at`, `CHECK` de no-vacío.
- La unicidad de `patient_reference` **no es un `UNIQUE` de columna**: es el índice
  `uk_domain_patients_reference_normalized ON domain_patients ((lower(btrim(patient_reference))))`.
- `domain_studies` (no `estudio`): `id UUID PK`, `case_id UNIQUE`, `status`,
  `patient_id UUID NULL`, `subject_ref TEXT NULL`, `study_date DATE`, `modality`,
  `description`, `review_priority` (CHECK `low|medium|high`, default `medium`),
  `created_at`, `updated_at`.
- FK real: `fk_domain_studies_patient (patient_id) REFERENCES domain_patients(id)`
  **ON DELETE RESTRICT** — confirmado en `V20260812_016_patient_domain_foundation.sql`.
  La migración es aditiva y **no reconcilia** estudios históricos desde `subject_ref`
  (quedan con `patient_id = NULL`).
- `subject_ref` sólo tiene un índice no único (`V20260726_011_subject_history.sql`).
  No es PK de nada ni FK hacia nada. **No existe tabla ni entidad `SUBJECT`.**
- `Study.java` es un `record` con el orden exacto: `id, caseId, status, patientId,
  subjectRef, studyDate, modality, description, reviewPriority, createdAt, updatedAt`.
- Rutas verificadas: `PatientController` → `/api/patients`
  (`POST /`, `GET /?query&limit`, `GET /{patientId}`, `PATCH /{patientId}`,
  `GET /{patientId}/studies`); `StudyPatientController` → `/api/studies`,
  `PUT /{caseId}/patient`.
- `PatientService` depende de `PatientRepository`, `StudyRepository` **y**
  `AuditService`. `assignStudy()` usa `expectedPatientId` (concurrencia optimista) y
  exige `reason` = `INITIAL_ASSIGNMENT` (primera asociación) o `CORRECTION`
  (reasignación); **no permite desasociar**. Audita `STUDY_PATIENT_ASSIGNED` /
  `STUDY_PATIENT_REASSIGNED`, `PATIENT_CREATED`, `PATIENT_UPDATED`.
- `StudyRepository.updatePatientIfExpected()` hace
  `SET patient_id = ? WHERE case_id = ? AND patient_id IS NOT DISTINCT FROM ?`.

**Frontend**

- `NewAnalysisDrawer.tsx` bloquea la carga hasta que haya `selectedPatient` **y**
  `caseId` válido (`patientReady && caseIdReady`). Etapas reales:
  `idle → processing → completing → associating → opening`.
- `patientStudyAssociation.ts` → `associatePatientAfterAnalysis()` llama
  `PUT /api/studies/{caseId}/patient` con `expectedPatientId: null` y
  `reason: "INITIAL_ASSIGNMENT"`.
- **Matiz importante para la rama de error de la Fig. 10.6:** hay tres resultados:
  `associated`, `conflict` (HTTP 409) y `error`. El botón *reintentar*
  (`retryPatientAssociation()`) sólo aparece en `error`. En `conflict` el mensaje es
  “Requiere revisión manual; no se reasignó automáticamente” — **no se reintenta
  automáticamente**. La corrida ya está persistida en ambos casos y no se repite la
  inferencia. Conviene dibujar la rama con esas dos salidas.
- Rutas: `/worklist`, `/estudio/{caseId}`, `/pacientes`, `/pacientes/{patientId}`
  (detalle de Patient = timeline de Studies).

**AI Module**

- `POST /inputs/study` → `register_study_zip()` (`study_ingestion.py`): extrae el ZIP,
  `classify_study_series()`, registra **todas** las series y marca `analyzable` sólo en
  las elegidas. Slots reales: `sagittal`, `axial`, `sagittal_t1`, `sagittal_t2`
  (T1/T2 sagitales son entradas independientes para P10.7; pueden compartir `inputId`
  con el ganador sagital).
- Extensiones: `POST /v2/series-segmentation/run` (`pfi.full-series-segmentation.v1`) y
  `POST /v2/degenerative-findings/disc-multitask/...` (`pfi.disc-degenerative-findings.v1`).
- El Frontend las consume **siempre vía Backend**: `/api/ai/v2/product/series-segmentation`
  y `/api/ai/v2/product/disc-degenerative-findings` (`productAnalysisApi.ts`).
  Frontera pública `Frontend → Backend → AI Module` confirmada.

### Discrepancias prompt ↔ código (documentar en el informe final)

1. Nombres físicos: `domain_patients` / `domain_studies`, no `patient` / `estudio`.
2. `patient_reference` es único por **índice funcional normalizado**, no por `UNIQUE`.
3. **No existe tabla `rol` ni `usuario_rol`.** Los roles son una columna de texto
   separada por comas en `doctor_accounts.roles`. La fila de la tabla del capítulo
   (“tabla intermedia muchos a muchos”) está desactualizada, pero el prompt pide
   conservar esa fila → se conservó y se deja constancia acá.
4. **No hay tabla de mediciones.** Las mediciones automáticas viven en
   `domain_study_runs.metrics_snapshot` (JSONB); las del revisor en
   `domain_reviewer_annotations`; las correcciones en `domain_review_corrections`.
5. `MODELO / ARTIFACT` no es una tabla de la base: es el registro de artifacts
   (manifest + hash) fuera de PostgreSQL. Se dibujó punteado como referencia lógica.
6. El “catálogo de cortes (P10.5)” corresponde a `domain_input_resources`.

---

## 2. Entorno LaTeX (RESUELTO — importante)

El sandbox traía TeX Live 2021 **incompleto**. Se dejó funcionando así (todo fuera
del repo, en `$TEXMFHOME` y `/tmp`, nada versionado):

- `texlive-bibtex-extra` + `texlive-lang-spanish` (biblatex, logreq, biblatex-iso690,
  spanish.ldf) extraídos de los `.deb` de Ubuntu jammy → `$TEXMFHOME`.
- `biber` 2.17 + dependencias Perl extraídos a `/tmp/debs/broot`, wrapper en
  `/tmp/biber.sh`.
- `quiver.sty` desde GitHub (`varkor/quiver`, commit `792731a`, previo a la dependencia
  de `tikz-nfold`, que no existe en TL2021). `quiver` no se usa en el documento.

**Compilación base verificada antes de tocar nada:**

```
latexmk -pdf -interaction=nonstopmode -e '$biber=q{/tmp/biber.sh %O %S}' main.tex
→ 0 errores, 172 páginas (idéntico al main.pdf versionado)
```

Páginas de las figuras en el build base: **10.4 → p. 82, 10.5 → p. 84, 10.6 → p. 86.**

---

## 3. Figuras

Se descartó Graphviz (cruces y solapamientos inaceptables) y se armó un generador
propio con posiciones explícitas:

- `diagrams/architecture/pfi_diagram.py` — primitivas SVG (cajas tabulares, pata de
  gallo, dependencias punteadas) + `check_layout()` que **verifica solapamientos,
  desbordes de texto y salidas de lienzo** en cada render.
- `diagrams/architecture/fig_10_04_modelo_datos.py` → **HECHA** (3600×2208 px).
  Sin `SUBJECT`; `PATIENT 1 → 0..* STUDY` en verde con `ON DELETE RESTRICT`;
  `subject_ref` como atributo opcional anotado; sin caption dentro del bitmap.
- `diagrams/architecture/fig_10_05_clases_dominio.py` → **HECHA** (3552×2376 px),
  recién regenerada con el corredor de aristas corregido. **Falta la revisión visual
  final de esta última versión.**
- `fig_10_06_flujo_end_to_end.py` → **NO EMPEZADA.**

### Restricción de tamaño que hay que respetar (calculada)

A `0.92\textwidth` (≈15 cm) el texto del bitmap debe ser ≈1 % del ancho del lienzo
para quedar legible en A4 (la figura actual del repo está en 1,16 %). Por eso los
lienzos son de ~1500 unidades de ancho con fuente 15–16, y **no** de 2500–3000.
Si se agrega contenido hay que quitar filas, no agrandar el lienzo.

---

## 4. Lo que FALTA (en orden)

1. **Revisar visualmente** el `fig_10_05_clases_dominio.png` recién generado.
2. **Crear `fig_10_06_flujo_end_to_end.py`** — flujo apaisado por lanes/columnas:
   `AUTENTICACIÓN → SELECCIONAR/CREAR PATIENT → DATOS DEL STUDY → CARGA ZIP DICOM →
   BACKEND (validación+autorización) → AI MODULE (ingesta+clasificación) → INPUTS
   (Sag T1 / Sag T2 / Axial) → CORRIDA/INFERENCIA → {full-series, P10.7} → BACKEND
   (validación+normalización) → POSTGRESQL/ASSETS → ASOCIAR STUDY→PATIENT →
   WORKSPACE/REVISIÓN → REAPERTURA/HISTORIAL`, con la rama de error de asociación
   (usar los tres estados reales del Frontend: `associated` / `error` → reintentar /
   `conflict` → revisión manual) y sin ninguna flecha Frontend↔AI Module directa.
3. **Editar `chapters/capitulo_10_diseno_arquitectura.tex`** (nada de esto está hecho
   todavía; el archivo está intacto):
   - línea 156 y 158 → los dos párrafos nuevos de 10.4.2 (punto 5 del prompt).
   - línea 189 → borrar la fila `sujeto`, agregar fila `patient`.
   - línea 190 → reemplazar la fila `estudio` por `estudio (Study)`.
   - línea 205 → reemplazar el bullet “Un sujeto agrupa…” y agregar el bullet de
     asociación explícita/auditable.
   - línea 236 → primer párrafo nuevo de 10.5.1 (punto 10 del prompt).
   - línea 242 → “…desde la autenticación y la selección del Patient hasta la
     persistencia, asociación del Study y revisión profesional.”
   - línea 219 → subir `0.72\textwidth` a ~`0.94\textwidth` en la Figura 10.5.
   - Conservar `\ref{fig:arch-modelo-datos}`, `\ref{fig:arch-clases-dominio}`,
     `\ref{fig:arch-flujo-end-to-end}` y los tres captions actuales.
4. **Compilar y verificar** (mismo comando de arriba), revisar las páginas 82/84/86.
5. **Restaurar los auxiliares** antes del commit: `main.aux`, `main.log`, `main.toc`,
   `main.bcf`, `main.lof`, `main.lot`, `main.out`, `main.run.xml`, `main.bbl` están
   versionados y el prompt pide dejarlos como estaban; **sí** se actualiza `main.pdf`.
6. **Commit + push** a `master`: `docs: update Patient architecture diagrams and chapter 10`.

---

## 5. Estado del working tree ahora mismo

```
 M images/architecture/fig_10_04_modelo_datos.png
 M images/architecture/fig_10_05_clases_dominio.png
?? diagrams/
```

Nada más fue tocado. `chapters/`, `main.pdf`, los auxiliares, las Figuras
10.1/10.2/10.3/10.7/10.8/10.9, el Capítulo 11 y los tres repos funcionales están
**intactos**.
