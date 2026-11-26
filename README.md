# doc_tesis

English version: [docs/en/README.md](docs/en/README.md).

Fuente en LaTeX del trabajo de titulación «Navegación y exploración autónoma de interiores utilizando un robot móvil de tracción diferencial», para optar al título de Ingeniero Civil Electrónico en la Universidad Tecnológica Metropolitana (UTEM), Santiago, Chile, 2026.

## Para quién

Para la comisión evaluadora y cualquier persona que quiera leer la tesis, y para el autor, que reúne aquí la tesis y el material de su defensa.

## Cómo usarlo

Para leerla, abre el PDF entregado: `docs/submitted/thesis-corrected-v2.pdf`. La presentación y el guion de la defensa están en `docs/defense/`. Los archivos pesados se guardan con Git LFS, así que después de clonar corre `git lfs pull`.

Para compilarla necesitas una distribución de TeX con XeLaTeX, biber y makeglossaries (MiKTeX o TeX Live), más las fuentes Arial y TeX Gyre Pagella. Desde la raíz del repositorio:

```bash
latexmk -r content/latexmkrc -cd content/main.tex
```

`content/latexmkrc` elige XeLaTeX y corre biber y makeglossaries. El PDF queda junto al archivo principal, como main.pdf dentro de content/. Dentro de content/ basta con `latexmk main.tex`, porque latexmk lee el latexmkrc de la carpeta donde corre.

## Cómo funciona

`docs/how-it-works.md` explica el flujo completo de principio a fin, cada parte con su ruta, por dónde empezar a leer y cómo comprobar que funciona.

## Estado

Entregada y corregida según las observaciones de la comisión. Defendida y aprobada el 25 de noviembre de 2026, con nota final 6,7: 6,6 en el documento y 6,8 en la presentación.

## Estructura

- `content/`: el texto del documento. `main.tex`, luego `front/` (de la portada al resumen), `chapters/` (capítulos 01 a 07) y `back/` (glosario y anexo).
- `figures/`: las figuras con sus fuentes, como el `.pptx` o `.fzz` junto a la imagen exportada. Una carpeta por capítulo (de `03-implemented-solution/` a `06-results/`, más `appendix/`), según el primer capítulo que usa la figura.
- `bibliography/`: las referencias, citadas en estilo APA con biblatex.
- `templates/`: el logo de la UTEM que usa la portada.
- `docs/`: objetivos, glosario, supuestos, decisiones y especificaciones, más `defense/` (material de la defensa) y `submitted/` (PDF entregado).

## Cómo contribuir

Las tareas usan el formulario de issue Task. Los pull requests siguen `.github/pull_request_template.md`. Las reglas para personas y herramientas de IA están en `AGENTS.md`.

## Estándar

Este repositorio sigue `SVN11X/standards@v1` con el perfil `docs`. `AGENTS.md` se genera automáticamente, así que no lo edites a mano. Para regenerarlo o correr el chequeo en tu equipo:

```bash
pip install pyyaml
git clone --depth 1 --branch v1 https://github.com/SVN11X/standards .standards
python .standards/scripts/standard.py agents .
python .standards/scripts/standard.py check .
```

## Licencia

[CC BY 4.0](LICENSE): puedes compartir y adaptar el material, incluso con fines comerciales, siempre que cites al autor.
