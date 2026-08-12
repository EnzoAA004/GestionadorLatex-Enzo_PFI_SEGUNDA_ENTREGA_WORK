# Prompt para Codex / IntelliJ — Integración de capítulos 1 a 6 en proyecto LaTeX PFI

## Contexto del proyecto

Este repositorio será utilizado para generar el documento final en PDF del Proyecto Final de Ingeniería en formato LaTeX.

La tesis corresponde a un prototipo de software para análisis asistido de resonancias magnéticas lumbares sagitales. El sistema propuesto no emite diagnósticos ni reemplaza el criterio profesional. Su objetivo es asistir tareas operativas específicas: segmentación anatómica, mediciones cuantitativas simples, visualización superpuesta y generación de una salida estructurada editable revisable por el profesional.

El trabajo se desarrolla como un Proyecto Final de Ingeniería de tipo desarrollo. La solución se limita a un MVP académico, reproducible y validable técnicamente.

## Objetivo de esta tarea para Codex

Quiero que prepares o adaptes la estructura LaTeX del repositorio para incorporar los capítulos 1 a 6 del documento final de tesis:

1. Introducción
2. Planteamiento del problema
3. Justificación
4. Objetivos
5. Alcance
6. Descripción de la solución propuesta

La estructura debe quedar lista para que, en una segunda instancia, pueda incorporarse:

7. Estado del arte
8. Marco teórico

Esos capítulos 7 y 8 ya existen en otro documento y luego serán migrados a LaTeX, por lo que por ahora solo deben quedar referenciados como placeholders o comentados.

## Requisitos generales

- Usar LaTeX en español.
- Mantener una estructura modular por capítulos.
- Evitar poner todo el contenido en un único archivo `.tex`.
- Crear un archivo principal, por ejemplo `main.tex`, que invoque los capítulos con `\input{}`.
- Crear una carpeta `chapters/` para los capítulos.
- Crear una carpeta `assets/` para imágenes futuras si no existe.
- Crear un archivo de bibliografía `references.bib` aunque por ahora tenga entradas mínimas o placeholders.
- Usar una configuración compatible con compilación mediante `pdflatex` o `latexmk`.
- El documento debe poder compilar sin errores aunque los capítulos 7 y 8 todavía no estén incorporados.
- Dejar comentarios claros indicando dónde se deben agregar los capítulos 7 y 8 posteriormente.
- No inventar resultados técnicos, métricas de segmentación ni validaciones que todavía no fueron realizadas.
- Mantener el tono académico, claro y formal.

## Estructura esperada de archivos

Si el repositorio está vacío o no tiene una estructura LaTeX definida, crear algo similar a:

```text
.
├── main.tex
├── references.bib
├── README.md
├── assets/
└── chapters/
    ├── capitulo_01_introduccion.tex
    ├── capitulo_02_planteamiento_problema.tex
    ├── capitulo_03_justificacion.tex
    ├── capitulo_04_objetivos.tex
    ├── capitulo_05_alcance.tex
    └── capitulo_06_descripcion_solucion.tex
```

Si ya existe una estructura LaTeX, adaptarse a ella sin romperla, pero mantener la modularidad por capítulos.

## Configuración sugerida de `main.tex`

Usar una configuración similar a esta, ajustándola si el proyecto ya tiene una plantilla propia:

```latex
\documentclass[12pt,a4paper]{report}

\usepackage[spanish,es-tabla]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{geometry}
\usepackage{setspace}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{array}
\usepackage{hyperref}
\usepackage{csquotes}
\usepackage{enumitem}

\geometry{left=3cm,right=2.5cm,top=3cm,bottom=3cm}
\onehalfspacing

\hypersetup{
    colorlinks=true,
    linkcolor=black,
    citecolor=black,
    urlcolor=blue
}

\begin{document}

\title{Prototipo de software para análisis asistido de resonancias magnéticas lumbares sagitales}
\author{Enzo Asplanatti \\ Francisco Fabrello}
\date{2026}

\maketitle
\tableofcontents
\clearpage

\input{chapters/capitulo_01_introduccion}
\input{chapters/capitulo_02_planteamiento_problema}
\input{chapters/capitulo_03_justificacion}
\input{chapters/capitulo_04_objetivos}
\input{chapters/capitulo_05_alcance}
\input{chapters/capitulo_06_descripcion_solucion}

% Capítulos a incorporar en una segunda instancia:
% \input{chapters/capitulo_07_estado_del_arte}
% \input{chapters/capitulo_08_marco_teorico}

\bibliographystyle{plain}
\bibliography{references}

\end{document}
```

