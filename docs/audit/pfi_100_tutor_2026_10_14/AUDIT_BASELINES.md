# Baselines de la auditoría PFI

Inventario G0 verificado el 14/10/2026. Los checkouts habituales no fueron modificados. Cada worktree parte del SHA local confirmado; no se sincronizaron ramas con remotos.

| Repositorio | Ruta local | Rama base | SHA base | Rama audit local | SHA de contenido auditado al G3 | Cambios locales previos | Pruebas disponibles |
|---|---|---|---|---|---|---|---|
| Gestionador LaTeX | `C:\Users\enzoa\OneDrive\Documentos\1.ReposGitHub-Backends\GestionadorLatex-Enzo_PFI_SEGUNDA_ENTREGA_WORK` | `audit/pfi-2026-modelo-financiero-documental` | `0454dc38ce0e12c3267e73b5fcb4b852c3cfde89` | `audit/pfi-100-tutor-2026-10-14` | `643e657502440e933c59f1356e3beae1edd5df44` | limpio en G0; correcciones locales trazadas en la matriz | pdfLaTeX + Biber; compilación final exitosa, log preservado |
| Backend | `C:\Users\enzoa\OneDrive\Documentos\1.ReposGitHub-Backends\PFI_MVP_Juntos\PFI_MVPTest_Enzo_Backend_final_integration` | `integration/final-2026` (snapshot local) | `9bca0532cc3f2541337e5e395f98cc37a30f7fb8` | `audit/pfi-100-tutor-2026-10-14` | `9bca0532cc3f2541337e5e395f98cc37a30f7fb8` | limpio; snapshot inspeccionado sin cambios | `mvn test` (no ejecutado; sin cambio de código) |
| Frontend | `C:\Users\enzoa\OneDrive\Documentos\1.ReposGitHub-Backends\PFI_MVP_Juntos\PFI_MVPTest_Enzo_Frontend_final_integration` | `integration/final-2026` | `5ec83e15aafd13ae3d944178a4f9f169a76eb3f7` | `audit/pfi-100-tutor-2026-10-14` | `5ec83e15aafd13ae3d944178a4f9f169a76eb3f7` | limpio; snapshot inspeccionado sin cambios | `npm test`, `npm run build`, `npm run lint`, `npm run typecheck` (no ejecutados; sin cambio de código) |
| AI Module | `C:\Users\enzoa\OneDrive\Documentos\1.ReposGitHub-Backends\PFI_MVP_Juntos\PFI_MVPTest_Enzo_AImodule_final_integration` | `integration/final-2026` | `d363113d46284205233aede3f1f48e32b7ebf186` | `audit/pfi-100-tutor-2026-10-14` | `d363113d46284205233aede3f1f48e32b7ebf186` | limpio; snapshot inspeccionado sin cambios | `python -m pytest --cov` (no ejecutado; sin cambio de código) |

Los cuatro worktrees de auditoría están bajo `C:\Users\enzoa\OneDrive\Documentos\1.ReposGitHub-Backends\PFI_MVP_Juntos\_worktrees_auditoria_pfi_100\` (`latex`, `backend`, `frontend`, `ai-module`). El snapshot de Backend es deliberadamente el SHA local provisto; no incluye el commit que su referencia remota local indicaba como posterior.

El SHA de LaTeX de la tabla identifica el último commit de contenido evaluado; los commits posteriores de empaquetado de evidencia/informe pueden avanzar la rama sin modificar ese contenido. Los SHAs de Backend, Frontend y AI Module permanecen en los snapshots de integración declarados. No se ejecutaron pruebas de producto porque esos repositorios no recibieron cambios de código.
