# FINAL_THESIS_LATEX_UPDATE_PLAN

Estado: auditoria documental, sin editar capitulos LaTeX.

Fuente tecnica canonica comparada:
- Backend `main` `33081f7cc3702afe4db04a2b63de4762408b5d50`
- Frontend `main` `ff191e1195a4e6bf06312ae8e266d37894c5b7b1`
- AI module `main` `22b12e04ce37f5c9ba6a02f356ac2022390bf06e`
- Documento canonico: `C:/Users/enzoa/Documents/GitHub/PFI_MVPTest_Enzo_Backend/docs/final/FINAL_PRODUCT_TECHNICAL_SOURCE_OF_TRUTH.md`

## 1. Estructura actual del repo

Archivo principal:
- `main.tex`

Includes activos en `main.tex`:
- Frontmatter: `chapters/title.tex`, `chapters/acknowledgments.tex`
- Comentados: `chapters/summary.tex`, `chapters/abstract.tex`
- Capitulos vivos: 14 `\input{chapters/...}`
- Anexos vivos: 7 `\input{appendices/...}`
- Bibliografia: `references.bib`
- Configuracion: `config/symbols.tex`, paquetes y formato definidos en `main.tex`

Capitulos vivos:
- `chapters/capitulo_01_introduccion.tex` - Introduccion
- `chapters/capitulo_02_planteamiento_problema.tex` - Planteamiento del problema
- `chapters/capitulo_03_justificacion.tex` - Justificacion
- `chapters/capitulo_04_objetivos.tex` - Objetivos
- `chapters/capitulo_05_alcance.tex` - Alcance
- `chapters/capitulo_06_estado_del_arte.tex` - Estado del arte
- `chapters/capitulo_07_marco_teorico.tex` - Marco teorico
- `chapters/capitulo_08_user_research.tex` - User research
- `chapters/capitulo_09_requerimientos.tex` - Requerimientos
- `chapters/capitulo_10_diseno_arquitectura.tex` - Arquitectura
- `chapters/capitulo_11_capacidades_prototipo.tex` - Capacidades
- `chapters/capitulo_12_metodologia_validacion.tex` - Metodologia y validacion tecnica
- `chapters/capitulo_13_resultados_evaluacion.tex` - Resultados tecnicos
- `chapters/capitulo_14_planificacion_academica.tex` - Planificacion academica

Anexos vivos:
- `appendices/anexo_a_cronograma.tex`
- `appendices/anexo_b_glosario.tex`
- `appendices/anexo_c_anatomia.tex`
- `appendices/anexo_d_entrevistas.tex`
- `appendices/anexo_e_configuracion_entrenamiento.tex`
- `appendices/anexo_f_evolucion_tecnica.tex`
- `appendices/anexo_g_adr.tex`

Archivos legacy no incluidos por `main.tex` y no deben editarse como fuente viva salvo decision explicita:
- `chapters/capitulo_06_descripcion_solucion.tex`
- `chapters/capitulo_07_estado_del_arte.tex`
- `chapters/capitulo_08_marco_teorico.tex`
- `chapters/capitulo_09_planificacion_proyecto.tex`
- `appendices/anexo_a_glosario_tecnico.tex`
- `appendices/anexo_b_figuras_anatomicas.tex`
- `appendices/anexo_c_modulo_axial_preliminar.tex`
- `migration_reference/**`
- `UADE_PFI_Template-develop/**`

Recursos:
- Imagenes activas: `images/architecture/*`, `images/anatomy/*`, `images/user_research/*`, `images/methodology/*`, `images/UADE*.png`
- Diagramas fuente: `diagrams/architecture/*.py`, `diagrams/methodology/*`
- Figuras pendientes: varias figuras 10.x y 11.x estan como `FIGURE_PENDING_MIGRATION` y solo se agregan a LOF, sin imagen real insertada.
- Tablas: mayormente inline en los `.tex`, no hay carpeta `tables/` activa.
- Artefactos de build presentes: `main.pdf`, `main.aux`, `main.log`, `main.toc`, etc.

