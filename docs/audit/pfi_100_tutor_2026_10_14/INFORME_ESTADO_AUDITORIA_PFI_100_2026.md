# Informe de estado de la auditoría PFI — 100% tutor 2026

**Corte:** 14 de octubre de 2026. **Estado:** auditoría local en curso; no cerrada ni publicada. Los 67 hallazgos están registrados individualmente en la matriz de seguimiento. No se marca ningún hallazgo resuelto sin evidencia. Los estados parciales y los bloqueos se conservan como tales.

## Resumen de estados

| Estado | Hallazgos |
|---|---:|
| Corrección aplicada | 18 |
| Cerrado con evidencia | 3 |
| Confirmado | 37 |
| En investigación | 3 |
| Bloqueado por evidencia | 6 |

## Registro de los 67 hallazgos

| ID | Estado de auditoría | Confirmación | Repositorio(s) | Commit local | Acción / justificación registrada |
|---:|---|---|---|---|---|
| 1 | Corrección aplicada | Parcial | Gestionador LaTeX | 58e29fcb34942a7cf3107908f1f4911791df70d4 | Se conservó la portada existente y se completaron el resumen y abstract bilingües con palabras clave y resultados respaldados. |
| 2 | Corrección aplicada | Sí | Gestionador LaTeX | 58e29fcb34942a7cf3107908f1f4911791df70d4 | Se agregó un capítulo final con relación objetivo–evidencia–cumplimiento, discusión, limitaciones y trabajo futuro; la redacción conserva los límites reales de la evidencia. |
| 3 | Cerrado con evidencia | No | Gestionador LaTeX | 0454dc38ce0e12c3267e73b5fcb4b852c3cfde89 | Cerrado con evidencia: las cuatro figuras cuestionadas aparecen en el PDF final con diagramas/captions activos y se revisaron visualmente las páginas físicas 93, 95, 104 y 131. |
| 4 | Confirmado | Parcial | Gestionador LaTeX; AI Module |  | Mantener el gate oficial y completar la tabla por clase con métricas provenientes del artifact verificable; no reinterpretar el promedio secundario como aprobado. |
| 5 | Corrección aplicada | Sí | Gestionador LaTeX; Backend; AI Module | 21295af8462380cf1591ca607c1aad7cbe708b0a | Se aclaró que RF-22 define las ocho categorías P10.7 pero la inferencia automática del producto está deshabilitada por blocked_preprocessing_parity y automaticInferenceEnabled=false; sin cambios de código. |
| 6 | Corrección aplicada | Sí | Gestionador LaTeX; AI Module | 4f27a62214e254e1d991cba379b4c9c6cbf5d52b | Se separaron P10.6 (clasificador axial RSNA/LumbarDISC) y P10.7 (ocho hallazgos sagitales SPIDER); se documentó tarea y procedencia sin reconstruir particiones ni reentrenar. |
| 7 | Corrección aplicada | Sí | Gestionador LaTeX; Frontend; Backend | 304153cbdbc0a1908efa9d361d03bbe148d30a92 | Precisar alcances; no atribuir 11/11 al flujo global. |
| 8 | Corrección aplicada | Parcial | Gestionador LaTeX | ecaf4cf6e4c57bb08f506167b430ca7b8289feb6 | Se alineó el cronograma académico con la entrega del 75 % y la defensa, separándolos del cierre de software y la validación profesional posterior. |
| 9 | En investigación | Parcial | Gestionador LaTeX; Backend; Frontend |  | Mantener explícita la separación API/Frontend y ajustar estados de requisito a la evidencia de integración. |
| 10 | En investigación | Parcial | Gestionador LaTeX; Backend; Frontend; AI Module |  | Cruzar cada elemento con alcance, RF y código; resolver solo los casos sin definición/estado consistente. |
| 11 | Corrección aplicada | Sí | Gestionador LaTeX; AI Module | 461cd1a5a7efed8840f7008116e713208cda125a | Se incorporaron los conteos y trazas verificables del split E9, junto con los límites de uso previo del test, falta del split histórico alternativo y ausencia de control de duplicados por contenido. Resolución parcial. |
| 12 | Confirmado | Sí | Gestionador LaTeX; AI Module |  | Recuperar IoU por modelo y reportarlo; si HD95 no existe, declararlo no calculado y revisar que el objetivo/criterio no prometa esa evidencia. |
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
| 31 | Bloqueado por evidencia | Parcial | Gestionador LaTeX |  | Solicitar/localizar cuestionario y exportación agregada original; no reconstruir respuestas ni denominadores desde porcentajes del PDF. |
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
| 56 | Bloqueado por evidencia | Parcial | Gestionador LaTeX; AI Module |  | Mantener bloqueado hasta adjuntar y revisar términos/licencias vigentes por dataset/modelo, alcance de redistribución y uso comercial; documentar límite sin emitir conclusión legal no sustentada. |
| 57 | Confirmado | Sí | Gestionador LaTeX; AI Module |  | Reportar la partición como evaluación propia y reformular cualquier equivalencia con benchmark; no reentrenar ni acceder a test oculto sin protocolo. |
| 58 | Confirmado | Parcial | Gestionador LaTeX; AI Module |  | Actualizar el análisis como antecedente comparable y justificar por qué no se usa como baseline directo; no presentar sus métricas como comparación propia. |
| 59 | Corrección aplicada | Sí | Gestionador LaTeX | 1126134521c79d5858b220c5a163e0dd7f84610e | Citar la revisión para describir criterios usados, no para inferir superioridad diagnóstica. |
| 60 | Corrección aplicada | Sí | Gestionador LaTeX | 1126134521c79d5858b220c5a163e0dd7f84610e | No clasificar el estudio ni el método a partir de un único corte/medición. |
| 61 | Corrección aplicada | Parcial | Gestionador LaTeX | 475570dabc211261c0b8f6733bb197b910fb1b68 | El inventario comercial completo y comparación de estudios clínicos siguen parciales; revisar cada resumen/indicación antes de comparaciones de desempeño. |
| 62 | Corrección aplicada | Sí | Gestionador LaTeX | 475570dabc211261c0b8f6733bb197b910fb1b68 | Usar el artículo como ejemplo metodológico externo, no como resultado propio ni umbral de aceptación del PFI. |
| 63 | Bloqueado por evidencia | Parcial | Gestionador LaTeX; AI Module |  | Localizar release exacto, manifest y cuaderno; verificar máscaras y pacientes únicos antes de corregir conteos. No reconstruir cifras por multiplicación sola. |
| 64 | Corrección aplicada | Sí | Gestionador LaTeX | 475570dabc211261c0b8f6733bb197b910fb1b68 | Comparación directa de utilidad/esfuerzo contra los PACS de los centros no fue realizada. |
| 65 | Corrección aplicada | Parcial | Gestionador LaTeX | 784066e6723fab9cb90bf5794783c3e667a1b415 | No se implementa ni valida interpretación diagnóstica automática; decisión de alcance explícita. |
| 66 | Bloqueado por evidencia | Parcial | Gestionador LaTeX |  | Limitar perfiles a datos respaldados por las fuentes disponibles; localizar fechas/consentimientos/autorización antes de publicar información personal adicional. |
| 67 | En investigación | Parcial | Gestionador LaTeX |  | Auditar todos los registros y sus afirmaciones enlazadas; corregir metadatos solo tras cotejo editorial/DOI. |