## Contenido a incorporar

A continuación se incluye el contenido base de los capítulos 1 a 6. Convertirlo a LaTeX, respetando capítulos, secciones, subsecciones, listas y énfasis académico. Corregir caracteres especiales si hace falta.

---

# Capítulo 1. Introducción

El análisis de imágenes médicas constituye una de las áreas donde la ingeniería informática ha adquirido un rol cada vez más relevante. En particular, la aplicación de técnicas de procesamiento de imágenes e inteligencia artificial permite asistir tareas vinculadas con la detección, segmentación, medición y visualización de estructuras anatómicas. Estas herramientas no buscan reemplazar el criterio profesional, sino complementar el trabajo del especialista mediante resultados cuantitativos, trazables y revisables.

Dentro de este contexto, la resonancia magnética de columna lumbar representa una modalidad de estudio ampliamente utilizada para observar estructuras anatómicas como cuerpos vertebrales, discos intervertebrales y canal espinal. La revisión de este tipo de imágenes requiere experiencia profesional, interpretación anatómica y, en muchos casos, mediciones o comparaciones visuales entre niveles. Sin embargo, parte del análisis estructural continúa dependiendo de observación manual, delimitación visual de regiones de interés y mediciones realizadas de forma no completamente automatizada.

Esta situación presenta una oportunidad de desarrollo desde la ingeniería informática: construir una herramienta que permita asistir el análisis de resonancias magnéticas lumbares sagitales mediante segmentación automática de estructuras relevantes, extracción de mediciones geométricas simples, visualización superpuesta de resultados y generación de una salida estructurada editable. El propósito no es emitir diagnósticos ni reemplazar al profesional de salud, sino ofrecer un soporte operativo que permita organizar información anatómica y cuantitativa de manera revisable.

El presente Proyecto Final de Ingeniería propone el diseño y desarrollo de un prototipo funcional de software orientado al análisis asistido de resonancias magnéticas lumbares sagitales. El sistema se plantea como una herramienta académica y experimental que trabaja sobre imágenes de RM lumbar, segmenta estructuras anatómicas previamente definidas, obtiene mediciones cuantitativas acotadas y presenta los resultados en una interfaz que permita su revisión por parte de un profesional.

El proyecto se apoya principalmente en datasets públicos anotados, en particular SPIDER, que contiene resonancias magnéticas lumbares sagitales con máscaras de referencia para vértebras, discos intervertebrales y canal espinal. Esta decisión permite desarrollar y evaluar técnicamente el prototipo sin depender inicialmente de datos clínicos privados, favoreciendo la reproducibilidad del trabajo y reduciendo riesgos asociados al tratamiento de información sensible.

Desde el punto de vista del alcance, el prototipo se limita a una primera versión funcional o MVP. Este MVP contempla la carga y normalización de estudios, segmentación de estructuras anatómicas seleccionadas, extracción de mediciones geométricas simples, visualización superpuesta de las máscaras sobre la imagen original y generación de una salida estructurada editable. Quedan fuera del alcance el diagnóstico clínico autónomo, la recomendación terapéutica, la validación clínica multicéntrica, la integración hospitalaria completa y la certificación regulatoria.

La organización del documento sigue una progresión desde la definición del problema hacia el desarrollo y validación del prototipo. En primer lugar, se presenta el planteamiento del problema, la justificación, los objetivos, el alcance y la descripción general de la solución propuesta. Luego se desarrolla el estado del arte y el marco teórico, que fundamentan técnica y conceptualmente el proyecto. Posteriormente se incorporan el user research, los requerimientos, la arquitectura, la metodología de desarrollo, la implementación, las pruebas, los resultados y las conclusiones.

De esta manera, el trabajo busca integrar conocimientos de procesamiento de imágenes médicas, aprendizaje automático, diseño de software, interacción humano-computadora y validación técnica, dentro de un prototipo acotado y orientado a un problema concreto: asistir el análisis estructural de resonancias magnéticas lumbares sagitales mediante segmentación, medición y revisión profesional.

