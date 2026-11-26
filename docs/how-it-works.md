# How it works

<!-- An AI tool may draft this file from the real code, never from a guess. It stays a draft until the owner confirms it. Update it in the same change that alters the main flow. Paths in backticks must exist: the check reads them. -->

## From start to finish

1. `latexmk -r content/latexmkrc -cd content/main.tex` reads `content/latexmkrc`, changes to `content/` and runs XeLaTeX on `content/main.tex`.
2. The preamble of `content/main.tex` sets the fonts, the page layout, the figure macros (`\utemFigure` and `\utemFigurePropia`), the glossary entries from `content/back/01-glossary.tex` and the bibliography from `bibliography/references.bib`.
3. The body includes the front matter from `content/front/`, the chapters from `content/chapters/` and the appendix `content/back/02-appendix.tex`.
4. latexmk runs biber for the APA references and makeglossaries for the glossary, then XeLaTeX again until every reference resolves.
5. The result is main.pdf, next to `content/main.tex`.

## Parts

- `content/main.tex`: preamble, macros and the order of every part of the thesis.
- `content/front/`: title page, reproduction authorization, grade note, dedication, acknowledgements and abstract.
- `content/chapters/`: the seven chapters, from introduction to conclusion.
- `content/back/`: glossary entries and appendix.
- `figures/`: every figure the chapters include, one folder per chapter, written as `../figures/<chapter>/<name>` from `content/`.
- `bibliography/references.bib`: every cited work.
- `templates/`: the UTEM logo of the title page.
- `docs/defense/` and `docs/submitted/`: the defense material and the submitted PDF. The build does not use them.

## Where to start reading

`content/main.tex`, because it lists every file of the thesis in reading order.

## Run it and check it

```bash
latexmk -r content/latexmkrc -cd content/main.tex
```

The build works when latexmk ends without errors and main.log, next to the PDF, has no undefined citation or reference.

## Not covered

The build needs the Arial font, which TeX distributions do not ship. It comes with Windows.