Ubicacion tematica actual:
- Introduccion: capitulo 1
- Estado del arte: capitulo 6
- Marco teorico: capitulo 7
- Metodologia: capitulo 12
- Arquitectura: capitulo 10
- Desarrollo/capacidades: capitulo 11 y anexo F
- IA/modelos: capitulos 11/13 y anexos E/F
- Resultados: capitulo 13
- Validacion: capitulos 12/13 y pendiente profesional en capitulos 5/11/13
- Cloud: capitulo 10 y anexo G
- Negocio: no existe capitulo o seccion final suficiente
- Conclusiones: no existe capitulo final

## 2. Secciones correctas a conservar

- Capitulo 1: mantiene bien el no diagnostico, datasets publicos y alcance academico. Requiere expansion, no reemplazo.
- Capitulo 5: distingue validacion tecnica vs revision profesional pendiente. Requiere actualizar longitudinal y estado final de producto.
- Capitulo 6: el estado del arte esta amplio y contiene FODA/Porter. Requiere limpieza editorial y expansion hacia features finales, no borrado.
- Capitulo 7: marco teorico robusto para RM, segmentacion, metricas, human-in-the-loop y privacidad. Mantener.
- Capitulo 8 y Anexo D: entrevistas y encuesta estan documentadas; faltan incorporar validaciones profesionales finales si existen.
- Capitulo 13: presenta correctamente que axial no supera quality gate y que no hay validacion clinica. Debe expandirse con evidencia de producto final.
- Anexo E: configuracion de entrenamiento util. Debe sincronizar metricas exactas y estados.

## 3. Secciones desactualizadas