# Capítulo 2. Planteamiento del problema

La interpretación de resonancias magnéticas lumbares es una tarea especializada que requiere conocimiento anatómico, experiencia clínica y capacidad para analizar distintas estructuras en múltiples niveles de la columna. En el flujo habitual de revisión, el profesional debe acceder al estudio, recorrer las secuencias disponibles, identificar estructuras relevantes, observar relaciones anatómicas, detectar posibles alteraciones y, cuando corresponde, realizar mediciones o comparaciones visuales.

Aunque los sistemas actuales de visualización médica permiten acceder a las imágenes y realizar mediciones manuales, muchas tareas vinculadas con la delimitación de estructuras anatómicas y la obtención de valores cuantitativos continúan dependiendo del trabajo manual o semimanual. Esto puede generar carga operativa, variabilidad entre observadores y dificultad para obtener resultados estructurados, trazables y fácilmente reutilizables.

En el caso de las resonancias magnéticas lumbares sagitales, estructuras como cuerpos vertebrales, discos intervertebrales y canal espinal son fundamentales para el análisis anatómico. Sin embargo, su delimitación manual puede consumir tiempo y estar sujeta a diferencias de criterio. Además, cuando las mediciones no se encuentran integradas en una salida estructurada, su reutilización o revisión posterior puede depender de registros dispersos, capturas de pantalla o informes redactados manualmente.

El problema central que aborda este proyecto puede formularse de la siguiente manera:

``Existe una oportunidad de asistencia informática en el análisis estructural de resonancias magnéticas lumbares sagitales, dado que la segmentación de estructuras anatómicas, la obtención de mediciones simples y la generación de salidas revisables aún pueden requerir tareas manuales, variables y poco integradas dentro de un mismo flujo funcional.''

Este problema no implica afirmar que el profesional carezca de herramientas para analizar estudios de RM lumbar, ni que la interpretación clínica pueda automatizarse por completo. Por el contrario, el proyecto reconoce que el criterio profesional es indispensable. La dificultad se ubica en tareas operativas específicas que pueden ser asistidas por software: delimitar estructuras, calcular mediciones geométricas, visualizar resultados de manera clara y organizar una salida editable que facilite la revisión.

A partir de esta problemática, se identifican tres dimensiones principales.

En primer lugar, una dimensión operativa: el análisis manual de estructuras anatómicas puede demandar tiempo, especialmente cuando se requiere revisar varios niveles, comparar regiones o generar documentación complementaria. La automatización parcial de segmentaciones y mediciones podría reducir parte de esta carga.

En segundo lugar, una dimensión de variabilidad: las mediciones manuales o la delimitación visual de estructuras pueden diferir entre usuarios o entre distintos momentos de revisión. Un sistema asistivo no elimina la necesidad de validación profesional, pero puede ofrecer una base inicial homogénea y trazable sobre la cual el profesional intervenga.

En tercer lugar, una dimensión de documentación: los resultados generados durante la revisión de una imagen no siempre quedan estructurados de forma editable, reutilizable y vinculada con la región anatómica de origen. Una salida organizada por estructura, nivel y medición puede facilitar la trazabilidad del análisis.

Por lo tanto, el desafío de ingeniería consiste en diseñar un prototipo que integre en un mismo flujo funcional la carga de imágenes, la segmentación automática de estructuras lumbares, la derivación de mediciones geométricas, la visualización de resultados y la generación de una salida editable. Este sistema debe mantener siempre al profesional dentro del circuito de revisión, evitando presentar los resultados como diagnósticos automáticos.

La solución propuesta se diferencia de un sistema clínico completo o de un producto regulado. Su finalidad es académica y experimental. Busca demostrar la factibilidad de integrar componentes conocidos —dataset público, modelo de segmentación, métricas, mediciones, interfaz y salida estructurada— en un prototipo funcional acotado al análisis asistido de RM lumbar sagital.

# Capítulo 3. Justificación

El desarrollo del presente proyecto se justifica desde una perspectiva técnica, académica y funcional.

