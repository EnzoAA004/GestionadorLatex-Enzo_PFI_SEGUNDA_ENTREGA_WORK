# Informe de estado de la auditoría PFI — 100% tutor 2026

**Corte:** 14 de octubre de 2026. **Estado:** auditoría local en curso; no cerrada ni publicada. Los 67 hallazgos están registrados individualmente en la matriz de seguimiento. No se marca ningún hallazgo resuelto sin evidencia. Los estados parciales y los bloqueos se conservan como tales.

## Resumen de estados

| Estado | Hallazgos |
|---|---:|
| Corrección aplicada | 19 |
| Cerrado con evidencia | 3 |
| Confirmado | 37 |
| En investigación | 2 |
| Bloqueado por evidencia | 6 |

## Registro de los 67 hallazgos

| ID | Estado de auditoría | Confirmación | Repositorio(s) | Commit local | Acción / justificación registrada |
|---:|---|---|---|---|---|
| 1 | Corrección aplicada | Parcial | Gestionador LaTeX | 58e29fcb34942a7cf3107908f1f4911791df70d4 | Se conservó la portada existente y se completaron el resumen y abstract bilingües con palabras clave y resultados respaldados. |
| 2 | Corrección aplicada | Sí | Gestionador LaTeX | 58e29fcb34942a7cf3107908f1f4911791df70d4 | Se agregó un capítulo final con relación objetivo–evidencia–cumplimiento, discusión, limitaciones y trabajo futuro; la redacción conserva los límites reales de la evidencia. |
| 3 | Cerrado con evidencia | No | Gestionador LaTeX | 0454dc38ce0e12c3267e73b5fcb4b852c3cfde89 | Cerrado con evidencia: las cuatro figuras cuestionadas aparecen en el PDF final con diagramas/captions activos y se revisaron visualmente las páginas físicas 94, 96, 105 y 132 del PDF recompilado. |
| 4 | Confirmado | Parcial | Gestionador LaTeX; AI Module |  | Model card axial ya aporta Dice/IoU por clase; el model card sagital solo publica macro no-background. Gate axial oficial sigue sin aprobarse (Dice macro foreground 0,67935). Completar el desglose solo donde el artifact lo respalde. |
| 5 | Corrección aplicada | Sí | Gestionador LaTeX; Backend; AI Module | 21295af8462380cf1591ca607c1aad7cbe708b0a | Se aclaró que RF-22 define las ocho categorías P10.7 pero la inferencia automática del producto está deshabilitada por blocked_preprocessing_parity y automaticInferenceEnabled=false; sin cambios de código. |
| 6 | Corrección aplicada | Sí | Gestionador LaTeX; AI Module | 4f27a62214e254e1d991cba379b4c9c6cbf5d52b | Se separaron P10.6 (clasificador axial RSNA/LumbarDISC) y P10.7 (ocho hallazgos sagitales SPIDER); se documentó tarea y procedencia sin reconstruir particiones ni reentrenar. |
| 7 | Corrección aplicada | Sí | Gestionador LaTeX; Frontend; Backend | 304153cbdbc0a1908efa9d361d03bbe148d30a92 | Precisar alcances; no atribuir 11/11 al flujo global. |
| 8 | Corrección aplicada | Parcial | Gestionador LaTeX | ecaf4cf6e4c57bb08f506167b430ca7b8289feb6 | Se alineó el cronograma académico con la entrega del 75 % y la defensa, separándolos del cierre de software y la validación profesional posterior. |
| 9 | Corrección aplicada | Parcial | Gestionador LaTeX; Backend; Frontend | 11568e2e8d5a80b6551288fbca74c6d13bb0ffa3 | Se reconcilió el uso actual: Patient/patientId en API y persistencia Backend; subjectRef sigue activo en historial/comparación del Frontend; Demo Mode es descriptivo y el alta/selección completa desde navegador es parcial. |
| 10 | En investigación | Parcial | Gestionador LaTeX; Backend; Frontend; AI Module |  | Cruzar cada elemento con alcance, RF y código; resolver solo los casos sin definición/estado consistente. |
| 11 | Corrección aplicada | Sí | Gestionador LaTeX; AI Module | 461cd1a5a7efed8840f7008116e713208cda125a | H11-A documenta 610 registros/184 pacientes y SHA del CSV. H11-B reporta 610/610 pares de rutas resueltos, 1.162 hashes sin fallos, cero grupos repetidos de imágenes/pares entre splits, y 55 grupos de máscaras repetidas (113 filas) dentro del mismo split/paciente. No valida alineación anatómica/semántica; test reutilizado y split histórico alternativo siguen como límites. |
| 12 | Confirmado | Parcial | Gestionador LaTeX; AI Module |  | Se localizaron IoU agregadas axial y sagital en manifests/model cards; no se encontró HD95/NSD reportado. Mantener sus valores ligados a modelo, split y agregación, y declarar HD95/NSD no calculados. |
| 13 | Corrección aplicada | Parcial | Gestionador LaTeX | 643e657502440e933c59f1356e3beae1edd5df44 | Se transcribieron los supuestos verificados del libro canónico y se aclaró que los clientes fraccionarios son equivalentes esperados del modelo, no observaciones comerciales. |
| 14 | Bloqueado por evidencia | Parcial | Gestionador LaTeX |  | Bloqueado hasta localizar registros fechados de sesiones, consentimientos y autorizaciones; no se inventaron metadatos ni se contactó a los profesionales. |
| 15 | Confirmado | Sí | Gestionador LaTeX; Backend; AI Module |  | Reproducir el comando/documento de suite; identificar cada fallo y si es ambiental, aislarlo con skip condicionado y razón, o reparar sin esconder fallos. |
| 16 | Cerrado con evidencia | No | Gestionador LaTeX | 0454dc38ce0e12c3267e73b5fcb4b852c3cfde89 | Cerrado con evidencia: la duplicación no aparece en el PDF final y el párrafo de organización documental aparece una sola vez en la página física 19. |
| 17 | Cerrado con evidencia | No | Gestionador LaTeX | 0454dc38ce0e12c3267e73b5fcb4b852c3cfde89 | Cerrado con evidencia: el encabezado 5.6 “Alcance del documento final” figura en el índice y en la página física 25; las dos frases duplicadas no aparecen en el PDF final. |
| 18 | Confirmado | Sí | Gestionador LaTeX |  | Conservar una descripción principal y referenciarla desde el anexo, después de verificar los conteos en la fuente primaria. |
| 19 | Confirmado | Sí | Gestionador LaTeX |  | Dejar explicación completa en resultados y usar referencias breves en capacidades/limitaciones. |
| 20 | Confirmado | Parcial | Gestionador LaTeX |  | Consolidar sin eliminar límites distintos ni reducir una limitación con impacto metodológico. |
| 21 | Confirmado | Sí | Gestionador LaTeX |  | Revisar ítems contra el texto antes de renumerar; conservar conclusiones numéricas verificadas. |
| 22 | Confirmado | Sí | Gestionador LaTeX |  | Mantener una explicación canónica V1/V2 y resumir el resto mediante referencias; no borrar distinciones de entorno. |
| 23 | Confirmado | Sí | Gestionador LaTeX |  | Conservar síntesis en resultados y dejar fichas/evidencia en Anexo H; revisar duplicaciones internas del anexo. |
| 24 | Confirmado | Parcial | Gestionador LaTeX |  | Definir una explicación canónica y evitar suprimir advertencias locales necesarias para interpretar cada resultado. |
| 25 | Confirmado | Sí | Gestionador LaTeX |  | Consolidar requisitos solo tras comparar criterios de aceptación y conservar toda trazabilidad ID. |
| 26 | Confirmado | Sí | Gestionador LaTeX |  | Migrar remisiones a labels automáticos y comprobar los destinos en PDF. |
| 27 | Confirmado | Parcial | Gestionador LaTeX |  | Identificar la fuente de cada requisito y completar trazabilidad, sin atribuir una necesidad de usuario inexistente. |
| 28 | Confirmado | Sí | Gestionador LaTeX |  | Usar estados temporales precisos: diseñado, desplegado, probado y no productivo; enlazar evidencia de cada componente. |
| 29 | Confirmado | Sí | Gestionador LaTeX |  | Resolver junto con H53 y distinguir puntaje calibrado de estado operativo. |
| 30 | Confirmado | Sí | Gestionador LaTeX |  | Acordar un mapa de niveles con nombres y alcance explícitos y referenciarlo, distinguiéndolo de las capas de test. |
| 31 | Bloqueado por evidencia | Parcial | Gestionador LaTeX |  | Se localizaron figuras de encuesta, pero no exportación fuente de respuestas. Solicitar CSV/XLSX original del formulario y versión del cuestionario; no reconstruir denominadores desde las figuras. |
| 32 | Confirmado | Sí | Gestionador LaTeX |  | Ajustar cualquier uso ambiguo de “validado” a “evaluado”; separar co-registro T1/T2 intra-dataset de registro multiplanar entre datasets. |
| 33 | Confirmado | Sí | Gestionador LaTeX |  | Definir términos preferidos y estados de revisión en glosario/contrato; armonizar el uso en prosa y tablas. |
| 34 | Confirmado | Sí | Gestionador LaTeX |  | Mover la historia necesaria a anexos cronológicos y convertir el resto en descripción del estado actual. |
| 35 | Corrección aplicada | Parcial | Gestionador LaTeX | 1126134521c79d5858b220c5a163e0dd7f84610e | Usar mismos puntos anatómicos antes de cualquier comparación; no interpretar 36° como anormal. |
| 36 | Confirmado | Sí | Gestionador LaTeX |  | Presentarlos como antecedentes, no benchmark comparativo, salvo que se adopte partición/protocolo realmente comparable. |
| 37 | Confirmado | Sí | Gestionador LaTeX |  | Numerar ecuaciones por capítulo y verificar símbolos y exponentes visualmente antes del PDF de cierre. |
| 38 | Confirmado | Parcial | Gestionador LaTeX |  | Inventariar cada tabla, rotular y normalizar de forma consistente; reconstruir listas en compilación final. |
| 39 | Confirmado | Parcial | Gestionador LaTeX |  | Revisar niveles de headings, entradas de índice y títulos contra PDF recompilado, no editar números impresos manualmente. |
| 40 | Confirmado | Sí | Gestionador LaTeX |  | Corregir idioma/tiempos verbales tras verificar cada estado contra evidencia del repositorio. |
| 41 | Confirmado | Parcial | Gestionador LaTeX |  | Definir siglas y términos en primera aparición/glosario; mantener códigos internos solo donde aporten trazabilidad. |
| 42 | Confirmado | Parcial | Gestionador LaTeX |  | Homogeneizar títulos/niveles y ordenar glosario; verificar la primera página del Anexo H en el PDF. |
| 43 | Confirmado | Sí | Gestionador LaTeX |  | Agregar tabla de contribuciones solo con evidencia de autoría verificable; evitar inferir roles personales. |
| 44 | Confirmado | Sí | Gestionador LaTeX |  | Revisar qué identificadores son públicos/necesarios y trasladar hashes/licencias/instrucciones a una disponibilidad reproducible; nunca eliminar trazabilidad de evidencia. |
| 45 | Bloqueado por evidencia | Parcial | Gestionador LaTeX |  | No publicar detalles personales adicionales ni completar consentimientos retroactivamente; localizar autorizaciones existentes y limitar la versión a evidencia autorizada. |
| 46 | Confirmado | Sí | Gestionador LaTeX; AI Module |  | Agregar solo visualizaciones y métricas reconstruibles desde predicciones/anotaciones verificables; no generar intervalos sin datos fuente. |
| 47 | Confirmado | Sí | Gestionador LaTeX |  | Distinguir requisito medible de resultado observado; definir metas solo si la evidencia y el alcance las sostienen. |
| 48 | Confirmado | Parcial | Gestionador LaTeX |  | Reconciliar fórmulas y escenarios con workbook canónico, comentar valores extremos y normalizar formato numérico. |
| 49 | Confirmado | Sí | Gestionador LaTeX |  | Crear matriz cualitativa probabilidad-impacto-mitigación con supuestos declarados, sin asignar probabilidades cuantitativas inventadas. |
| 50 | Confirmado | Parcial | Gestionador LaTeX |  | Verificar referencias una a una en sus fuentes/editoriales; no añadir citas sin confirmar pertinencia y metadatos. |
| 51 | Confirmado | Sí | Gestionador LaTeX |  | Reducir o mover el detalle de branding y presentar el nombre en introducción/alcance si se conserva. |
| 52 | Confirmado | Sí | Gestionador LaTeX |  | Corregir duplicación y precisión terminológica; atribuir la propuesta técnica con fuente y alcance concretos. |
| 53 | Corrección aplicada | Sí | Gestionador LaTeX | 44a2481734bfe47d3d344fe8479af1b33ac198a7 | Corregir atribución plural; distinguir la preocupación de EN-01 de las opiniones favorables y presentar la decisión como criterio de diseño con fundamento metodológico. |
| 54 | Corrección aplicada | Sí | Gestionador LaTeX | 44a2481734bfe47d3d344fe8479af1b33ac198a7 | Retirar la cita textual o identificar una fuente primaria fechada y autorizada; conservar transcripciones sin cambios. |
| 55 | Corrección aplicada | Parcial | Gestionador LaTeX | 784066e6723fab9cb90bf5794783c3e667a1b415 | La comparación independiente requerirá estudios comunes, especialistas y protocolo; no se presenta como realizada. |
| 56 | Bloqueado por evidencia | Parcial | Gestionador LaTeX; AI Module |  | Las fuentes primarias consultadas publican SPIDER y Al-Kafri/Mendeley V2 bajo CC BY 4.0; la ficha RSNA identifica un Research Use Agreement y su artículo limita a uso no comercial. H56 sigue parcialmente bloqueado por el texto integral del acuerdo RSNA inaccesible desde esta sesión y las condiciones/licencia propias de checkpoints/pesos y redistribución. |
| 57 | Confirmado | Sí | Gestionador LaTeX; AI Module |  | Reportar la partición como evaluación propia y reformular cualquier equivalencia con benchmark; no reentrenar ni acceder a test oculto sin protocolo. |
| 58 | Confirmado | Parcial | Gestionador LaTeX; AI Module |  | Actualizar el análisis como antecedente comparable y justificar por qué no se usa como baseline directo; no presentar sus métricas como comparación propia. |
| 59 | Corrección aplicada | Sí | Gestionador LaTeX | 1126134521c79d5858b220c5a163e0dd7f84610e | Citar la revisión para describir criterios usados, no para inferir superioridad diagnóstica. |
| 60 | Corrección aplicada | Sí | Gestionador LaTeX | 1126134521c79d5858b220c5a163e0dd7f84610e | No clasificar el estudio ni el método a partir de un único corte/medición. |
| 61 | Corrección aplicada | Parcial | Gestionador LaTeX | 475570dabc211261c0b8f6733bb197b910fb1b68 | El inventario comercial completo y comparación de estudios clínicos siguen parciales; revisar cada resumen/indicación antes de comparaciones de desempeño. |
| 62 | Corrección aplicada | Sí | Gestionador LaTeX | 475570dabc211261c0b8f6733bb197b910fb1b68 | Usar el artículo como ejemplo metodológico externo, no como resultado propio ni umbral de aceptación del PFI. |
| 63 | Bloqueado por evidencia | Parcial | Gestionador LaTeX; AI Module |  | Se retiró “cobertura completa” y “1.545 máscaras finales”: 515×3 queda como combinaciones paciente-nivel nominales, no conteo auditado. Faltan máscaras fuente, índice por archivo/paciente/nivel, mapping T1→T2, manifest enlazado y protocolo/autoría. El manifest axial mantiene IDs opacos. |
| 64 | Corrección aplicada | Sí | Gestionador LaTeX | 475570dabc211261c0b8f6733bb197b910fb1b68 | Comparación directa de utilidad/esfuerzo contra los PACS de los centros no fue realizada. |
| 65 | Corrección aplicada | Parcial | Gestionador LaTeX | 784066e6723fab9cb90bf5794783c3e667a1b415 | No se implementa ni valida interpretación diagnóstica automática; decisión de alcance explícita. |
| 66 | Bloqueado por evidencia | Parcial | Gestionador LaTeX |  | Limitar perfiles a datos respaldados por las fuentes disponibles; localizar fechas/consentimientos/autorización antes de publicar información personal adicional. |
| 67 | En investigación | Parcial | Gestionador LaTeX |  | Auditar todos los registros y sus afirmaciones enlazadas; corregir metadatos solo tras cotejo editorial/DOI. |

