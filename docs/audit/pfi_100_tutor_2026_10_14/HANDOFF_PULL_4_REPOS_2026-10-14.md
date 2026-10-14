# Handoff para continuar la auditoría PFI desde otra computadora

**Fecha:** 14 de octubre de 2026. **Estado:** auditoría abierta; ramas de auditoría publicadas para continuar el trabajo entre equipos. Este handoff no integra las ramas en `main` ni en las ramas de integración.

## Repositorios y ramas de continuidad

Los cuatro repositorios deben clonarse desde la rama `audit/pfi-100-tutor-2026-10-14`:

| Repositorio | Remoto | SHA base publicado antes de este handoff |
|---|---|---|
| AI Module | `https://github.com/EnzoAA004/PFI_MVPTest_Enzo_AImodule.git` | `d363113d46284205233aede3f1f48e32b7ebf186` |
| Backend | `https://github.com/EnzoAA004/PFI_MVPTest_Enzo_Backend.git` | `9bca0532cc3f2541337e5e395f98cc37a30f7fb8` |
| Frontend | `https://github.com/EnzoAA004/PFI_MVPTest_Enzo_Frontend.git` | `5ec83e15aafd13ae3d944178a4f9f169a76eb3f7` |
| Gestionador LaTeX | `https://github.com/EnzoAA004/GestionadorLatex-Enzo_PFI_SEGUNDA_ENTREGA_WORK.git` | `bf25b9d65bd34d9906a3ceaf410b0c507ed3f357` |

El SHA de LaTeX de la fila es el estado que contiene la evidencia H04 y los cuatro commits de esta fase inmediatamente antes de añadir este archivo. La rama remota resultante también incluye el commit de este handoff. Para obtener el SHA exacto publicado, consultar la rama remota después del push.

## Clonar en la computadora nueva

Desde PowerShell, ejecutar los cuatro comandos desde la carpeta contenedora elegida:

```powershell
git clone --single-branch --branch audit/pfi-100-tutor-2026-10-14 https://github.com/EnzoAA004/PFI_MVPTest_Enzo_AImodule.git PFI_MVPTest_Enzo_AImodule-auditoria
git clone --single-branch --branch audit/pfi-100-tutor-2026-10-14 https://github.com/EnzoAA004/PFI_MVPTest_Enzo_Backend.git PFI_MVPTest_Enzo_Backend-auditoria
git clone --single-branch --branch audit/pfi-100-tutor-2026-10-14 https://github.com/EnzoAA004/PFI_MVPTest_Enzo_Frontend.git PFI_MVPTest_Enzo_Frontend-auditoria
git clone --single-branch --branch audit/pfi-100-tutor-2026-10-14 https://github.com/EnzoAA004/GestionadorLatex-Enzo_PFI_SEGUNDA_ENTREGA_WORK.git GestionadorLatex-Enzo_PFI_SEGUNDA_ENTREGA_WORK-auditoria
```

Al continuar después de un primer clon, en cada repositorio usar:

```powershell
git switch audit/pfi-100-tutor-2026-10-14
git pull --ff-only origin audit/pfi-100-tutor-2026-10-14
```

Antes de editar, verificar `git status --short --branch`. Para publicar avances posteriores, hacer commits pequeños en la misma rama de auditoría y usar push normal; no usar `--force`.

## Estado de la auditoría

- La matriz conserva los 67 hallazgos: 19 `Corrección aplicada`, 4 `Cerrado con evidencia`, 37 `Confirmado`, 1 `En investigación` (H67) y 6 `Bloqueado por evidencia`.
- H04 sigue parcial. El ZIP anonimizado está en `GestionadorLatex.../docs/audit/pfi_100_tutor_2026_10_14/evidencias/fuentes_h04_2026-10-14/`; las métricas sagitales por clase se presentan como históricas secundarias, no como recálculo.
- Para autenticar H04 faltan el `final_test_metrics.json` original y el checkpoint de entrenamiento identificado por SHA `fb124f0b1e73a5f3e548769bf837089295ce8e02c33fb34ed3be7fc3c2142a39`, o evidencia reproducible de equivalencia con el checkpoint runtime `cf11dcc0ad77a7c787e64a796a2fd7398ef906add461cef4b3d61f1a5238e944`.
- El PDF vigente está en `main.pdf` del repositorio LaTeX: 234 páginas físicas, SHA-256 `01aa7b349a782dc95a49d561f5c31c8ca38da6252d8e67f471936f56737512b0`.
- El Backend `integration/final-2026` local estaba un commit detrás de su rama remota al preparar este handoff. La rama de auditoría preserva el snapshot local y es el punto de continuidad; no se debe sustituir ni integrar automáticamente con la rama de integración.

## Commits locales de la última fase

- `ce505b573a17ba35129c09bee1a70e27bef2c281` — evidencia histórica H04, Anexo E, Capítulo 13 y PDF.
- `31417b38612d12a1a6deaf65347bafe124a45fbb` — resumen de estados corregido.
- `6643739fa0da765b2891737e62530efc3385f913` — evidencia, QA y commit registrados en la matriz.
- `bf25b9d65bd34d9906a3ceaf410b0c507ed3f357` — manifiesto de hashes actualizado.

La rama publicada de LaTeX añadirá además el commit que incorpora este archivo de handoff.
