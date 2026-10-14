# Auditoría integral de observaciones del tutor — PFI 100 % (14/10/2026)

> **Documento listo para dar a Codex en el workspace local que contiene los cuatro repositorios del PFI.**
> 
> **Regla primordial:** toda auditoría y sus commits se realizan **localmente, aislados de las ramas compartidas**. No hacer `push`, PR, merge, rebase, publicación, edición del Google Docs compartido ni comunicación con el tutor hasta completar y revisar el cierre.

## 0. Contexto y objetivo

El tutor entregó `Hallazgos_PFI_revision.xlsx`: 67 observaciones, clasificadas en 19 de prioridad alta, 42 media y 6 baja. Debe usarse como **entrada inalterable** de la auditoría; sus observaciones no se sustituyen ni se borran. También se entrega `MATRIZ_SEGUIMIENTO_AUDITORIA_PFI_100_2026.xlsx`, una matriz operativa nueva que incluye la transcripción de los 67 registros y columnas de estado, evidencia, repositorios, pruebas y commits. **Todos los hallazgos arrancan `Sin revisar`**: ninguna corrección anterior se presume resuelta sin cotejar el estado actual.

El PFI contiene cuatro repositorios de trabajo que conviven en una carpeta contenedora local: (1) Gestionador LaTeX del documento, (2) Backend Spring Boot, (3) Frontend y (4) AI Module / FastAPI. Puede haber otros elementos en ese directorio: no modificarlos. La rama remota documental conocida a fecha 14/10/2026 es `audit/pfi-2026-modelo-financiero-documental`, cuyo commit observado es `0454dc38ce0e12c3267e73b5fcb4b852c3cfde89`; **confirmar el commit realmente presente en el checkout antes de usarlo como baseline**. No asumir que `main`, `master` o ramas `research/*` contienen automáticamente la versión correcta del producto.

El objetivo es preparar un **cierre académico verificable**, de modo que cada una de las 67 observaciones tenga (i) diagnóstico, (ii) decisión técnicamente defendible, (iii) cambio mínimo o justificación de no aplicabilidad, (iv) evidencia, (v) pruebas/compilación y (vi) commit local trazable. La finalidad es corregir problemas reales, no cambiar estados artificialmente para dar 67/67.

## 1. Restricciones innegociables

1. **No modificar ni comunicar al tutor** el Google Docs compartido durante la ejecución local. El documento de LaTeX y el PDF compilado son el artefacto académico que se audita; Google Docs es una versión complementaria que se sincronizará posteriormente y de forma controlada. Registrar diferencias sin corregirlas silenciosamente.
2. **No hacer `git push`, PR, merge, rebase, force-push ni alterar `main`/`master`.** Commits locales sí, únicamente en ramas de auditoría aisladas. Al final mostrar el plan de publicación y obtener conformidad para publicarlo.
3. **No tocar trabajo ajeno ni archivos preexistentes sin seguimiento.** No ejecutar `git reset --hard`, `git clean`, borrados globales ni `git stash` automático. No reescribir historial.
4. No inventar métricas, evidencia clínica, tiempos de inferencia, salidas de pruebas, resultados financieros, procedencia de etiquetas, licencias, profesionales participantes ni validaciones. Mantener intactas las transcripciones literales.
5. No ejecutar entrenamientos costosos ni crear infraestructura Cloud facturable para cerrar observaciones sin autorización explícita. Sí se permiten inspecciones estáticas, pruebas locales y reconstrucción reproducible de evidencia existente.
6. Distinguir rigurosamente: **código implementado**, **integrado**, **habilitado**, **demostrado con fixtures**, **probado con stack local real**, **E2E base Cloud V2 con datos sintéticos**, **validación profesional cualitativa** y **validación clínica independiente no ejecutada**.
7. Los diagramas, screenshots, logo y cifras financieras actuales requieren contrastes propios. No sustituir diagramas o cifras por contenido inventado; registrarlos como abiertos mientras falte el insumo verificable.
8. Respetar contratos y arquitectura entre los tres repositorios de software; no introducir cambios funcionales para tapar observaciones puramente documentales.
9. Conservar el Excel original **byte por byte**, registrar su `SHA256` y no editarlo. Hash de referencia de la copia entregada en este paquete: `ccbd9af2f9d64c76b51e8d9c4d7a46a0831e1fb7b6a5714b9a6d536f521f1790`. Si el hash de la copia local difiere, investigar antes de seguir.
10. Para el texto final, no hablar como si «faltara la próxima entrega»; describir **qué se implementó, qué se comprobó y qué quedó como límite del alcance efectivamente ejecutado**, sin ocultar carencias.

