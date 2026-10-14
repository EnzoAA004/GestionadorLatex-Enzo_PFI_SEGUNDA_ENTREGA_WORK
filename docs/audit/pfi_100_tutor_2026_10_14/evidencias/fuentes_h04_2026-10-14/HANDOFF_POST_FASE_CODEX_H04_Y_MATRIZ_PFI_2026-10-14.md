# Handoff de continuación — H04 y conciliación de estado de auditoría PFI 100 %

**Fecha:** 14/10/2026. **Carácter:** instrucciones de auditoría documental; no autoriza publicación, merge ni alteraciones en datasets o modelos.

## 1. Baseline recibido

Codex informa trabajo **local** en `audit/pfi-100-tutor-2026-10-14` y PDF recompilado de **233 páginas físicas**, con QA pdfLaTeX/Biber y `git diff --check` satisfactorios. Los informes recibidos documentan H63/H56/H04 y el cierre documental H10. No se comprobó en esta intervención el checkout local de Windows ni el último PDF (no fueron adjuntados). No modificar snapshots de integración ni Google Docs del tutor.

**Discrepancia de estado comprobada:** La hoja `Seguimiento` de `MATRIZ_SEGUIMIENTO_AUDITORIA_PFI_100_2026.xlsx` contiene 67 filas de hallazgos y los siguientes estados actuales: 19 `Corrección aplicada`, 4 `Cerrado con evidencia`, 37 `Confirmado`, 1 `En investigación` (únicamente H67), 6 `Bloqueado por evidencia`. **La cabecera del `INFORME_ESTADO_AUDITORIA_PFI_100_2026.md` dice incorrectamente `En investigación = 2` y suma 68.** Actualizar esa cabecera y cualquier resumen dependiente, sin modificar el estado de ningún hallazgo para hacer cuadrar cifras.

## 2. Evidencia nueva — H04 sagital recuperada en Colab

Archivos disponibles para archivar en el expediente de auditoría:

- `H04_auditoria_sagital_por_clase_anonimizada.zip`, SHA-256 real del ZIP `c1cb2d8da690da97dcb4e2af7fbf461a110727c7ed29ffb39cadb3dc0a019c8b`.
- `H04_HANDOFF_METRICAS_SAGITALES_RECUPERADAS_2026-10-14.md`, con provenance, valores completos, cautelas y protocolo recomendado.

**Aclaración crítica:** el notebook H04 dio `NO_RECALCULADO`, pues no recibió las arrays/predicciones y el checkpoint original en esa sesión. No obstante recuperó en su inventario `source_reports` un informe histórico `final_test_metrics.json` que contiene desgloses por clase. No llamar a esto una evaluación nueva ni asignar al notebook una re-ejecución inexistente.

### Métricas sagitales históricas halladas

| ID | Clase | Dice | IoU | Cortes con GT presente | Cortes con predicción presente |
|---:|---|---:|---:|---:|---:|
| 0 | `background` (fuera del macro) | 0.9938577058644824 | 0.9877904066426408 | 1218 | 1218 |
| 1 | `vertebra_group` | 0.9086311731471105 | 0.8325610469993652 | 1113 | 1107 |
| 2 | `canal` | 0.9071209541140243 | 0.8300286820657623 | 465 | 483 |
| 3 | `disc_group` | 0.8645426918929516 | 0.7614048416617744 | 887 | 885 |
| | **Macro primer plano (clases 1–3)** | **0.8934316063846954** | **0.8079981902423006** | | |

El macro aritmético coincide exactamente con el manifiesto `sagittal-spider-final-v1`. El informe cubre 1218 cortes de 256×256; la asignación a **33 pacientes de test** procede del manifest, no de un recuento nuevo en este notebook. Los valores son agregados por clase a nivel píxel/cortes y luego macro entre clases: **no** presentarlos como macro por paciente ni como resultado del benchmark oculto SPIDER.

