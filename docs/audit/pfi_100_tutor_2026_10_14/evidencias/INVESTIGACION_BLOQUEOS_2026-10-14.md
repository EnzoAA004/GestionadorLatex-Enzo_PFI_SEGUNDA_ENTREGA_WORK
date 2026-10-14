# Investigación documental de bloqueos

Fecha de corte: 2026-10-14. Los repositorios de integración se inspeccionaron en modo lectura; no se alteraron ni sincronizaron.

## Evidencia encontrada

- **H04:** `PFI_MVPTest_Enzo_AImodule_final_integration/models/final/axial_t2_alkafri_final_v2_candidate.pt.modelcard.md` contiene Dice e IoU de validación y prueba por clase, con 102 casos de prueba; el gate macro foreground figura como no aprobado (0,679348). El model card sagital `models/final/sagittal_spider_multiclass_final_best.pt.modelcard.md` da métricas agregadas, no un desglose Dice por cada clase. No se reentrenó ni se recalcularon métricas.
- **H11:** se conserva H11-A y se agregó H11-B mediante el reporte anonimizado de Colab: 610/610 imágenes y máscaras resolubles; 1.162 archivos hash sin error; cero grupos repetidos de imágenes/pares entre splits; 55 grupos de máscaras idénticas (113 filas) dentro del mismo split y paciente. No se repitió la auditoría del CSV E9. Test reutilizado, split histórico y correspondencia semántica siguen siendo límites.
- **H12:** ambos model cards/manifests informan IoU agregada; axial test: 0,569973 macro foreground y 0,691540 excluyendo raw_0; sagital test: 0,807998 macro no-background. No se encontró HD95 ni NSD reportado en esos artifacts.
- **H14/H45/H66:** `appendices/anexo_d_entrevistas.tex` contiene transcripciones documentales. Una transcripción no acredita la existencia del audio original ni fecha, consentimiento o autorización de publicación.
- **H31:** están las imágenes `images/user_research/fig_08_01_encuesta_p3.png`, `fig_08_01_encuesta_p1.png`, `fig_08_02_encuesta_p9.png`, `fig_08_02_encuesta_p7.png`, `fig_08_03_encuesta_p12_p13.png` y `fig_08_03_encuesta_p11.png`. No se localizó el archivo fuente de respuestas ni la exportación del formulario.
- **H56:** las fuentes primarias consultadas dicen que SPIDER y Mendeley Data V2 para Sudirman/Al-Kafri están publicados bajo CC BY 4.0. La ficha RSNA registra el RSNA MIRA Dataset Research Use Agreement y el artículo del dataset dice que se ofrece para uso no comercial. No pude abrir el texto íntegro del acuerdo RSNA desde esta sesión; tampoco están en el snapshot las condiciones específicas de licencia/redistribución de los checkpoints y pesos.
- **H63:** se localizaron notebooks, procesamientos de máscaras y manifests. El manifest axial `artifacts/post_e50/absolute_level_anchor/post_e50_67B_split_manifest.json` declara listas opacas vacías y test interno bloqueado; no identifica pacientes. No se localizó paquete fuente de máscaras/etiquetas con procedencia, protocolo, autoría y conteos trazables.

## Archivos externos que faltan

| ID | Aportar |
|---|---|
| H04 | Para el modelo sagital: archivo JSON/CSV de métricas Dice/IoU por clase del split de prueba asociado al checkpoint final, con mapping de clases y manifest/hash del split. El snapshot solo contiene las métricas macro en `models/final/sagittal_spider_multiclass_final_best.pt.modelcard.md` y su manifest. |
| H12 | Si se mantiene HD95/NSD como criterio o resultado esperado: reporte de evaluación fuente con dichos valores, vinculado a checkpoint, split y unidad de agregación. Si nunca se calcularon, basta con mantenerlos explícitamente como no calculados y no se requiere archivo adicional. |
| H14 | Audios originales de las sesiones citadas, registro fechado de cada sesión y consentimientos/autorizaciones de uso y publicación aplicables. |
| H31 | Exportación original de respuestas (CSV/XLSX del formulario) y versión exacta del cuestionario aplicado, con fechas/campos necesarios para verificar denominadores. |
| H45 | Audio fuente de las entrevistas cuya atribución cuestiona el hallazgo y registro fechado que permita cotejarlo; consentimiento/autorización aplicable. |
| H56 | Copia accesible del RSNA MIRA Dataset Research Use Agreement (la ficha oficial identifica el documento, pero su Google Doc no fue accesible aquí) y licencia/condiciones de los checkpoints y pesos, incluida redistribución. No falta corroborar que las páginas oficiales consultadas listan CC BY 4.0 para SPIDER y Mendeley V2. |
| H63 | Paquete original de máscaras/etiquetas de cada modelo, manifest que las vincule con estudios/pacientes y registro/protocolo de etiquetado con autoría y conteos. |
| H66 | Audios originales, registro fechado de las sesiones y consentimientos/autorizaciones para publicar perfiles o atribuciones ampliadas. |

