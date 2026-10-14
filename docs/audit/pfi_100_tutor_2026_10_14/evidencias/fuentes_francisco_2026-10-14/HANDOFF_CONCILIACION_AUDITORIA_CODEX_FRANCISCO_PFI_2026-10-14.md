# Handoff de conciliación: auditoría Codex vs. entrega de Francisco

**Fecha:** 14/10/2026  
**Modalidad:** lectura y diagnóstico únicamente; no se modificaron repositorios, Google Docs, el Word ni los Excel fuente.  
**Alcance:** archivos aportados: `MATRIZ_SEGUIMIENTO_AUDITORIA_PFI_100_2026.xlsx`, `Hallazgos_PFI_revision_estado.xlsx`, `PFI_Tercera_entrega_corregida.docx` y `main.pdf`.

## 1. Decisión de gobierno documental

1. Mantener como **fuente editable de la tesis** el trabajo de LaTeX en el worktree/branch local de auditoría. Preservar el checkpoint que produjo el `main.pdf` de 232 páginas; **no reemplazar en bloque** `.tex` con el DOCX paralelo.
2. Mantener como **registro maestro de auditoría** la matriz `MATRIZ_SEGUIMIENTO_AUDITORIA_PFI_100_2026.xlsx`, con sus campos de evidencia, commit, QA y revisión final.
3. Tratar `PFI_Tercera_entrega_corregida.docx` y `Hallazgos_PFI_revision_estado.xlsx` como **fuentes secundarias de propuestas editoriales** que requieren contraste por ID. Preservar sus originales intactos en el expediente para trazabilidad, anotando autoría y fecha.
4. No cerrar un hallazgo por coincidencia de redacción: exigir evidencia concreta, trazabilidad y QA. No divulgar ni hacer merge/push sin autorización.

## 2. Estados originales de las planillas

| Fuente | Estado reportado |
|---|---|
| Matriz Codex (67 IDs) | 19 `Corrección aplicada`; 3 `Cerrado con evidencia`; 37 `Confirmado`; 2 `En investigación`; 6 `Bloqueado por evidencia` |
| Excel Francisco (67 IDs) | 45 `Corregido`; 20 `Parcial`; 2 `Pendiente` |

**Advertencia:** no son taxonomías equivalentes. `Corregido` en Francisco refleja el estado de su propia edición del Word; no prueba integración al LaTeX ni cierre con evidencia experimental. No sustituir estados en bloque.

## 3. Diferencias y decisiones por hallazgo

| ID | Diagnóstico de conciliación | Acción recomendada |
|---|---|---|
| H01 | El Word tiene portada propuesta con `[COMPLETAR: legajo]` y título pendiente de confirmar; el PDF LaTeX ya contiene portada con legajos, resumen y abstract. | Mantener portada LaTeX; incorporar solo aportes editoriales contrastados; no reintroducir placeholders. |
| H02 | Ambas líneas contemplan capítulo 16 de conclusiones; el Word contiene el capítulo en el cuerpo, aunque su índice textual copiado aún pasa de 15 a anexos. | Mantener capítulo final LaTeX y verificar numeración/índice; comparar mejoras de discusión de Francisco sin duplicarlas. |
| H03 | Codex reporta figuras activas y las hemos visto en el PDF; Francisco dice que dibujó diagramas. | Validar DER/clases/Cloud contra implementación congelada antes de decidir qué imagen o figura es autoritativa. |
| H04 | Word clarifica 5 clases de primer plano = `raw_0` + cuatro estructuras; fuente del módulo axial registra `background_250` como fondo excluido del Dice macro foreground. LaTeX mantiene Dice oficial 0,6793, análisis sin raw_0 0,8106. | Conservar criterio exacto de seis clases totales y cinco de primer plano, las métricas originales y el gate FAIL. Auditar métricas sagitales por clase antes de dar cierre. Evitar decir que el macro oficial `incluye background_250`. |
| H07/H09 | Hay avances sobre E2E y dominio Patient en ambas fuentes, pero pueden usar baselines distintos. | Preferir evidencia del código/snapshots probados, y mantener distinción API/persistencia vs UI parcial, y mocks/sintéticos vs reales. |
| H11 | La edición Word todavía contiene `[COMPLETAR: pacientes y cortes de entrenamiento]` y la frase de que faltan los conteos; LaTeX incorpora 427/81/102 registros, 128/27/29 pacientes, SHA y limitación de test reutilizado. | **No importar la versión de H11 del Word**. Agregar evidencia Colab H11-B: 610/610 rutas exactas; hashes 1162/1162 sin errores; 0 duplicados por contenido de imágenes y pares; 55 grupos de máscaras idénticas, 113 filas afectadas, sin cruces de pacientes/splits. H11 no se convierte en test independiente. |
| H12 | Word agrega columna IoU y deja HD95/NSD como no calculadas; Codex las conserva como bloqueo de evidencia. | Revisar si información realmente medida existe; no fabricar métricas de superficie. |
| H13 | Word agrega supuestos y habla de hoja financiera `PFI_RM_LUMBAR_FINAL`; Codex confrontó un libro reconciliado de 36 meses. | Usar una única fuente canónica de cifras financieras, acordada por ambos, con versión/hash. Verificar tablas y VAN/TIR antes de importar supuestos. |
| H14/H45/H66 | Word formula afirmaciones de consentimiento verbal con marcadores de confirmación; Codex mantiene bloqueos por falta de audios, fechas y constancias. | No convertir una nota `[COMPLETAR]` en una afirmación factual. Buscar soportes originales o reformular con precisión sobre lo documentado. |
| H31 | Word propone anexo de encuesta y pide respuestas/frecuencias; Codex no encontró exportación original. | Reconciliar 167 respuestas con la fuente primaria si está disponible, sin inferir n por ítem. |
| H56 | Word propone anexo J con licencias y restricciones; Codex solicita fuentes originales. | Aprovechar la estructura del anexo como propuesta, pero corroborar textos originales y compatibilidad comercial separadamente. |
| H63 | Word menciona procedencia de máscaras, pero no consta que anexara los archivos de anotación, correspondencia o protocolo fuente. | Mantener bloqueo hasta contrastar evidencias reales. |