Desde el punto de vista técnico, la disponibilidad de datasets públicos anotados y de modelos de segmentación médica permite abordar problemas que anteriormente requerían acceso exclusivo a datos privados o infraestructura clínica compleja. En particular, el dataset SPIDER ofrece una base adecuada para entrenar o evaluar modelos de segmentación sobre resonancias magnéticas lumbares sagitales, incluyendo estructuras alineadas con el alcance del prototipo: vértebras, discos intervertebrales y canal espinal. Esto permite construir una prueba de concepto técnicamente viable y reproducible.

Además, existen arquitecturas y frameworks de aprendizaje profundo ampliamente utilizados en segmentación médica, como U-Net, nnU-Net y herramientas especializadas en imágenes biomédicas. Estos antecedentes permiten enfocar el valor del proyecto no en crear necesariamente una arquitectura completamente nueva, sino en integrar un flujo completo: carga de estudios, preprocesamiento, segmentación, medición, visualización y salida editable.

Desde el punto de vista académico, el proyecto resulta pertinente para un Proyecto Final de Ingeniería porque combina investigación aplicada, diseño de software, procesamiento de datos, inteligencia artificial, validación técnica y documentación de resultados. La propuesta no se limita a entrenar un modelo aislado, sino que busca construir un prototipo funcional con componentes articulados y verificables. Esto permite aplicar conocimientos propios de la carrera en un problema concreto y con restricciones reales.

A su vez, el proyecto se plantea dentro de límites claros. No se propone desarrollar un sistema de diagnóstico autónomo, ni una herramienta certificada para uso clínico, ni una plataforma hospitalaria completa. Esta delimitación es importante porque evita sobreprometer capacidades y permite concentrar el esfuerzo en un MVP técnicamente alcanzable: segmentar estructuras, obtener mediciones simples y presentar resultados revisables.

Desde el punto de vista funcional, la herramienta propuesta puede aportar valor como soporte al análisis estructural de RM lumbar. La segmentación automática permitiría identificar visualmente regiones de interés; las mediciones geométricas aportarían información cuantitativa derivada de las máscaras; y la salida estructurada editable permitiría organizar los resultados para revisión profesional. En todos los casos, el profesional conserva el control final sobre la interpretación, corrección y eventual descarte de los resultados.

El estado del arte muestra que existen avances relevantes en segmentación automática de columna lumbar, datasets públicos y soluciones comerciales orientadas a mediciones y reportes. Sin embargo, muchos antecedentes se concentran en componentes parciales: algunos aportan datos, otros modelos de segmentación, otros métricas de evaluación y otros productos cerrados. La brecha que justifica este PFI se encuentra en integrar esos elementos en un prototipo académico, acotado, reproducible y orientado a revisión profesional.

El proyecto también se justifica por su enfoque de trazabilidad. Cada medición generada debe estar asociada a una estructura segmentada visible, y cada resultado debe poder ser revisado por el usuario. Esta característica permite diferenciar el prototipo de una ``caja negra'' diagnóstica y orientarlo hacia una herramienta asistiva, donde la inteligencia artificial actúa como apoyo operativo.

Finalmente, la elección de trabajar inicialmente con datasets públicos reduce riesgos vinculados con privacidad y datos sensibles. Si en etapas futuras se incorporaran imágenes clínicas no públicas, deberían contemplarse procedimientos de anonimización, consentimiento y resguardo normativo. Para el alcance actual, el uso de datos públicos permite concentrar el desarrollo en la validación técnica del pipeline y en la construcción del prototipo funcional.

En síntesis, el proyecto se justifica porque aborda una necesidad real de asistencia en el análisis estructural de RM lumbar, utiliza recursos técnicos disponibles, mantiene un alcance académico responsable y propone una integración funcional que conecta segmentación, medición, visualización y revisión profesional.

# Capítulo 4. Objetivos

## 4.1 Objetivo general

Diseñar y desarrollar un prototipo funcional de software que analice resonancias magnéticas lumbares sagitales para segmentar estructuras anatómicas relevantes, obtener un conjunto acotado de mediciones cuantitativas y generar una salida visual y estructurada editable que asista al profesional sin reemplazar su criterio clínico.

## 4.2 Objetivos específicos

Para alcanzar el objetivo general, se definen los siguientes objetivos específicos:

1. Relevar antecedentes académicos, datasets públicos, herramientas abiertas y soluciones comerciales relacionadas con el análisis asistido de resonancias magnéticas lumbares.
2. Identificar la brecha funcional que justifica el desarrollo de un prototipo académico orientado a segmentación, mediciones, visualización y salida editable.
3. Definir el alcance del MVP, especificando las estructuras anatómicas contempladas, las funcionalidades incluidas y las exclusiones clínicas, técnicas y regulatorias.
4. Analizar el flujo de trabajo y las necesidades de potenciales usuarios mediante actividades de user research orientadas a profesionales vinculados con resonancias magnéticas lumbares.
5. Diseñar un pipeline de procesamiento que contemple carga, normalización, preprocesamiento, segmentación, postprocesamiento, mediciones y visualización de resultados.
6. Implementar o adaptar un modelo de segmentación para identificar estructuras anatómicas en RM lumbar sagital, priorizando vértebras, discos intervertebrales y canal espinal.
7. Desarrollar un módulo de mediciones cuantitativas simples derivadas de las máscaras de segmentación generadas por el sistema.
8. Diseñar una interfaz que permita visualizar la imagen original junto con las segmentaciones superpuestas y las mediciones asociadas.
9. Generar una salida estructurada editable que organice los resultados del sistema sin constituir un informe clínico automático.
10. Evaluar técnicamente el desempeño del prototipo mediante métricas de segmentación y comparación contra anotaciones de referencia del dataset utilizado.
11. Complementar la validación técnica con una revisión cualitativa profesional orientada a valorar plausibilidad anatómica, utilidad de las mediciones, claridad visual y legibilidad de la salida generada.
12. Documentar las decisiones de diseño, limitaciones, resultados obtenidos y posibles líneas de trabajo futuro.

# Capítulo 5. Alcance

El alcance del proyecto se define en función de un MVP académico orientado al análisis asistido de resonancias magnéticas lumbares sagitales. El sistema propuesto no busca reemplazar el criterio profesional ni emitir diagnósticos, sino automatizar tareas operativas específicas vinculadas con segmentación, medición, visualización y documentación estructurada.

## 5.1 Funcionalidades incluidas

El proyecto incluye el diseño y desarrollo de un prototipo funcional con las siguientes capacidades:

- Carga de estudios de RM lumbar sagital provenientes de datasets públicos o fuentes compatibles con el entorno de desarrollo.
- Normalización y preprocesamiento de las imágenes para su uso dentro del pipeline.
- Segmentación automática de un conjunto acotado de estructuras anatómicas.
- Visualización de las máscaras generadas sobre la imagen original.
- Extracción de mediciones geométricas simples derivadas de las segmentaciones.
- Organización de resultados por estructura anatómica y, cuando sea posible, por nivel lumbar.
- Generación de una salida estructurada editable para revisión profesional.
- Evaluación técnica de las segmentaciones mediante métricas cuantitativas.
- Revisión cualitativa complementaria por parte de un profesional del área.

## 5.2 Estructuras anatómicas contempladas

El MVP se concentrará en tres estructuras anatómicas principales:

- cuerpos vertebrales;
- discos intervertebrales;
- canal espinal.

Estas estructuras se seleccionan porque se encuentran alineadas con el dataset público definido como base del proyecto y porque permiten derivar mediciones geométricas simples que pueden ser revisadas visualmente.

## 5.3 Mediciones contempladas

Las mediciones incluidas serán acotadas y de naturaleza geométrica. Podrán incluir, según la calidad de las máscaras obtenidas y la información espacial disponible:

- áreas proyectadas de estructuras segmentadas;
- dimensiones relativas de discos intervertebrales;
- medidas aproximadas asociadas al canal espinal en el plano sagital;
- relaciones o comparaciones simples entre niveles.

Estas mediciones no serán interpretadas automáticamente como diagnósticos. Por ejemplo, una reducción de dimensión o área no será clasificada por el sistema como patología, sino presentada como dato cuantitativo revisable.

## 5.4 Validación incluida

La validación se desarrollará en dos niveles.

En primer lugar, se realizará una validación técnica cuantitativa, comparando las máscaras generadas por el sistema contra anotaciones de referencia disponibles en el dataset utilizado. Para ello podrán emplearse métricas como Dice, IoU, distancia de Hausdorff o métricas de superficie, según corresponda.