## Evidencia final de compilación

La tesis compila en el worktree local con pdfLaTeX (MiKTeX 25.12) y Biber 2.21; el PDF tiene 232 páginas físicas (230 páginas numeradas en el cuerpo). SHA-256 del PDF: `903848C2013B2E5574FA702B71386BB2FAC1B68AD50959C2C6B5A15BB577F554`. La búsqueda del log final no reporta errores fatales, citas indefinidas ni referencias cruzadas indefinidas. En esta fase se revisaron visualmente las páginas físicas 29 (H63) y 42 (FODA); también se verificaron Lista de Figuras p.15 y Tabla 6.2 p.35. Las advertencias de composición en tablas preexistentes se mantienen como limitación visual menor.

## Hallazgos que mantienen límites o requieren evidencia adicional

- **H04:** el artefacto axial trae métricas por clase; el sagital solo trae macro Dice/IoU. No se reentrenó ni se extrapolaron métricas.
- **H63:** las 1.545 no son un inventario verificado de máscaras del proyecto; la cifra se conserva únicamente como 515×3 combinaciones nominales y H63 sigue bloqueado.
- **H56:** se matizó la afirmación de reproducibilidad; el acuerdo RSNA y términos de checkpoint/pesos siguen sin verificarse.
- **H12:** se localizaron IoU por modelo; no se localizaron valores HD95/NSD, que quedan como no calculados.
- **H11:** H11-B agrega hashes de contenido de 1.162 archivos y no encuentra duplicados de imagen/pares entre splits; sí hay 55 grupos de máscaras repetidas dentro de mismo paciente/split. No verifica alineación anatómica ni resuelve el split histórico; el test se usó en axial-full-v1.
- **H14:** faltan registros fechados de sesiones, consentimientos y autorizaciones; la resolución queda bloqueada por evidencia.
- **H14, H45 y H66:** el Anexo D contiene transcripciones documentales, no audios originales ni metadatos de consentimiento/fecha/autorización suficientes para validar atribución y publicación.
- **H31:** faltan exportación original de respuestas y versión del cuestionario; solo se localizaron figuras de encuesta.
- **H56:** SPIDER y Al-Kafri/Mendeley V2 identifican CC BY 4.0; RSNA identifica un Research Use Agreement y la publicación oficial dice uso no comercial. Falta obtener el texto íntegro accesible del acuerdo RSNA y confirmar términos de los checkpoints/pesos y su redistribución.
- **H63:** faltan paquete de máscaras fuente, manifest enlazado a estudios/pacientes y registro/protocolo de etiquetado.
- **H67 y otros hallazgos de investigación:** permanecen abiertos hasta completar la verificación bibliográfica y documental correspondiente.

Los repositorios Backend, Frontend y AI Module se conservaron en sus snapshots locales declarados y se inspeccionaron sin modificaciones. No se hizo push, merge, publicación remota, edición de Google Docs ni contacto con el tutor. Los archivos externos pendientes por ID quedan detallados en la matriz y en el registro de evidencia actualizado. El cierre definitivo permanece abierto.
