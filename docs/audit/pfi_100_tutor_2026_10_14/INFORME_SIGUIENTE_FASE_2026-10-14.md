# Informe de la siguiente fase de auditoría

Fecha: 2026-10-14. Trabajo local en `audit/pfi-100-tutor-2026-10-14`.

## Lote abordado

- **H63:** en §6.3.3 y dos tablas se reemplazó la afirmación de “1.545 máscaras finales”/“cobertura completa”. El texto ahora distingue 515 pacientes × 3 niveles como 1.545 combinaciones paciente-nivel nominales, no como inventario de archivos probado por el PFI. El expediente del proyecto no contiene el paquete fuente, conteo por paciente/nivel ni manifest enlazado para verificar el total. H63 permanece bloqueado.
- **H56:** la FODA ya no declara “reproducibilidad completa”. Precisa que el alcance documental es parcial por los inventarios/manifests ausentes y por las condiciones de uso de RSNA/LumbarDISC pendientes. H56 permanece bloqueado parcialmente.
- **H04:** se especificaron los artefactos necesarios para métricas sagitales Dice/IoU por clase: checkpoint/hash, split/hash, mapping de clases y reglas background/void, predicciones/GT vinculadas, protocolo de agregación y script/versión. No se fabricaron métricas ni se cambiaron Dice macro 0,8934, IoU macro 0,8080 ni resultados axiales.

## Verificación

pdfLaTeX/Biber/pdfLaTeX/pdfLaTeX finalizó con código 0. PDF: 232 páginas físicas. Se comprobó por extracción de texto la formulación en la página física 29 y la FODA en la página 42. El log no reporta referencias/citas indefinidas ni errores fatales. `git diff --check` pasa en archivos fuente versionados. No se ejecutaron pruebas de producto.

## Pendientes de esta fase ampliada

- H10: dictamen de consistencia entre capacidades (Demo Mode, exportación, Grad-CAM, 67B2/67C, chat) y alcance/requerimientos/código.
- H67: verificación primaria de bibliografía y afirmaciones enlazadas.
- Los hallazgos editoriales confirmados restantes requieren lotes separados con evidencia y QA individual. Los bloqueos H14/H31/H45/H56/H63/H66 no se cierran sin sus fuentes originales.
- El acuerdo RSNA, artefactos de checkpoint/pesos, encuesta original, soportes de entrevistas y paquete fuente de máscaras aún no fueron aportados.

Los únicos commits de esta fase son locales. No se modificaron los snapshots de integración ni Google Docs; no hubo push, merge o rebase.