En segundo lugar, se realizará una validación cualitativa complementaria con un profesional vinculado al análisis de imágenes médicas. Esta revisión se orientará a evaluar la plausibilidad anatómica de las segmentaciones, la utilidad de las mediciones, la claridad de la visualización y la legibilidad de la salida estructurada editable.

## 5.5 Exclusiones del alcance

Quedan fuera del alcance del proyecto:

- diagnóstico clínico automático;
- clasificación integral de patologías degenerativas;
- recomendación terapéutica;
- reemplazo del criterio médico;
- uso clínico real del sistema;
- validación clínica multicéntrica;
- integración completa con sistemas hospitalarios;
- integración PACS/RIS obligatoria;
- certificación regulatoria como software médico;
- comparación longitudinal obligatoria entre estudios de un mismo paciente;
- entrenamiento sobre datos privados no anonimizados;
- desarrollo de un producto comercial final.

Estas exclusiones permiten mantener el proyecto dentro de un alcance académico realista y técnicamente verificable.

## 5.6 Alcance del documento final

El documento final abarcará la fundamentación del problema, estado del arte, marco teórico, user research, requerimientos, arquitectura, metodología de desarrollo, cronograma, implementación, validación, resultados, discusión, conclusiones y trabajos futuros. La documentación buscará dejar trazabilidad entre las decisiones de diseño y los resultados obtenidos durante el desarrollo del prototipo.

# Capítulo 6. Descripción de la solución propuesta

La solución propuesta consiste en un prototipo funcional de software para el análisis asistido de resonancias magnéticas lumbares sagitales. El sistema recibirá como entrada una imagen o serie de RM lumbar, aplicará un pipeline de procesamiento para segmentar estructuras anatómicas relevantes, obtendrá mediciones cuantitativas simples a partir de las máscaras generadas y presentará los resultados en una interfaz visual y una salida estructurada editable.

La solución se plantea como una herramienta de asistencia. Esto significa que el sistema no emitirá diagnósticos, no clasificará patologías de manera autónoma y no recomendará tratamientos. Su función será asistir tareas operativas: delimitar estructuras, calcular valores geométricos, visualizar resultados y organizar información para revisión.

## 6.1 Flujo general del sistema

El flujo general del prototipo puede describirse en las siguientes etapas:

1. Carga del estudio: el usuario incorpora una RM lumbar sagital compatible con el sistema o selecciona un estudio previamente disponible dentro del entorno de prueba.
2. Normalización y preprocesamiento: la imagen se prepara para su análisis mediante procedimientos como ajuste de formato, normalización de intensidades, reorientación, remuestreo o recorte, según las necesidades del modelo utilizado.
3. Segmentación anatómica: el sistema aplica un modelo de segmentación para identificar las estructuras contempladas en el MVP: vértebras, discos intervertebrales y canal espinal.
4. Postprocesamiento: las máscaras generadas se procesan para mejorar su consistencia, separar componentes, organizar estructuras y preparar la información para mediciones y visualización.
5. Extracción de mediciones: a partir de las máscaras se calculan mediciones geométricas simples, tales como áreas proyectadas, dimensiones relativas o relaciones entre estructuras.
6. Visualización superpuesta: la interfaz presenta la imagen original junto con las máscaras segmentadas, permitiendo al usuario revisar visualmente los resultados.
7. Revisión profesional: el usuario puede aceptar, observar, corregir o descartar resultados. Esta etapa mantiene al profesional dentro del circuito de decisión.
8. Salida estructurada editable: el sistema genera una plantilla organizada con los resultados obtenidos, incluyendo estructuras, mediciones, unidades, observaciones y estado de revisión.

## 6.2 Módulo de entrada y preprocesamiento

El módulo de entrada tendrá como finalidad cargar las imágenes que serán analizadas por el prototipo. En una primera etapa, el sistema trabajará con datos provenientes de datasets públicos anotados, priorizando aquellos que permitan evaluar segmentaciones contra máscaras de referencia.

El preprocesamiento buscará homogeneizar la información de entrada para facilitar la aplicación del modelo de segmentación. Debido a que las imágenes de resonancia magnética pueden presentar variabilidad de intensidad, resolución, orientación y formato, esta etapa resulta fundamental para obtener resultados consistentes.

Entre las tareas posibles se incluyen normalización de intensidades, ajuste de dimensiones, conversión de formato, remuestreo espacial y preparación de tensores de entrada para el modelo. Las transformaciones aplicadas deberán documentarse para asegurar trazabilidad y reproducibilidad.