| LATEX FILE | SECTION | CURRENT CLAIM | FINAL TECHNICAL TRUTH | ACTION |
|---|---|---|---|---|
| `chapters/capitulo_10_diseno_arquitectura.tex` | 10.3.2 Modelo de datos | Patient es identidad longitudinal principal; `subjectRef` no se utiliza como identidad longitudinal principal. | Backend tiene Patient entity/API/`Study.patientId`/persistencia, pero Frontend real todavia opera el flujo historial/longitudinal con `subjectRef` y consume `/api/subjects`, no `/api/patients`. Patient = `IMPLEMENTED_PARTIAL`. | UPDATE |
| `chapters/capitulo_10_diseno_arquitectura.tex` | 10.4.1 Flujo end-to-end | El recorrido comienza con seleccion/creacion de Patient y mantiene asociacion explicita Study-Patient. | Browser final no crea/selecciona persisted Patient; Patient smoke 8/8 fue Backend/API-level. | UPDATE |
| `chapters/capitulo_11_capacidades_prototipo.tex` | 11.2 Ingesta | Profesional selecciona/crea Patient antes del analisis. | Limitacion UI: flujo real shipped continua basado en `subjectRef`; la creacion/seleccion Patient no esta validada browser-level. | UPDATE |
| `chapters/capitulo_11_capacidades_prototipo.tex` | 11.7 Visualizacion | E2E real pendiente de cierre. | Playwright demo E2E final 11/11 PASS en stack real main; aun distinguir Demo Mode de inferencia real. | UPDATE |
| `chapters/capitulo_11_capacidades_prototipo.tex` | 11.9 Persistencia | Estudios del mismo Patient se vinculan con Patient; `subjectRef` no sustituye. | Backend persistencia Patient validada; UI longitudinal real es `subjectRef`. | UPDATE |
| `chapters/capitulo_11_capacidades_prototipo.tex` | 11.11.1 Hallazgos estructurales | Ninguna de las ocho estimaciones se expone en producto. | Product-analysis existe en demo path; 67B2 offline validado pero runtime parity no probado; P10.7 sigue bloqueado para inferencia automatica real. | UPDATE |
| `chapters/capitulo_11_capacidades_prototipo.tex` | 11.12 Estado consolidado | Recorrido E2E pendiente; comparacion longitudinal futura; despliegue planificado. | Playwright 11/11 PASS; longitudinal implementado y validado en demo/subjectRef; Backend/Frontend DEV Cloud Run desplegados; Cloud completo no. | UPDATE |
| `chapters/capitulo_13_resultados_evaluacion.tex` | Todo el capitulo | Solo resultados de segmentacion y verificacion de mediciones. | Debe incorporar resultados tecnicos finales: backend Java21, frontend lint/typecheck/build/tests, AI focal/regression, Docker stack, Playwright 11/11, Patient API E2E, persistencia, product-analysis demo/blocked real, invalid DICOM 422, secret scan. | EXPAND |
| `chapters/capitulo_13_resultados_evaluacion.tex` | 13.8 Limitaciones | Seis limitaciones centradas en segmentacion/mediciones. | Debe agregar limitaciones finales: 67B2 runtime parity, 67C experimental, P10.7 blocked preprocessing parity, Grad-CAM experimental/no explicit browser E2E, Patient UI partial, Demo Mode non-clinical, asset registry ephemeral P2, Cloud partial, no clinical validation. | EXPAND |
| `chapters/capitulo_14_planificacion_academica.tex` | Planificacion por entregables | P10.7 implementado e integrado; Full Product UI E2E pendiente; comparacion longitudinal fuera del alcance inmediato. | P10.7 automaticInferenceEnabled=false / blocked preprocessing parity; Full Product UI E2E Playwright 11/11 PASS; longitudinal implementado en demo/subjectRef. | UPDATE |
| `appendices/anexo_a_cronograma.tex` | Desvios / calendario | Full Product UI E2E pendiente luego de P10.9. | Actualizar a E2E final validado, con alcance Demo Mode y sin presentar Patient browser-level. | UPDATE |
| `appendices/anexo_f_evolucion_tecnica.tex` | Estado entrega 50 / producto visible | Incorpora Patient como identidad longitudinal y Study mediante patientId; E2E pendiente. | Patient Backend/API implementado parcialmente; Frontend `subjectRef`; Playwright E2E final completado. | UPDATE |
| `appendices/anexo_g_adr.tex` | ADR Cloud | Google Cloud como plataforma objetivo; recursos a crear. | Diferenciar desplegado: Artifact Registry/WIF, Backend Cloud Run DEV, Frontend Cloud Run DEV. No desplegado: AI Cloud Run privado, Cloud SQL, Secret Manager, Storage productivo, DEMO env, monitoring/alerting live. | UPDATE |
| `chapters/capitulo_10_diseno_arquitectura.tex` | 10.6 Vista fisica | Vercel/Railway/tunel como validacion actual; Google Cloud objetivo no implementado. | Reemplazar/actualizar por estado final mixto: Backend/Frontend DEV Cloud Run desplegados y validados; AI/private/DB/secrets/storage/demo/monitoring no. | UPDATE |
| `chapters/capitulo_10_diseno_arquitectura.tex` | 10.6 dimensionamiento | Dice inferencia real P10.7 durante E2E local. | Debe evitar afirmar P10.7 real productivo si la fuente final dice `blocked_preprocessing_parity`, `automaticInferenceEnabled=false`. | UPDATE |
| `chapters/capitulo_07_marco_teorico.tex` | Salida estructurada | Preinforme deterministico, no LLM. | El producto final incluye contextual LLM/chat validado en demo/mock; mantener determinismo del reporte pero agregar diferencia con chat asistivo. | EXPAND |
| `chapters/capitulo_09_requerimientos.tex` | Requerimientos funcionales/no funcionales | Probablemente no incluye todas las extensiones finales. | Agregar/ajustar trazabilidad para longitudinal, report/PDF/JSON, review analytics, concordance, Grad-CAM experimental, Demo Mode, Cloud partial. | EXPAND |

## 4. Claims incorrectos o riesgosos

