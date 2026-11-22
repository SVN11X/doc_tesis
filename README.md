# doc_tesis

The LaTeX source of the undergraduate thesis «Navegación y exploración autónoma de interiores utilizando un robot móvil de tracción diferencial», for the degree of Ingeniero Civil Electrónico at Universidad Tecnológica Metropolitana (UTEM), Santiago, Chile, 2026. The thesis is written in Spanish.

## For whom

The examining committee and anyone who wants to read the thesis, and the author, who keeps the thesis and its defense material in one place.

## Use it

To read it, open the submitted PDF: `docs/submitted/thesis-corrected-v2.pdf`. The defense slides and script are in `docs/defense/`. The large files are stored with Git LFS, so run `git lfs pull` after cloning.

To build it you need a TeX distribution with XeLaTeX, biber and makeglossaries (MiKTeX or TeX Live), plus the Arial and TeX Gyre Pagella fonts. From the repository root:

```bash
latexmk -r content/latexmkrc -cd content/main.tex
```

`content/latexmkrc` selects XeLaTeX and runs biber and makeglossaries. The PDF is written next to the main file, as main.pdf in content/. Inside content/, `latexmk main.tex` is enough, since latexmk reads the latexmkrc of the folder it runs in.

## How it works

`docs/how-it-works.md` explains the main flow from start to finish, each part with its path, where to start reading the code and how to check that it works.

## Status

Submitted and corrected after the committee's observations. Defense in preparation.

## Layout

- `content/`: The text of the document. `main.tex`, then `front/` (title page to abstract), `chapters/` (01 to 07) and `back/` (glossary and appendix).
- `figures/`: Figures with their sources, such as the `.pptx` or `.fzz` file next to the exported image. One folder per chapter (`03-implemented-solution/` to `06-results/`, and `appendix/`), named after the first chapter that uses the figure.
- `bibliography/`: References, cited in APA style through biblatex.
- `templates/`: The UTEM logo used on the title page.
- `docs/`: goals, glossary, assumptions, decisions and specs, plus `defense/` and `submitted/`.

## Contributing

Tasks use the Task issue form. Pull requests follow `.github/pull_request_template.md`. Rules for people and AI tools are in `AGENTS.md`.

## Standard

This repository follows `SVN11X/standards@v1` with the `docs` profile. `AGENTS.md` is generated, so do not edit it by hand. To regenerate it or run the check locally:

```bash
pip install pyyaml
git clone --depth 1 --branch v1 https://github.com/SVN11X/standards .standards
python .standards/scripts/standard.py agents .
python .standards/scripts/standard.py check .
```

## License

Not licensed for reuse. All rights reserved.
