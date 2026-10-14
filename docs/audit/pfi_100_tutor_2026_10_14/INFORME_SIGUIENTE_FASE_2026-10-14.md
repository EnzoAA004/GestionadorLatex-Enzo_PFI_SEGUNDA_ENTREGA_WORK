# Informe de la siguiente fase de auditoría

Fecha: 2026-10-14. Trabajo local en `audit/pfi-100-tutor-2026-10-14`.

## Lote abordado

- **H63:** en §6.3.3 y dos tablas se reemplazó la afirmación de “1.545 máscaras finales”/“cobertura completa”. El texto ahora distingue 515 pacientes × 3 niveles como 1.545 combinaciones paciente-nivel nominales, no como inventario de archivos probado por el PFI. El expediente del proyecto no contiene el paquete fuente, conteo por paciente/nivel ni manifest enlazado para verificar el total. H63 permanece bloqueado.
- **H56:** la FODA ya no declara “reproducibilidad completa”. Precisa que el alcance documental es parcial por los inventarios/manifests ausentes y por las condiciones de uso de RSNA/LumbarDISC pendientes. H56 permanece bloqueado parcialmente.
- **H04:** se archivó un inventario anonimizado que recupera valores históricos sagitales Dice/IoU por clase, sin evaluación nueva. El JSON original no acompaña el ZIP y su SHA informado sigue sin verificación independiente. El checkpoint runtime del snapshot coincide con el manifest (`cf11…`), pero no se demostró equivalencia con el best checkpoint de entrenamiento (`fb124…`). Los valores se consignaron como evidencia histórica secundaria en el Anexo E; H04 continúa parcial.
- **H10:** cerrado documentalmente. §5.5 define las extensiones auxiliares (Demo Mode, PDF/JSON, Grad-CAM, 67B2, 67C, chat) como complementarias y sin RF de aceptación del flujo principal; §7/§11 distinguen el preinforme determinístico del chat mock. Se conservaron los estados de código y no se afirmó despliegue productivo de Qwen.

## Verificación

pdfLaTeX/Biber/pdfLaTeX/pdfLaTeX finalizó con código 0. PDF: 233 páginas físicas. Se revisaron visualmente la delimitación de H10 en la página física 25, H63 en la 29 y la FODA en la 43. El log no reporta referencias/citas indefinidas ni errores fatales. `git diff --check` pasa en archivos fuente versionados. No se ejecutaron pruebas de producto.

## Pendientes de esta fase ampliada

- H67: verificación primaria de bibliografía y afirmaciones enlazadas.
- Los hallazgos editoriales confirmados restantes requieren lotes separados con evidencia y QA individual. Los bloqueos H14/H31/H45/H56/H63/H66 no se cierran sin sus fuentes originales.
- El acuerdo RSNA, artefactos de checkpoint/pesos, encuesta original, soportes de entrevistas y paquete fuente de máscaras aún no fueron aportados.

**Dictamen provisional H67:** permanece “En investigación”. La verificación previa solo cubría parcialmente las referencias citadas en la matriz; en esta tanda no se hizo cotejo primario completo de [1]–[40], sus DOI, metadatos editoriales y afirmaciones asociadas. No se alteraron citas ni bibliografía por conjetura. Para cerrarlo hace falta un barrido referenciado registro por registro, con una fuente editorial/DOI verificable y revisión de pertinencia para cada afirmación sustantiva.

Commits locales de esta fase: `de37d9c` (H63/H56/H04 y PDF), `5688ffb` (referencias en matriz), `b549056` (alcance H10), `3d34839` (registro de H10) y `aca3d08` (matriz H10). No se modificaron los snapshots de integración ni Google Docs; no hubo push, merge o rebase.