## 6.3 Módulo de segmentación

El módulo de segmentación será responsable de identificar automáticamente las estructuras anatómicas definidas en el alcance. Para ello se implementará o adaptará un modelo de aprendizaje profundo orientado a segmentación de imágenes médicas.

El sistema podrá utilizar como referencia arquitecturas ampliamente empleadas en este campo, tales como U-Net, nnU-Net u otros enfoques compatibles con el dataset y las restricciones de hardware disponibles. La elección final dependerá de la factibilidad de entrenamiento, disponibilidad de recursos, rendimiento obtenido y facilidad de integración con el resto del prototipo.

La salida principal de este módulo será una máscara anatómica o conjunto de máscaras que indiquen las regiones correspondientes a vértebras, discos intervertebrales y canal espinal. Estas máscaras serán utilizadas posteriormente para visualización, mediciones y evaluación técnica.

## 6.4 Módulo de mediciones cuantitativas

El módulo de mediciones utilizará las máscaras generadas para obtener valores geométricos simples. La finalidad de estas mediciones será aportar información cuantitativa de apoyo, no establecer diagnósticos clínicos.

Cada medición deberá estar asociada a una estructura segmentada visible y, cuando corresponda, a un nivel anatómico. Además, deberá indicarse la unidad utilizada y conservarse la relación con la imagen y la máscara de origen.

Las mediciones podrán incluir áreas proyectadas, dimensiones relativas de discos, medidas asociadas al canal espinal en el plano sagital y comparaciones simples entre estructuras. La selección definitiva de mediciones dependerá de la calidad de las máscaras, la información espacial disponible y la validación profesional.

## 6.5 Módulo de visualización

El módulo de visualización permitirá observar la imagen original junto con las segmentaciones superpuestas. Esta funcionalidad resulta esencial porque permite revisar visualmente la plausibilidad anatómica de los resultados.

La interfaz deberá permitir diferenciar las estructuras segmentadas, activar o desactivar capas, consultar mediciones asociadas y revisar los resultados generados por el sistema. El diseño se orientará a claridad y revisión, no a reemplazo del visor médico profesional.

La visualización superpuesta también servirá como soporte para la validación cualitativa, ya que el profesional podrá evaluar si los contornos generados resultan razonables, si las estructuras están correctamente representadas y si la información presentada es comprensible.

## 6.6 Módulo de salida estructurada editable

La salida estructurada editable será una plantilla generada a partir de los resultados del sistema. Esta salida podrá incluir datos como estructura anatómica, nivel, medición, unidad, observación y estado de revisión.

Su carácter editable es fundamental. El usuario debe poder corregir valores, agregar comentarios, descartar mediciones o indicar que un resultado requiere revisión. De esta forma, la salida no se presenta como informe clínico cerrado, sino como un documento de apoyo generado automáticamente y supervisado por el profesional.

Este módulo representa uno de los aportes principales del prototipo, porque conecta los resultados técnicos del modelo con una forma de documentación revisable y trazable.

## 6.7 Rol del profesional

El prototipo se diseñará bajo un enfoque de humano en el circuito. El sistema propone resultados, pero el profesional conserva la decisión final. Esta decisión de diseño responde tanto a razones éticas como técnicas: las segmentaciones automáticas pueden presentar errores, las mediciones requieren interpretación contextual y el alcance del proyecto no contempla diagnóstico autónomo.

El profesional podrá intervenir revisando la segmentación, evaluando mediciones, modificando la salida editable y aportando observaciones. De esta manera, la inteligencia artificial funciona como soporte operativo y no como reemplazo del juicio experto.

## 6.8 Resultado esperado del MVP

El resultado esperado es un prototipo capaz de ejecutar un flujo completo sobre RM lumbar sagital: cargar una imagen, procesarla, segmentar estructuras anatómicas, generar mediciones, visualizar resultados y producir una salida editable.

El éxito del MVP no dependerá únicamente de alcanzar métricas elevadas de segmentación, sino de demostrar una integración funcional coherente entre los módulos. La validación deberá considerar tanto el rendimiento técnico como la utilidad percibida del flujo propuesto.

