# 0001. Organize the files without changing the text

- Status: accepted
- Date: 2026-11-21
- Proposed by: Claude Code (repo-improve)
- Accepted by: the owner, in the Claude Code session of 2026-11-21

## Context

The thesis lived in `1-PagPreliminar/`, `2.Texto/`, `3.Pag_final/` and `2.Texto/Imag/`, with Spanish names, unused files in `_sin_uso/` and the defense material outside git. The owner asked to organize the files and not to change the content of any file.

## Decision

- Use the docs layout of the standard: `content/` (`front/`, `chapters/`, `back/`), `figures/`, `bibliography/` and `templates/`, with English kebab-case names.
- Inside the TeX files, change only the path strings that point to moved files (47 lines). The owner allowed path lines and nothing else.
- Store files that can pass 5 MB (`docs/defense/*.pptx`, `docs/defense/*.png`, `docs/submitted/*.pdf`) in Git LFS.
- Keep `defensa/` (rehearsal recordings, their feedback and the videos) on the owner's computer only. The feedback is private for now.
- Keep the line endings and whitespace of `.tex` and `.bib` files as they are, through `.gitattributes` and `.editorconfig`.

## Alternatives considered

- Declaring the old folders as extra folders kept every path, but left the layout and names the owner asked to fix.
- Committing the large files directly was simpler, but the standard limits files to 5 MB.

## Consequences

The PDF built from the new layout has the same 168 pages, identical text and the same 52 images as before the move. Editors and tools that pointed to `main.tex` at the root must now open `content/main.tex`. To undo it, revert the commit `refactor: move the thesis into the docs layout`.