**Enlace al índice usado en entrenamiento:** `training_index_sha256 = 2720b7218c92870f6f0a000b57111ed36b5cf3b78c716f244f427ca7fee4a4ba`, coincidente entre reportes y manifest.

**Hash original reportado por el notebook:** `final_test_metrics.json` = `0b23514d88f75436154fc66cbf1e62a71c2b2208662447344e081b2d344818eb`. **El ZIP anonimizado NO incluye el archivo original completo**, de manera que se requiere localizarlo y recalcular independientemente su SHA-256 antes de afirmar autenticidad binaria de la fuente.

**Discrepancia entre checkpoints** que NO se puede ignorar:

- Best checkpoint durante entrenamiento: `fb124f0b1e73a5f3e548769bf837089295ce8e02c33fb34ed3be7fc3c2142a39`.
- Artifact runtime publicado: `cf11dcc0ad77a7c787e64a796a2fd7398ef906add461cef4b3d61f1a5238e944`.

La diferencia podría ser repaquetado, pero esa explicación es una **hipótesis** y NO está demostrada. Verificar equivalencia de tensores, mapping, arquitectura y protocolo de evaluación entre ambos antes de cerrar la cadena de procedencia. Evitar comparar solo las métricas, ya que no prueban identidad de pesos.

### Acción solicitada

1. Comprobar estado y HEAD de la rama local; respetar cambios no versionados/preexistentes, no push/merge.
2. Archivar el ZIP y el handoff H04 y documentar hashes de **los archivos realmente recibidos**.
3. Localizar el `final_test_metrics.json` original, comprobar SHA y vincular al notebook de entrenamiento `notebooks/45_gcs_spider_final_training.ipynb`, índice, split y release.
4. Documentar en capítulo 13/Anexo E, de forma explícita y sin inventar, las métricas históricas por clase **cuando se verifique procedencia suficiente**; de lo contrario, consignar los valores recuperados como evidencia histórica secundaria sujeta a verificación original.
5. Mantener separado el problema axial del H04: **6 clases totales**, con métrica oficial sobre cinco clases no-background (incluye `raw_0`, excluye `background_250`); `Dice=0.679348...`, `FAIL` para umbral `0.70`; el análisis sobre cuatro estructuras `~0.8106` es secundario y NO cambia el gate.
6. Mantener el estado de H04 **parcial** hasta resolver hash original, procedencia del checkpoint y demás trazabilidad necesaria. No atribuir exactitud clínica ni equivalencia a test SPIDER oculto.
7. Arreglar la cabecera del informe general: `En investigación = 1`, y corroborar que el panel/resúmenes Excel concuerdan. No cambiar 67 IDs ni su historial.
8. Compilar y revisar visualmente únicamente las zonas modificadas, y registrar commits **locales** de alcance acotado con referencia a H04 y al ajuste del informe.

## 3. Priorización posterior sugerida

- H67: cotejo bibliográfico fuente primaria para las citas [1]–[40], verificando DOI, metadatos y relación con afirmaciones.
- Correcciones editoriales de `Confirmado`: lotes H18–H30 y luego H32–H42, sin alterar evidencias ni quitar advertencias metodológicas esenciales.
- H31: requerir export de encuesta y cuestionario original del usuario; no fabricar denominadores.
- H14/H45/H66: mantener bloqueo hasta que existan registros/autorizaciones o aplicar minimización identificable y atribuciones no personalizadas; no inventar consentimientos.
- H56: documentación legal completa de RSNA y pesos/checkpoints, separar uso académico de autorización comercial.
- H63: inventario original de máscaras y protocolo de etiquetas; no declarar 1545 archivos verificados.
- H13/H48: contrastar cifras solo con workbook canónico reconciliado aprobado y su hash; no importar cifras de un documento alternativo sin reconciliación.

**Criterio final:** auditoría H04 y auditoría general siguen abiertas; no sincronizar automáticamente el Google Docs compartido ni declarar cierre definitivo.