## 2. Etapa G0 — Inventario y aislamiento (obligatoria antes de editar)

- Partir de la **carpeta padre que contiene los cuatro repositorios**. Descubrirlos por sus `.git`, nombre, URL de remoto y estructura. No adivinar rutas ni mover directorios. No confundir un directorio auxiliar con un repositorio del producto.
- Por **cada** repositorio registrar: ruta, remoto, rama y HEAD, `git status --short`, archivos ignorados relevantes, commits recientes, tags de freeze e indicación de cómo probarlo. Localizar cambios sin commit y dos o más archivos no rastreados preexistentes: **no tocarlos**.
- Resolver y documentar la línea base apropiada de cada repositorio a partir del estado realmente aprobado del PFI. Para LaTeX, contrastar `0454dc3` con el HEAD actual; para backend/frontend/IA no asumir que las ramas antiguas son actuales. Si hay ambigüedad que pueda destruir trabajo, no alterar ese repositorio y consignar el bloqueo.
- Preferir `git worktree` en un subdirectorio **separado del checkout habitual** (por ejemplo, `../_worktrees_auditoria_pfi_100/<repo>/`) y crear la rama local `audit/pfi-100-tutor-2026-10-14` desde el baseline verificado. Esta forma evita cambiar las ramas que el equipo usa diariamente. Si ya existe, reutilizarla tras verificar su base; no sobrescribirla.
- Documentar en `AUDIT_BASELINES.md` una tabla `Repositorio | Ruta local | Rama base | SHA base | Rama audit local | SHA audit actual | Estado de cambios no rastreados | Pruebas disponibles`.

## 3. Etapa G0.1 — Primer commit local exclusivamente documental

Dentro del worktree de auditoría del **Gestionador LaTeX**, crear el directorio canónico:

`docs/audit/pfi_100_tutor_2026_10_14/`

Copiar allí **sin modificaciones** los siguientes archivos proporcionados:

- `Hallazgos_PFI_revision.xlsx` — **fuente original del tutor; inmutable**.
- `MATRIZ_SEGUIMIENTO_AUDITORIA_PFI_100_2026.xlsx` — copia operativa, estados iniciales «Sin revisar».
- Este archivo `PROTOCOLO_Y_PROMPT_CODEX_AUDITORIA_TUTOR_PFI_100_2026.md` — procedimiento completo.
- `PLANTILLA_INFORME_CIERRE_AUDITORIA_PFI_100_2026.md` — estructura del informe final.

Agregar un `README.md` que identifique la fuente, el SHA256 y la fecha de corte, aclarando «**auditoría en desarrollo; no publicada**». Agregar `AUDIT_BASELINES.md` con los 4 SHAs. Hacer **un commit local** limitado a esos archivos, por ejemplo:

`audit(pfi): registrar hallazgos originales del tutor y matriz de seguimiento`

**DETENERSE ANTES DE TODO PUSH.** No modificar todavía los otros tres repositorios, salvo preparar worktrees locales seguros. No subir el Excel ni siquiera a una rama remota «privada»: el repositorio documental es público y una rama remota también puede quedar visible.

## 4. Etapa G1 — Investigación exhaustiva, hallazgo por hallazgo

Procesar los IDs `1` a `67` tal como aparecen en el Excel. Priorizar altos, después medios y bajos, sin descartar ninguna fila. Pueden agruparse por subsistema, pero el registro **siempre es uno por ID** y cada celda debe poder auditarse. Por cada registro:

1. Leer el **texto literal** del hallazgo, prioridad, ubicación y sugerencia del tutor. No reescribir la observación original.
2. Buscar la situación real en: fuente `*.tex`, `main.tex`, PDF compilado, bibliografía, evidencia de experimentos, tres repositorios de producto y documentos de pruebas existentes. Distinguir el documento que el tutor auditó de la versión posterior (219 páginas según el reporte local; confirmar PDF y log).
3. Clasificar `¿Confirmado?` como `Sí`, `No`, `Parcial` o `No aplica`, siempre con prueba y motivo. Si ya fue corregido por commits anteriores, marcar `Ya resuelto`, adjuntar commit/ruta y comprobar el PDF actual.
4. Asignar `Frente`, `Repositorio(s)`, `Ruta / sección`, `Evidencia verificable`, `Corrección o justificación`, y señalar qué otras filas dependen de la misma corrección.
5. Identificar si el hallazgo pide: corrección editorial (ortografía, título, número, duplicación, referencia cruzada); sincronización de fuentes; evidencia de QA; reconstrucción científica/metodológica; cambios funcionales; nuevo gráfico; reconciliación económica; o redefinición de alcance. **No tratar todo como redacción.**
6. Si un hallazgo es incorrecto, redundante o ya no aplicable: registrar la justificación específica con evidencia. No desacreditar la revisión del tutor ni borrar la fila.
7. Si faltan datos o validación real para resolverlo, dejar `Bloqueado por evidencia` y especificar qué falta. Nunca considerar `Bloqueado` un cierre.

Casos de prioridad crítica entre los IDs altos: **#1 y #2** (portada/abstract y conclusiones generales), **#3** (4 figuras sin insertar), **#4** (taxonomía y Dice axial), **#5/#6** (modelo de hallazgos y origen de etiquetas), **#7/#8** (alcance E2E y estados), **#9** (Patient frente a `subjectRef`), **#10** (componentes no definidos en alcance), **#11** (partición del modelo axial). Revisar los restantes 56 con idéntico rigor; no limitar la auditoría a estos ejemplos.

## 5. Etapa G2 — Correcciones mínimas y commits temáticos locales

- Antes de cada modificación, conservar una referencia al texto original y definir criterios de aceptación verificables.
- Cambiar solo lo necesario para resolver el problema; **no alterar sustancialmente el alcance, resultados, modelos, contratos ni arquitectura** sin justificación y evidencia.
- Para LaTeX, usar referencias automáticas `\label`, `\ref`, `\autoref` o equivalente; no hardcodear números ni páginas. Vigilar diferencia de numeración entre Google Docs y LaTeX, especialmente tabla profesional 13.5 (Docs) frente a 13.7 (LaTeX, por dos tablas Cloud adicionales).
- Si la evidencia exige actualizar código, hacerlo en la **rama local de auditoría del repositorio responsable**, con pruebas apropiadas. Documentar el vínculo con el ID original y la compatibilidad de contratos. No desplegar a Cloud.
- Commits locales **pequeños y temáticos**: `audit(pfi): resolver H04 taxonomía del Dice axial`, `docs(pfi): corregir H08 estados de validación`, etc. Registrar SHA local en la fila correspondiente. No agrupar indiscriminadamente los 67 hallazgos en un solo commit.
- Si una corrección afecta a dos repositorios, registrar los dos SHAs y su dependencia. No modificar código solo porque existe una carpeta de backend/frontend/IA: primero demostrar que es necesario.
- Cada vez que se cierre un bloque, verificar que el PDF, las referencias cruzadas, las tablas de trazabilidad y la matriz se correspondan. Guardar evidencia sanitizada bajo `docs/audit/pfi_100_tutor_2026_10_14/evidencias/` (no incluir datos médicos identificables, secretos o archivos de gran tamaño).

## 6. Significado formal de los estados de la matriz

- **Sin revisar:** sin análisis propio.
- **En investigación:** se analiza el contraste.
- **Confirmado:** observación reproducida, todavía sin resolución.
- **Ya resuelto:** no se reproduce en el baseline por un cambio previo, pendiente de aceptación final.
- **Corrección aplicada:** cambio realizado localmente; aún falta alguna evidencia, revisión o prueba.
- **No aplica justificado:** se demostró que no corresponde; se registra fundamento específico, versionado y verificable.
- **Bloqueado por evidencia:** falta insumo o prueba; **no cuenta como cierre**.
- **Cerrado con evidencia:** hay prueba de resolución y QA, archivo/ruta localizable y commit registrado. Si era `Ya resuelto`, convertirlo a este estado tras verificación.

