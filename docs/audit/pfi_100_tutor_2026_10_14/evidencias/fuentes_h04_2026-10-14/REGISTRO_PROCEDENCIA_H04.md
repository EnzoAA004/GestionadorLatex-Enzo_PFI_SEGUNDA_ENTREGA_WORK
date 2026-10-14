# Registro de procedencia — H04 sagital

**Fecha de recepción e inspección:** 14 de octubre de 2026. **Alcance:** archivo documental local; no se ejecutó una inferencia ni se modificó el snapshot AI Module.

## Archivos recibidos y archivados

| Archivo | SHA-256 verificado en origen y copia |
|---|---|
| `H04_auditoria_sagital_por_clase_anonimizada.zip` | `c1cb2d8da690da97dcb4e2af7fbf461a110727c7ed29ffb39cadb3dc0a019c8b` |
| `PFI_H04_Auditoria_Sagital_Dice_IoU_Por_Clase_v1.ipynb` | `85df88f244f041b8dd29d9de24f725d6f7dce9055b8fcff64da49618aa392551` |
| `HANDOFF_POST_FASE_CODEX_H04_Y_MATRIZ_PFI_2026-10-14.md` | `185b2a265bc4e19a06bcd8901cd6e0ac88d2eff95fcf8e146c2081933eb05a9f` |

Los tres archivos se conservan byte por byte en este directorio. El ZIP anonimizado contiene `H04_resumen_anonimo.json` y `H04_informe_anonimo.md`; **no** contiene el `final_test_metrics.json` histórico completo. El resultado del notebook fue `NO_RECALCULADO`, pues no dispuso de arrays/predicciones ni del checkpoint original.

## Qué se verificó localmente

- El inventario JSON anonimizado enumera 23 fuentes candidatas, entre ellas `final_test_metrics.json`, e informa para el original el SHA-256 `0b23514d88f75436154fc66cbf1e62a71c2b2208662447344e081b2d344818eb`. El inventario transcribe los valores por clase reproducidos en el Anexo E y el hash del índice de entrenamiento `2720b7218c92870f6f0a000b57111ed36b5cf3b78c716f244f427ca7fee4a4ba`.
- El SHA del checkpoint `models/final/sagittal_spider_multiclass_final_best.pt` del snapshot local AI Module es `cf11dcc0ad77a7c787e64a796a2fd7398ef906add461cef4b3d61f1a5238e944`, consistente con su manifest. El inventario histórico reporta otro SHA como best checkpoint de entrenamiento: `fb124f0b1e73a5f3e548769bf837089295ce8e02c33fb34ed3be7fc3c2142a39`. No se obtuvo el archivo de ese hash ni se compararon tensores; la hipótesis de repaquetado no se considera comprobada.
- Se inspeccionaron en el snapshot el notebook de entrenamiento `notebooks/45_gcs_spider_final_training.ipynb`, el manifest y el model card sagital. El notebook declara el hash esperado del índice y la salida `final_test_metrics.json`; el archivo JSON original no fue localizado en el snapshot inspeccionado. La mera declaración de generación no autentica una copia ausente.
- La matriz registra 67 IDs, con estados de auditoría 19 `Corrección aplicada`, 4 `Cerrado con evidencia`, 37 `Confirmado`, 1 `En investigación` y 6 `Bloqueado por evidencia`. El panel contiene fórmulas que reflejan esos conteos al recalcularse; su vista importada mostró 67 en total y 1 en investigación.

## Limitación y próximos artefactos requeridos

No está localizado el archivo `final_test_metrics.json` para recalcular su SHA, ni el artifact exacto de best checkpoint `fb124…` o evidencia de equivalencia verificable con el checkpoint runtime `cf11…`. Para autenticar/reproducir el reporte hacen falta el JSON original; el checkpoint exacto o comparación reproducible de pesos; el split/hash, mapping de clases y protocolo/script versionado; y, para una reevaluación independiente, predicciones y ground truth por caso (o entradas suficientes para regenerarlas). Los valores recuperados son evidencia histórica secundaria, agregada por clase sobre cortes/píxeles y luego macro entre las clases 1–3. No son macro por paciente, evaluación nueva, benchmark oculto SPIDER ni evidencia de exactitud clínica. H04 permanece parcial.

El handoff separado `H04_HANDOFF_METRICAS_SAGITALES_RECUPERADAS_2026-10-14.md` mencionado en la instrucción de entrega no estaba presente en Descargas; se conserva el handoff efectivamente recibido con su hash arriba.