- Patient como feature browser-level completa: incorrecto. Redaccion final debe ser `IMPLEMENTED_PARTIAL`.
- `subjectRef` como compatibilidad secundaria no usada: incorrecto para Frontend final; sigue siendo identidad real del flujo historial/longitudinal.
- Full Product UI E2E pendiente: obsoleto; Playwright 11/11 PASS, pero recorrido es demo/product path y no Patient entity browser-level.
- P10.7 como inferencia real integrada: riesgoso; debe decir bloqueado por preprocessing parity y automatic inference disabled.
- Cloud como objetivo no implementado por completo: parcialmente obsoleto; DEV Backend/Frontend Cloud Run y Artifact Registry/WIF si estan deployed/validated.
- Cloud completo desplegado: prohibido; no sostenerlo.
- Grad-CAM simplemente no validado: impreciso; tests AI/API/wiring validados, `experimental=true`, no ejercitado explicitamente en browser E2E final.
- Comparacion longitudinal futura: obsoleto; implementada/validada en demo/subjectRef con valores deterministicos.
- Preinforme exclusivamente sin LLM: correcto para reporte, pero falta distinguir chat contextual LLM demo/mock.
- Segmentacion axial como modulo consolidado: evitar; `qualityGatePassed=false`.

## 5. Claims faltantes

Agregar claims finalizados, siempre con alcance:
- Backend final `main` `33081f7cc3702afe4db04a2b63de4762408b5d50`.
- Frontend final `main` `ff191e1195a4e6bf06312ae8e266d37894c5b7b1`.
- AI final `main` `22b12e04ce37f5c9ba6a02f356ac2022390bf06e`.
- Backend Java 21 suite final: 1053/1053, con 78 skipped Postgres-testcontainer-gated.
- Backend focal: 67/67.
- Frontend lint/typecheck/build clean y test scope final segun evidencia.
- AI focal: 67 passed, 1 skipped; AI full suite 479 passed / 40 failed por gaps de entorno preexistentes.
- Docker full stack build PASS.
- Playwright demo E2E 11/11 PASS.
- Patient API E2E 8/8 Backend/API-level.
- Persistencia con restart PASS.
- `product-analysis`: demo path validated; real 67B2 path blocked/no fabricated level.
- Report/PDF/JSON validated, `pfi.study-report.v1`.
- Invalid DICOM -> 422 `UNSUPPORTED_INPUT`.
- Secret scan con findings false positives.
- Concordance EXT-01, Review analytics EXT-02, Feedback curation EXT-05.
- Grad-CAM EXT-03: tests/API/wiring validados; no explicit browser E2E final.
- Demo Mode: synthetic/non-clinical, `status=partial`, no persistent UI indicator.
- AI asset/slice registry ephemeral P2.

## 6. Tablas a actualizar

- `tab:arch-componentes-funcionales`: agregar historia/longitudinal, report/PDF/JSON, concordance/review analytics si se decide llevar a arquitectura.
- `tab:arch-decisiones-requerimientos`: ajustar despliegue controlado y Patient/subjectRef.
- `tab:arch-logica-capas`: Spring Boot debe mencionar Java 21; AI FastAPI sigue servicio interno.
- `tab:arch-entidades-principales`: marcar Patient como implementado en Backend/API, UI parcial; `subjectRef` no relegarlo como meramente opcional en producto final.
- `tab:arch-cloud-dimensionamiento`: revisar claim de P10.7 real y separar medicion local vs Cloud Run DEV.
- `tab:cap-formatos-ingesta`: conservar, agregar invalid DICOM -> 422 si corresponde.
- `tab:cap-estado-capacidades`: actualizar E2E, longitudinal, product-analysis, Grad-CAM, Cloud, Patient partial.
- `tab:res-dice-modelos`: agregar IoU axial exacto y `qualityGatePassed=false`.
- Nueva tabla resultados finales por capa: Backend / Frontend / AI / Docker / Browser / Security.
- Nueva tabla Cloud deployed vs not deployed.
- Nueva tabla modelos IA y estado productivo: Sagittal, Axial, 67B2, 67C, P10.7, Grad-CAM.
- Nueva tabla limitaciones finales.

## 7. Figuras a actualizar o agregar

Figuras actualmente pendientes/marcadores:
- Capitulo 10: figuras 10.8 y 10.9 son placeholders de wireframes sin imagen real.
- Capitulo 11: figuras 11.1 a 11.10 son placeholders agregados al LOF, sin `\includegraphics`.

