# H11 — Evidencia Colab de partición axial E9 y handoff para Codex

**Fecha:** 14/10/2026. **Origen:** `informes_axial_E9_anonimizados.zip`, recibido de Colab, con `reporte_axial_E9_anonimizado.json` e `informe_axial_E9_anonimizado.md`.

**Objetivo:** aportar evidencia a la observación #11 de `Hallazgos_PFI_revision.xlsx` sin cambiar cifras, entrenar modelos, reutilizar el test ni modificar ramas publicadas.

## 1. Resultados directamente verificados del ZIP

| Partición | Registros | Identificadores de paciente únicos | Identificadores de estudio únicos reportados | Rutas de imagen únicas | Rutas de máscara únicas |
|---|---:|---:|---:|---:|---:|
| Entrenamiento | 427 | 128 | 128 | 427 | 384 |
| Validación | 81 | 27 | 27 | 81 | 81 |
| Prueba | 102 | 29 | 29 | 102 | 87 |
| **Total** | **610** | **184** (sin intersecciones) | **184** (según identificadores reportados) | **610** | **552** |

- CSV identificado: `E9_t2_final_labels_curated_split.csv`.
- SHA-256 calculado sobre el CSV: `17f78265b93cca59b0680c5fe336943acee78c4fbe34bd86a23df06ce80d051e`.
- SHA-256 registrado en el manifest V2: **idéntico**.
- Filas idénticas duplicadas: **0**.
- Intersecciones de identificadores de pacientes entre train/val/test: **0**.
- Intersecciones de identificadores de estudio entre train/val/test: **0**.
- Intersecciones de rutas de imagen y máscara entre train/val/test: **0**.
- Comparación con la otra partición histórica: **no realizada** (no se entregó segundo CSV).
- Comprobación de existencia/contenido de archivos: **no ejecutada**.

**Precisión sobre “estudios”:** los notebooks 49/50 del AI Module emplean por defecto `case_id_norm` tanto para el identificador de paciente como para el de estudio (`AXIAL_PATIENT_COL` y `AXIAL_STUDY_COL`). Por ello, el conteo de estudios igual al de pacientes **no constituye una verificación independiente de estudios clínicos distintos** hasta inspeccionar las columnas efectivamente utilizadas.

**Hallazgo adicional, no equivalente a fuga:** existen 43 asociaciones más que rutas de máscara distintas en train (427-384) y 15 en test (102-87). Es reutilización de rutas *dentro* de una partición, no un solapamiento *entre* particiones. Corresponde auditar la correspondencia imagen/máscara (y posibles máscaras compartidas intencionalmente) sin etiquetarla de error antes de examinar los datos. No se puede afirmar identidad o duplicación de contenido sin hash de los archivos.

## 2. Qué demuestra y qué no demuestra

**Comprobado:** el CSV auditado tiene exactamente el hash publicado por el manifest del artifact axial V2; el subconjunto curado contiene 610 registros; los identificadores documentados no se superponen entre particiones.

**Todavía no comprobado:** que no existan imágenes duplicadas por contenido con nombres/rutas diferentes; que las rutas de imagen/máscara existan y se relacionen correctamente; la concordancia con el segundo split histórico; la cantidad de estudios clínicos verdaderamente distintos. El hash del CSV no prueba por sí solo que los pesos del checkpoint sean reproducibles ni sustituye la verificación del artefacto de entrenamiento.

**Limitación metodológica que permanece:** el test de 102 registros fue evaluado previamente en `axial-full-v1`. Por tanto, el desempeño V2 sobre esa partición es **comparativo** y no constituye una evaluación final sobre un conjunto completamente intacto y nunca consultado. No crear un “nuevo test” sobre pacientes ya utilizados ni cambiar el umbral para producir un estado PASS.

## 3. Estado sugerido en la matriz de auditoría

- **Hallazgo #11:** `PARCIALMENTE RESUELTO — split E9 trazado, cotejado con SHA y sin solapamiento por identificador; subsisten revisión de contenido, discrepancia histórica y test reutilizado`.
- **Evidencia:** ZIP recibido, JSON/MD de Colab, manifest `models/final/axial_t2_alkafri_final_v2_candidate.pt.manifest.json`; notebooks `48_axial_final_training_patient_split.ipynb`, `49_axial_final_v2_train_validation.ipynb`, `50_axial_final_v2_test_once.ipynb`.
- **No marcar:** `CERRADO SIN LIMITACIONES` ni `TEST INDEPENDIENTE NUEVO`.

## 4. Corrección propuesta a LaTeX (condicionada a verificación de Codex)

En `chapters/capitulo_13_resultados_evaluacion.tex`, sección 13.2, actualizar la fila axial de la tabla de particiones por:

> Sudirman y Al-Kafri, plano axial | Paciente | 427 registros, 128 pacientes | 81 registros, 27 pacientes | 102 registros, 29 pacientes