## 4. Errores visibles en el PDF LaTeX aportado (232 páginas físicas)

Se confirmaron directamente por extracción de texto **y renderizado de la página**:

- **Página física 35 (numeración impresa: 33), Tabla 6.2:** aparece literalmente `hline ScanDiags` como nombre de solución. Es un defecto de fuente/composición y debe corregirse en LaTeX y recompilar.
- **Página física 15 (numeración impresa: 13), Lista de Figuras:** se repite `11.4` para la imagen de workspace axial y el panel de mediciones; la lista también muestra secuencia de numeración anómala para controles y preinforme. Revisar `\caption`, `\addcontentsline` manuales y secuencia completa del capítulo 11; corregir la **causa**, no solo el índice.
- **Páginas físicas 11 y 134:** título `Validación profesional final pendiente`; verificar si es un subtítulo histórico justificado o una caracterización desactualizada del documento final. No cambiar validaciones efectivamente no realizadas por declaraciones de ejecución.

**Nota:** la compilación sin referencias indefinidas no garantiza ausencia de errores de contenido o formato en tablas/índices. Las 232 páginas corresponden al PDF adjuntado; no implica que su fuente local contenga exactamente todos los commits de Codex, que todavía se deben conciliar por SHA.

## 5. Diferencias de producto/documentación

- El DOCX de Francisco contiene **43 apariciones literales de `[COMPLETAR:`**, entre texto, tablas y bibliografía; no está listo para entrega ni para importación como documento definitivo.
- El DOCX tiene nuevas secciones/anexos I, J y K, bibliografía ampliada y nuevas afirmaciones sobre competencia/mediciones. Son posibles aportes, no hechos automáticamente comprobados. Deben pasar control de fuente y correspondencia con LaTeX.
- El documento LaTeX del PDF es más actualizado en H11; en cambio el DOCX propone matices y tablas que pueden valer la pena incorporar una vez contrastados. No igualar páginas, índices o números de tabla por simple reemplazo.
- Mantener preservadas las métricas oficiales, el alcance académico, la delimitación cualitativa vs clínica, y las diferencias Cloud V1/V2.

## 6. Instrucciones propuestas para Codex

> Continuá **solo en el worktree local de auditoría del Gestionador LaTeX**. Archivá sin editar `PFI_Tercera_entrega_corregida.docx` y `Hallazgos_PFI_revision_estado.xlsx` como fuentes de revisión aportadas por Francisco, identificando procedencia y hash. No copies capítulos completos del Word al LaTeX ni sobrescribas la matriz maestra. Compará las 67 filas de la planilla de Francisco contra `MATRIZ_SEGUIMIENTO_AUDITORIA_PFI_100_2026.xlsx` por ID y generá una tabla diferencial con `ya resuelto / aporte aprovechable / contradicción / falta de evidencia`, citando rutas, commits y QA. Corregí primero el literal `hline ScanDiags` de la Tabla 6.2 y la numeración repetida de la Lista de Figuras del capítulo 11 que aparecen en el PDF físico páginas 35 y 15 respectivamente. Para H11 conservar los conteos E9 427/81/102, pacientes 128/27/29 y la limitación de test reutilizado; incorporar la nueva evidencia H11-B de hashes de contenido (1162 archivos, 0 hashes fallidos, 0 imágenes duplicadas, 55 grupos de máscaras repetidas dentro del paciente y split), sin interpretar la repetición como garantía de correcto alineamiento anatómico. No afirmar la independencia del test ni promover el artifact axial. Verificá el historial de H13 contra el Excel financiero canónico y los anexos/licencias de H56 contra las fuentes primarias. No importar las 43 notas `[COMPLETAR]` del Word. Tras cada cambio, realizá compilación pdfLaTeX/Biber, control de referencias, inspección visual de tablas e índice, `git diff --check`, y anotá el commit de manera local. No hagas push, merge, rebase, ni modifiques Google Docs o los snapshots de frontend/backend/AI sin permiso. Al finalizar, entregá matriz de conciliación y lista de bloqueos con evidencia requerida.

## 7. Estado de la auditoría

**Abierta.** El avance de Francisco no sustituye el registro de QA local de Codex; la matriz de Codex sigue siendo el instrumento de seguimiento hasta conciliación y cierre formal.