Figuras nuevas sugeridas:
- Arquitectura Cloud final con badges por estado: deployed DEV vs planned/not deployed.
- Flujo Patient vs subjectRef: Backend Patient API implementado, Frontend subjectRef actual.
- Pipeline de validacion final por capas.
- Matriz de modelos IA: offline validation vs runtime/product availability.
- Capturas reales del Playwright 11/11 si existen artefactos o se generan despues.
- Captura/diagrama de Demo Mode con advertencia non-clinical.

## 8. Nuevas secciones requeridas

Agregar o expandir:
- Capitulo 10: `Estado real de despliegue Cloud`.
- Capitulo 10 o 11: `Identidad longitudinal: Patient API y limitacion subjectRef en UI`.
- Capitulo 11: `Demo Mode y product-analysis`.
- Capitulo 11: `Extensiones de revision: concordance, review analytics, feedback curation`.
- Capitulo 11: `Grad-CAM experimental`.
- Capitulo 13: `Resultados finales de validacion tecnica por capa`.
- Capitulo 13: `Resultados de integracion Docker y browser E2E`.
- Capitulo 13: `Diferencia entre validacion tecnica y validacion clinica` reforzada.
- Capitulo final nuevo: `Discusion, conclusiones y trabajo futuro`.
- Capitulo o bloque final de negocio: modelo de negocio, costos, pricing, escenarios, VAN/TIR/Payback/break-even, branding.
- Seccion de validacion profesional final: Susana Torres y Claudia Cejas, si esa evidencia existe fuera del repo; no inventar.

## 9. Correcciones pendientes de devolucion 25%

- Parrafos largos en estado del arte: parcialmente corregido. Capitulo 6 sigue siendo extenso y algunas secciones/tablas son densas; requiere pasada editorial, especialmente FODA/Porter y matriz comparativa.
- Redundancia rol profesional: parcialmente corregida. El mensaje human-in-the-loop esta bien, pero se repite en capitulos 5, 7, 8, 10, 11 y 13; conviene centralizar y referenciar.
- Formato URL tabla 7.1: revisar numeracion final. En repo actual el estado del arte activo es capitulo 6; no se encontro una `Tabla 7.1` viva con ese nombre, posible pendiente heredado por renumeracion.
- Metodologia de entrevistas: corregida en capitulo 8 y anexo D; mantener y no reescribir.
- Fila de documentacion de entrevistas en planificacion: verificar/actualizar en `appendices/anexo_a_cronograma.tex` y `chapters/capitulo_14_planificacion_academica.tex`; hay filas de user research, pero falta reflejar validacion profesional final si existe.
- Referencia Natalia para axial antes en el cuerpo: corregida en capitulo 6 y anexo C legacy; en el cuerpo activo aparece Al-Kafri/Sudirman/Natalia en capitulo 6. Mantener control de que no dependa solo de anexo legacy.

## 10. Capitulos nuevos o pendientes para entrega final

Falta incorporar sin inventar contenido:
- Validacion profesional de Susana Torres.
- Validacion profesional de Claudia Cejas.
- Modelo de negocio.
- Costos.
- Pricing.
- Escenarios.
- VAN/TIR/Payback/break-even.
- Branding.
- Arquitectura Cloud final con estado real por recurso.
- Resultados/discusion.
- Conclusiones.
- Trabajo futuro.

## 11. Orden recomendado de edicion

1. Congelar vocabulario de estados y glosario editorial: `IMPLEMENTED_VALIDATED`, `IMPLEMENTED_PARTIAL`, `IMPLEMENTED_EXPERIMENTAL`, `IMPLEMENTED_BLOCKED`, `IMPLEMENTED_DEMO_ONLY`, `DEPLOYED`, `NOT_DEPLOYED`, `PLAN_ONLY`.
2. Actualizar capitulo 10 arquitectura: Java 21, Cloud real, Patient/subjectRef, P10.7 gating, Demo Mode, LLM/chat, storage/assets.
3. Actualizar capitulo 11 capacidades: estado final por feature, Patient partial, longitudinal, report/PDF/JSON, product-analysis, Grad-CAM, concordance, review analytics, feedback curation.
4. Actualizar capitulo 13 resultados: resultados finales por capa, Playwright 11/11, Patient API E2E 8/8 Backend-level, AI metrics, Docker, invalid DICOM, secret scan.
5. Actualizar limitaciones fuertes en capitulo 13 y/o conclusiones: axial gate, 67B2 parity, 67C, P10.7, Grad-CAM, Patient UI partial, Demo Mode, asset registry, Cloud partial, no clinical validation.
6. Actualizar capitulo 14 y anexo A/F para que el estado historico no contradiga el final.
7. Agregar capitulo/sections de negocio y cierre final solo cuando haya insumos externos.
8. Insertar o generar figuras reales para placeholders 10.x/11.x, despues de cerrar texto tecnico.
9. Compilar y resolver referencias cruzadas, LOF/LOT y bibliografia.

