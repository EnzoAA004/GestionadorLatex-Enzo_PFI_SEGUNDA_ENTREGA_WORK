# Fuentes reproducibles de las figuras de arquitectura (Capitulo 10)

Cada figura se genera con un script Python que produce primero un SVG y luego
el PNG final. `pfi_diagram.py` contiene las primitivas comunes (cajas tabulares,
cajas UML, nodos de flujo, pata de gallo, dependencias punteadas) y una funcion
`check_layout()` que aborta el render si detecta solapamientos entre cajas,
texto que desborda su caja o elementos fuera del lienzo.

## Regenerar

    pip install cairosvg pillow
    cd diagrams/architecture
    python3 fig_10_04_modelo_datos.py
    python3 fig_10_05_clases_dominio.py
    python3 fig_10_06_flujo_end_to_end.py

Cada script escribe el PNG en `images/architecture/` con el nombre que ya
referencia `chapters/capitulo_10_diseno_arquitectura.tex` y deja el SVG
intermedio junto al PNG. El proyecto LaTeX no depende de estos scripts: solo
consume los PNG versionados.

## Criterios de diseno

- Fondo blanco, tipografia sans-serif, paleta sobria y sin gradientes ni sombras.
- Ninguna figura incluye su caption dentro del bitmap.
- El tamano de fuente se mantiene cerca del 1 % del ancho del lienzo para que el
  texto siga siendo legible al insertar la figura a 0.92-0.94 \textwidth en A4.