La falta se refiere a evidencia no localizada en los snapshots inspeccionados; no afirma que esos archivos no existan fuera de ellos. H14/H45/H66 continúan bloqueados mientras no se aporte la evidencia correspondiente.

## Fuentes primarias consultadas para H56

- SPIDER, página oficial de datos: https://spider.grand-challenge.org/data/ (indica CC BY 4.0).
- Mendeley Data, dataset Lumbar Spine MRI, versión 2: https://data.mendeley.com/datasets/k57fr854j2/2 (indica CC BY 4.0).
- RSNA ATLAS, ficha oficial LumbarDISC: https://atlas.rsna.org/cards/b9ab56b8-10c1-4104-bca1-a57802f1ba08 (identifica la licencia como RSNA MIRA Dataset Research Use Agreement y enlaza su documento).
- Richards et al., publicación oficial del dataset: https://pubs.rsna.org/doi/10.1148/ryai.250480 (declara que el dataset está disponible para uso no comercial).

La evidencia permite sostener esas condiciones expresas de las fuentes y mantener fuera del escenario comercial el modelo/uso basado en LumbarDISC mientras no exista autorización suficiente. No determina por sí sola los derechos de redistribución o uso comercial de pesos derivados; H56 permanece bloqueado parcialmente.

## Conciliaciones adicionales

- **H03:** las entidades y relaciones de `images/architecture/fig_10_04_modelo_datos.png` se contrastaron con `docs/postgres_schema.sql` y migraciones del snapshot Backend; los nombres de clases/controladores de `images/architecture/fig_10_05_clases_dominio.png` se localizaron en el código Backend. Ambas figuras son consistentes con ese snapshot. La topología `images/architecture/fig_10_07_despliegue_google_cloud.png` se rotula como DEV/E2E observado el 13-10-2026 y coincide en nombres, CPU/memoria y bucket de artifacts con la configuración/evidencia Cloud documentada en LaTeX. Sin embargo, el Terraform inspeccionado es una etapa declarativa posterior: `enable_cloud_sql=false` y `enable_ai_service=false` por defecto, aunque documenta Cloud SQL preexistente y el servicio AI preexistente como recursos externos/no administrados por esa etapa. Por lo tanto, la figura sirve como topología observada fechada, no como inventario de recursos que ese Terraform crea; mantener esa delimitación visible y no presentar los tres snapshots de integración como HEAD remoto final.
- **H13:** el capítulo 15 identifica como fuente de cifras `financial/MIRA_L_Modelo_Financiero_36M_Reconciliado_2026_con_payback_dinamico.xlsx` y delimita `financial/PFI_RM_LUMBAR_FINANCIAL_MODEL_36M.xlsx` como histórico no canónico. El DOCX Francisco usa el nombre `PFI_RM_LUMBAR_FINAL`, distinto de ambos archivos presentes. No se importaron sus cifras ni supuestos: la fuente LaTeX canónica permanece identificada en el propio capítulo y el libro histórico se conserva sin cambios. SHA-256 del reconciliado: `91449d1733c391f4c56056de09a1105daf00c8568013b9adcdf1908328da81c7`; del histórico: `f1c8775a757dc7efcd40c03bd5a3fcc4b585bb7f35dd5909270efa0aed6b4444`.
