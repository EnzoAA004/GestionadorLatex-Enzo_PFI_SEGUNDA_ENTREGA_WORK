# Investigación documental de bloqueos

Fecha de corte: 2026-10-14. Los repositorios de integración se inspeccionaron en modo lectura; no se alteraron ni sincronizaron.

## Evidencia encontrada

- **H04:** `PFI_MVPTest_Enzo_AImodule_final_integration/models/final/axial_t2_alkafri_final_v2_candidate.pt.modelcard.md` contiene Dice e IoU de validación y prueba por clase, con 102 casos de prueba; el gate macro foreground figura como no aprobado (0,679348). El model card sagital `models/final/sagittal_spider_multiclass_final_best.pt.modelcard.md` da métricas agregadas, no un desglose Dice por cada clase. No se reentrenó ni se recalcularon métricas.
- **H11:** se conserva y reutiliza `H11_HANDOFF_RESULTADO_COLAB_AXIAL_E9_2026-10-14.md` y los informes anonimizados ya incorporados. No se repitió la auditoría del CSV E9.
- **H12:** ambos model cards/manifests informan IoU agregada; axial test: 0,569973 macro foreground y 0,691540 excluyendo raw_0; sagital test: 0,807998 macro no-background. No se encontró HD95 ni NSD reportado en esos artifacts.
- **H14/H45/H66:** `appendices/anexo_d_entrevistas.tex` contiene transcripciones documentales. Una transcripción no acredita la existencia del audio original ni fecha, consentimiento o autorización de publicación.
- **H31:** están las imágenes `images/user_research/fig_08_01_encuesta_p3.png`, `fig_08_01_encuesta_p1.png`, `fig_08_02_encuesta_p9.png`, `fig_08_02_encuesta_p7.png`, `fig_08_03_encuesta_p12_p13.png` y `fig_08_03_encuesta_p11.png`. No se localizó el archivo fuente de respuestas ni la exportación del formulario.
- **H56:** model cards/manifests identifican SPIDER y RSNA/LumbarDISC, además de hashes de artifacts. No se localizó dentro del snapshot un documento de licencia/terms aplicable a los datasets, pesos o checkpoints que acredite redistribución o uso comercial.
- **H63:** se localizaron notebooks, procesamientos de máscaras y manifests. El manifest axial `artifacts/post_e50/absolute_level_anchor/post_e50_67B_split_manifest.json` declara listas opacas vacías y test interno bloqueado; no identifica pacientes. No se localizó paquete fuente de máscaras/etiquetas con procedencia, protocolo, autoría y conteos trazables.

## Archivos externos que faltan

| ID | Aportar |
|---|---|
| H14 | Audios originales de las sesiones citadas, registro fechado de cada sesión y consentimientos/autorizaciones de uso y publicación aplicables. |
| H31 | Exportación original de respuestas (CSV/XLSX del formulario) y versión exacta del cuestionario aplicado, con fechas/campos necesarios para verificar denominadores. |
| H45 | Audio fuente de las entrevistas cuya atribución cuestiona el hallazgo y registro fechado que permita cotejarlo; consentimiento/autorización aplicable. |
| H56 | Texto/URL archivada o copia de los términos de uso/licencias de SPIDER, RSNA y LumbarDISC, más las condiciones/autorizaciones de los checkpoints y pesos sobre redistribución y uso comercial. |
| H63 | Paquete original de máscaras/etiquetas de cada modelo, manifest que las vincule con estudios/pacientes y registro/protocolo de etiquetado con autoría y conteos. |
| H66 | Audios originales, registro fechado de las sesiones y consentimientos/autorizaciones para publicar perfiles o atribuciones ampliadas. |

La falta se refiere a evidencia no localizada en los snapshots inspeccionados; no afirma que esos archivos no existan fuera de ellos. H14/H45/H66 continúan bloqueados mientras no se aporte la evidencia correspondiente.