Incorporar explicación concisa:

> La partición E9 del subconjunto axial curado comprende 610 registros asociados a 184 identificadores de paciente, distribuidos en 427 registros de entrenamiento (128 pacientes), 81 de validación (27 pacientes) y 102 de prueba (29 pacientes). El archivo `E9_t2_final_labels_curated_split.csv` coincide por SHA-256 con el manifest del artifact V2, y la auditoría de sus identificadores no encontró pacientes compartidos entre particiones ni filas idénticas duplicadas. Estos 610 registros no representan la totalidad del dataset original. La evaluación del test axial es comparativa, dado que esa partición ya había sido utilizada con un baseline anterior. La auditoría de duplicados por contenido y la comparación con un split histórico alternativo quedan delimitadas como verificaciones no ejecutadas.

## H11-B — auditoría posterior de contenido

El 14 de octubre de 2026 se aportó un reporte anonimizado adicional generado en Colab. Para las 610 filas del CSV se resolvieron exactamente 610 rutas de imagen y 610 rutas de máscara, sin filas no resueltas. Se calcularon hashes de contenido de 1.162 archivos distintos, sin errores de lectura. El reporte no encontró grupos repetidos de imágenes ni de pares imagen-máscara entre splits. Encontró 55 grupos de contenido repetido en máscaras (113 filas); esos grupos se mantuvieron dentro del mismo split y paciente, sin cruces entre splits o pacientes.

La igualdad de contenido no demuestra que una máscara esté alineada anatómicamente con la imagen ni que sus etiquetas sean semánticamente correctas. La repetición de máscaras (por ejemplo, vacías) tampoco prueba leakage por sí sola. H11-B no evalúa predicciones, no modifica métricas/manifests/gates y no convierte el test axial E9 —usado previamente en `axial-full-v1`— en una evaluación independiente. La diferencia con el split histórico alternativo sigue sin resolverse.

Se preservaron el ZIP con el resumen y el JSON anonimizados y el notebook v2 bajo `evidencias/fuentes_francisco_2026-10-14/`; los contenidos extraídos están en `evidencias/H11B_resultado_anonimizado/`. No se incorporaron rutas, identificadores de pacientes, CSV crudo, imágenes médicas ni credenciales.

Conservar una precisión sobre los “estudios”: los números 128/27/29 provienen de identificadores de paciente; no dar por probados estudios únicos adicionales.

También revisar `chapters/capitulo_11_capacidades_prototipo.tex` y `appendices/anexo_e_configuracion_entrenamiento.tex` para quitar únicamente afirmaciones ya refutadas por la auditoría (como que falta recuperar el conteo de entrenamiento). Mantener métricas Dice/IoU originales, calidad `candidate` y advertencia por reutilización de test.

## 5. Prompt operativo para Codex

> Trabajá en la rama **local de auditoría** ya preparada para los cuatro repositorios. Incorporá este archivo y los dos informes anonimizados de Colab como evidencia del hallazgo H11 (sin subir información identificatoria, CSV crudo, imágenes médicas ni credenciales). Verificá los datos contra el manifest V2 y los notebooks 48, 49 y 50 del AI Module; en particular, comprobá si `AXIAL_STUDY_COL` y `AXIAL_PATIENT_COL` se basaron ambos en `case_id_norm`. Auditá por qué el CSV tiene 384 rutas de máscara únicas frente a 427 imágenes en train y 87 frente a 102 en test; informá si la repetición es legítima o requiere corrección, sin alterar el dataset. Si los archivos originales están disponibles, calculá hashes de contenido de imágenes y máscaras para detectar coincidencias entre splits y registrá solo totales anónimos. Buscá el segundo CSV histórico y, si existe, compará diferencias de registros e IDs sin cambiar el split E9. Actualizá con cuidado el capítulo 13.2, el capítulo 11 y Anexo E para reportar 427/81/102 registros y 128/27/29 pacientes, sin equipararlos a 515 pacientes del dataset completo. Conservá la limitación de test reutilizado, las métricas y los quality gates originales. Actualizá el estado del hallazgo 11 en la matriz como parcial hasta cerrar los controles pendientes. Ejecutá QA, generá diff y commits **solo locales**. No hagas push, merge, rebase ni edites el Google Docs compartido.

## 6. Criterio de cierre del hallazgo

Puede considerarse **resuelta la inconsistencia documental de conteos y partición** cuando la tesis y la matriz muestren los valores verificados con la procedencia y hash. El **hallazgo global #11** debe conservar sus limitaciones explícitas sobre la reutilización del test y cualquier comprobación de integridad de datos que falte. Si el procedimiento de auditoría admite estados con reservas, puede cerrarse como `RESUELTO CON LIMITACIONES JUSTIFICADAS` únicamente tras documentar los controles adicionales o justificar su no ejecución; no describir test externo independiente.