## 12. Archivos exactos a tocar en la proxima fase

Alta prioridad:
- `chapters/capitulo_10_diseno_arquitectura.tex`
- `chapters/capitulo_11_capacidades_prototipo.tex`
- `chapters/capitulo_13_resultados_evaluacion.tex`
- `chapters/capitulo_14_planificacion_academica.tex`
- `appendices/anexo_a_cronograma.tex`
- `appendices/anexo_f_evolucion_tecnica.tex`
- `appendices/anexo_g_adr.tex`

Media prioridad:
- `chapters/capitulo_05_alcance.tex`
- `chapters/capitulo_06_estado_del_arte.tex`
- `chapters/capitulo_07_marco_teorico.tex`
- `chapters/capitulo_08_user_research.tex`
- `chapters/capitulo_09_requerimientos.tex`
- `appendices/anexo_b_glosario.tex`
- `appendices/anexo_e_configuracion_entrenamiento.tex`
- `references.bib`

Posibles nuevos archivos:
- `chapters/capitulo_15_modelo_negocio.tex`
- `chapters/capitulo_16_discusion_conclusiones.tex`
- `images/final_validation/*`
- `images/cloud/*`
- `images/product/*`

No tocar como fuente viva salvo limpieza posterior:
- `migration_reference/**`
- `UADE_PFI_Template-develop/**`
- capitulos/anexos legacy no incluidos por `main.tex`

## 13. Redacciones canonicas recomendadas

Patient:
> El dominio Patient esta implementado y validado en Backend/API/persistencia, incluyendo entidad Patient, `/api/patients`, `Study.patientId`, asociacion Patient-Study y persistencia. Sin embargo, el Frontend final conserva el flujo real de historial y longitudinal basado en `subjectRef`; `PatientHistoryPage` y `subjectHistoryApi` consumen `/api/subjects`, no `/api/patients`. Por lo tanto, Patient se clasifica como `IMPLEMENTED_PARTIAL` y no como E2E browser-level completo.

Cloud:
> El estado Cloud es mixto. Estan desplegados y validados Artifact Registry/WIF, Backend Cloud Run DEV y Frontend Cloud Run DEV. No estan desplegados AI Cloud Run privado, Cloud SQL, Secret Manager, storage productivo, DEMO environment ni monitoring/alerting live. La arquitectura completa de Google Cloud debe presentarse como objetivo/plan por componentes, no como entorno completamente desplegado.

67B2:
> 67B2 cuenta con evaluacion offline verificada: DEV top1 0.9343629343629344, top2 0.972972972972973, MRR 0.9617117117117117, n=259; locked validation Top1 0.9049295774647887, Top2 0.9612676056338029, MRR 0.9448356807511736; pipeline accuracy given emit 0.9909502262443439. Esa evidencia no prueba disponibilidad productiva: el runtime conserva `67B2_RUNTIME_PARITY_NOT_PROVEN`, `productEnabled=false` y `parityVerified=false`.

Grad-CAM:
> Grad-CAM esta marcado como experimental. Los tests AI especificos pasan, el contrato API esta validado y existe wiring de Frontend en `ActivationMapPanel.tsx`; no fue ejercitado explicitamente en el recorrido browser E2E final.

Validacion:
> La validacion tecnica demuestra funcionamiento del prototipo bajo condiciones controladas y datasets publicos/de-identificados; no equivale a validacion clinica ni autoriza diagnostico, tratamiento o sustitucion del criterio profesional.
