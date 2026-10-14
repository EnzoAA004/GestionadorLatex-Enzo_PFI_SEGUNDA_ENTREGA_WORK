# H11-B · Evidencia de contenido de imágenes y máscaras (Colab)

- Dictamen: **SIN_DUPLICADOS_DE_IMAGEN_ENTRE_SPLITS_POR_CONTENIDO**
- CSV E9 SHA coincide con manifest: **True**
- Archivos únicos leídos/hashiados: **1162 / 1162**
- Filas no resueltas: **0**; errores de lectura: **0**
- Rutas de máscaras usadas por varias imágenes: **55**
- Rutas de máscaras usadas por pacientes distintos: **0**
- Grupos de imágenes idénticas entre splits: **0**
- Grupos de pares imagen-máscara idénticos entre splits: **0**
- Grupos de máscaras idénticas entre splits: **0**

## Lectura técnica
Se completó el análisis de hashes de los archivos referenciados por E9.
La repetición de máscaras requiere explicar la relación imagen–máscara; si algunas se comparten por diseño, documentar la justificación con evidencia de origen.

## Límites que siguen vigentes
- La igualdad SHA-256 confirma contenido idéntico, no alineación anatómica correcta ni correspondencia semántica de etiquetas.
- La repetición de máscaras de contenido (por ejemplo máscaras vacías) NO demuestra leakage por sí sola.
- El control de contenidos no reemplaza auditoría de metadatos de paciente, series o geometría de imágenes.
- Los conteos de estudios no son independientes si se usa case_id_norm para estudio y paciente.
- El test axial E9 se usó previamente en axial-full-v1; no es evidencia de test histórico completamente virgen.
- Este notebook no realiza inferencia, entrenamiento, evaluación clínica, ni actualiza metrics/manifest.

## Instrucciones para Codex
- Guardar este informe como evidencia derivada junto con la auditoría H11-A sin copiar rutas ni IDs de pacientes.
- Comprobar el CSV y el snapshot original antes de modificar tablas de tesis.
- Si aparece contenido idéntico entre splits, investigar la procedencia y NO declarar ausencia de leakage.
- NO reinterpretar el test reutilizado como evaluación final externa e independiente.
- No ejecutar entrenamiento, no alterar el baseline axial, las métricas ni los gates para corregir este hallazgo.
