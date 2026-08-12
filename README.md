# Proyecto Final de Ingenieria - Documento LaTeX

Este repositorio contiene el documento LaTeX del Proyecto Final de Ingenieria:

**Prototipo de software para analisis asistido de resonancias magneticas lumbares sagitales**.

## Compilacion

Para compilar:

```bash
latexmk -pdf -use-biber main.tex
```

O alternativamente:

```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

## Estructura

- `main.tex`: archivo principal.
- `chapters/`: capitulos del documento.
- `assets/`: imagenes, diagramas y recursos graficos.
- `references.bib`: bibliografia.
- `PROMPT_CODEX_PFI_LATEX.md`: prompt de contexto y alcance utilizado para generar esta estructura.

## Estado actual

Incluye capitulos 1 a 8:

1. Introduccion
2. Planteamiento del problema
3. Justificacion
4. Objetivos
5. Alcance
6. Descripcion de la solucion propuesta
7. Estado del arte
8. Marco teorico

Pendiente de incorporar:

9. User research
10. Requerimientos del sistema
11. Diseno de la solucion y arquitectura
12. Metodologia de desarrollo
13. Cronograma del proyecto
14. Recursos, restricciones y riesgos
15. Implementacion del prototipo
16. Validacion y pruebas
17. Resultados obtenidos
18. Discusion
19. Conclusiones
20. Trabajos futuros

## Criterios importantes

- No transformar el sistema en una herramienta de diagnostico.
- Mantener la idea de software asistivo.
- Usar siempre "profesional" o "profesional del area" para referirse al usuario revisor.
- Mantener la diferencia entre medicion geometrica y conclusion clinica.
- No afirmar que el prototipo esta validado clinicamente.
- No afirmar integracion hospitalaria ni certificacion regulatoria.
- Mantener SPIDER como dataset principal del MVP.
- Dejar LumbarDISC como referencia complementaria o futura, no como dataset base del MVP.
- Preparar el documento para crecer capitulo por capitulo.