El Excel conserva en A:H el estado **histórico del tutor**. Codex actualiza únicamente I:U en `MATRIZ_SEGUIMIENTO_AUDITORIA_PFI_100_2026.xlsx`. El `Panel` computa recuentos sobre las filas reales. No escribir «67/67 resueltos» si alguna observación está bloqueada, no aplica sin fundamento o carece de QA.

## 7. Etapa G3 — Control de calidad y cierre técnico

**Obligatorio:**

- Comparar las fuentes originales con la última versión del documento PDF que realmente se genera en la rama de auditoría. No usar las páginas del Excel como offsets en `.tex` ni tomar números del índice manual de Docs como autoridad para LaTeX.
- Compilar LaTeX con **pdfLaTeX/Biber/pasadas sucesivas** según el sistema real, y conservar el log final. En Windows con MiKTeX puede no estar disponible `latexmk` por ausencia de Perl; usar el flujo directo documentado. La ausencia de referencias indefinidas debe constatarse en el log final.
- Ejecutar `git diff --check` y testear cada área de backend/frontend/IA afectada. Si no se modifica un repositorio, registrar «inspeccionado sin cambios».
- Inspeccionar numeración, índices de tablas/figuras, pies de figura, Anexos A–H, URLs/DOI, glosario, estado de validaciones y nomenclatura V1/V2 de Cloud.
- Cuantificar las 67 filas por estado, y hacer una **segunda revisión independiente** que compruebe que «resuelto» significa que el motivo del tutor ya no se reproduce. Revisar que no haya afirmaciones clínicas o económicas más fuertes que la evidencia.
- Finalizar `INFORME_CIERRE_AUDITORIA_PFI_100_2026.md` con 67 registros de `ID → estado → resumen de solución → evidencia → commit(s) → prueba`. Preparar un resumen académico neutro dirigido a lectura de docentes, sin frases «el tutor se equivocó» o «nos falta entregar».

**Puerta de cierre:** solo declarar auditoría integral terminada si **cada** fila está `Cerrado con evidencia` o `No aplica justificado` con sustento auditado, todos los QA pertinentes están aprobados y el PDF final compila sin errores de referencia. Los casos imposibles por falta de evidencia permanecen abiertos y bloquean la afirmación de cierre total; documentar su estado y dependencia real.

## 8. Etapa G4 — Publicación diferida, exclusivamente tras conformidad

- Hasta G3 concluido: **ningún push**, tampoco de las ramas de auditoría. Un repositorio público no ofrece confidencialidad a ramas remotas.
- Tras el control final, presentar al usuario: tabla por repo con rama, SHA base, lista de commits, pruebas, riesgos remanentes y documento de cierre; solicitar su conformidad para la publicación coordinada.
- Publicar entonces **solo las ramas de auditoría relevantes** y el informe final; no hacer merge automático a `main`/`master`, no forzar pushes, no tocar el Google Docs compartido sin una etapa de sincronización explícita. Si se desea que el tutor vea el resultado mediante la rama principal, esa integración debe aprobarse por separado.
- No enviar mensajes, correos o comentarios al tutor: el resultado es la documentación versionada, para que pueda consultarla cuando corresponda.

## 9. Primera ejecución concreta que quiero de Codex

**Empezá ahora con G0 y G0.1: descubrí los cuatro repositorios, verificá su estado real, creá worktrees y ramas locales aisladas, copiá el Excel original y la matriz operativa al árbol documental, validá el SHA256 y realizá el primer commit local de ingreso de auditoría. No hagas push. Luego seguí con G1: evaluá los 67 hallazgos uno por uno, actualizá sus estados y evidencia. Si algún cambio posterior es seguro y fundamentado, implementalo en G2 con commits locales, pero preservá datos y alcance. No declares auditoría final hasta superar G3. Al terminar la ejecución, entregá inventario, estado de cada hallazgo, commits locales por repositorio, verificaciones y bloqueos reales.**