## Evidencia final de compilación

La tesis compila en el worktree local con pdfLaTeX (MiKTeX 25.12) y Biber 2.21; el PDF tiene 231 páginas físicas. SHA-256 del PDF: `7cd60328ebedd83f902813a2baa14c2647025fd1ce2d9e15a49f58eaefd70c78`. La búsqueda del log final no reporta errores fatales, citas indefinidas ni referencias cruzadas indefinidas. La tabla de supuestos del modelo financiero se renderizó y revisó visualmente en la página PDF 155. Las advertencias de composición en tablas preexistentes se mantienen como limitación visual menor; la tabla nueva no presenta solapamientos.

## Hallazgos que mantienen límites o requieren evidencia adicional

- **H04 y H12:** no se recuperaron métricas por clase / fuentes de evaluación completas; no se inventaron valores ni se reentrenó.
- **H11:** se verificó documentalmente el split axial E9; no se acreditó ausencia de duplicados por contenido, no se comparó con el split histórico alternativo y el test ya se había usado en axial-full-v1.
- **H14:** faltan registros fechados de sesiones, consentimientos y autorizaciones; la resolución queda bloqueada por evidencia.
- **H31, H45, H56, H63 y H66:** se mantienen bloqueados por faltante de fuente/export, consentimiento, derechos/licencias, origen de máscaras/conteos o metadatos de entrevistas, según el detalle por ID en la matriz.
- **H67 y otros hallazgos de investigación:** permanecen abiertos hasta completar la verificación bibliográfica y documental correspondiente.

Los repositorios Backend, Frontend y AI Module se conservaron en sus snapshots locales declarados y se inspeccionaron sin modificaciones. Los commits de código no son necesarios para las correcciones actuales, que son documentales. No se hizo push, merge, publicación remota, edición de Google Docs ni contacto con el tutor. El cierre definitivo y cualquier publicación quedan sujetos a la conformidad del usuario cuando los bloqueos restantes se resuelvan.