En consecuencia, la solución propuesta se ubica en un punto intermedio entre la investigación algorítmica y el desarrollo de software aplicado. No se limita a evaluar un modelo, pero tampoco pretende convertirse en un producto clínico final. Su aporte consiste en construir una herramienta académica, trazable y revisable que permita explorar la asistencia informática en el análisis estructural de resonancias magnéticas lumbares sagitales.

## Transición hacia capítulos 7 y 8

Una vez definido el problema, los objetivos, el alcance y la solución propuesta, resulta necesario analizar qué antecedentes existen en relación con el análisis asistido de resonancias magnéticas lumbares, la segmentación automática de estructuras anatómicas, las mediciones cuantitativas derivadas de máscaras y las herramientas de revisión profesional. Por este motivo, el siguiente capítulo desarrolla el estado del arte, con el fin de identificar datasets, modelos, soluciones comerciales y brechas funcionales relevantes para el presente proyecto.

Posteriormente, el marco teórico establecerá los conceptos necesarios para comprender el diseño del prototipo: resonancia magnética lumbar, anatomía relevante, representación computacional de imágenes médicas, segmentación, aprendizaje supervisado, métricas de evaluación, visualización, salida estructurada e inteligencia artificial asistiva.

---

## Referencias mínimas sugeridas para `references.bib`

Crear `references.bib` con estas entradas mínimas. Se podrán completar más adelante cuando se integren estado del arte y marco teórico.

```bibtex
@misc{asplanatti_fabrello_propuesta_2026,
  author = {Asplanatti, Enzo and Fabrello, Francisco},
  title = {Propuesta PFI 2026: Segmentación de RM lumbar},
  year = {2026},
  note = {Documento interno de Proyecto Final de Ingeniería}
}

@article{vandergraaf_spider_2024,
  author = {van der Graaf, Jasper W. and others},
  title = {Lumbar spine segmentation in MR images: a dataset and a public benchmark},
  journal = {Scientific Data},
  volume = {11},
  number = {264},
  year = {2024},
  doi = {10.1038/s41597-024-03090-w}
}

@article{isensee_nnunet_2021,
  author = {Isensee, Fabian and Jaeger, Paul F. and Kohl, Simon A. A. and Petersen, Jens and Maier-Hein, Klaus H.},
  title = {nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation},
  journal = {Nature Methods},
  volume = {18},
  pages = {203--211},
  year = {2021},
  doi = {10.1038/s41592-020-01008-z}
}
```

## README sugerido

Crear o actualizar `README.md` con instrucciones breves:

```markdown
# Proyecto Final de Ingeniería — Documento LaTeX

Este repositorio contiene el documento LaTeX del Proyecto Final de Ingeniería:

**Prototipo de software para análisis asistido de resonancias magnéticas lumbares sagitales**.

## Compilación

Para compilar:

```bash
latexmk -pdf main.tex
```

O alternativamente:

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Estructura

- `main.tex`: archivo principal.
- `chapters/`: capítulos del documento.
- `assets/`: imágenes, diagramas y recursos gráficos.
- `references.bib`: bibliografía.

## Estado actual

Incluye capítulos 1 a 6:

1. Introducción
2. Planteamiento del problema
3. Justificación
4. Objetivos
5. Alcance
6. Descripción de la solución propuesta

Pendiente de incorporar:

7. Estado del arte
8. Marco teórico
9. User research
10. Requerimientos del sistema
11. Diseño de la solución y arquitectura
12. Metodología de desarrollo
13. Cronograma del proyecto
14. Recursos, restricciones y riesgos
15. Implementación del prototipo
16. Validación y pruebas
17. Resultados obtenidos
18. Discusión
19. Conclusiones
20. Trabajos futuros
```

## Criterios importantes

- No transformar el sistema en una herramienta de diagnóstico.
- Mantener la idea de software asistivo.
- Usar siempre “profesional” o “profesional del área” para referirse al usuario revisor.
- Mantener la diferencia entre medición geométrica y conclusión clínica.
- No afirmar que el prototipo está validado clínicamente.
- No afirmar integración hospitalaria ni certificación regulatoria.
- Mantener SPIDER como dataset principal del MVP.
- Dejar LumbarDISC como referencia complementaria o futura, no como dataset base del MVP.
- El documento debe quedar preparado para crecer capítulo por capítulo.
