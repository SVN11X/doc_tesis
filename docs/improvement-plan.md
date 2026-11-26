# Improvement plan

Scope agreed with the owner on 2026-11-21: organize the files without changing the text of the thesis. Only path strings inside TeX files may change.

- [x] Remove the files the owner already deleted (`_sin_uso/`, the observations table, the cleanup notebook) and the unused `_sin_uso/1-PagPreliminar/Logo.jpg`.
- [x] Move the thesis to the docs layout: `content/`, `figures/`, `bibliography/`, `templates/`, with English names. Change only the 47 path lines and prove the PDF text is identical.
- [x] Publish the defense slides, script and images in `docs/defense/` and the corrected PDF in `docs/submitted/`, with files over 5 MB in Git LFS. Keep `defensa/` (rehearsals, feedback, videos) local only.
- [x] Adopt the standard: `.standard.yml`, `README.md` with the build command, `AGENTS.md` and `docs/`. License CC BY 4.0 (first none, changed by the owner because the standard rejects a public repository without a license), citation style APA.
- [x] Add CI that runs the standard check and builds the PDF with XeLaTeX. The release workflow is left out: it needs write access and this thesis uses `submitted-*` tags, not `v*` releases.
- [x] Group the figures in one folder per chapter (`figures/03-implemented-solution/` to `figures/06-results/`, `figures/appendix/`). Change only the 30 path lines and prove the PDF is identical.
- [x] Put every image of the defense slides in `docs/defense/images/`, named by the first slide that shows it, extracting the 38 that exist only inside the `.pptx`, plus an index per slide.
- [x] Rename the local `defensa/` to `defense-rehearsals/` with recordings named by date, and move the YouTube video to `videos/youtube/`. Both stay ignored by git.
- [x] Write every README in Spanish and keep an English copy of the main one in `docs/en/README.md` (decision 0002).
- [x] Delete the four UTEM logos that neither the thesis nor the slides use.
- [x] Write `docs/goals.md`. Done on 2026-11-26 from the proposal the owner approved.
- [x] Tag the submitted version: `submitted-2026-10` on 42b5327, whose XeLaTeX build has the same text as `docs/submitted/thesis-corrected-v2.pdf`.

## Close after the defense

Scope agreed with the owner on 2026-11-26: the thesis was defended and approved on 2026-11-25, so tidy the repository as a final archive. The thesis text stays frozen.

- [x] Remove the four v3 backup copies that two "cambios" commits added (history keeps them) and ignore `*.backup.*` and `*.pre-refinamiento.*` in `docs/defense/`.
- [x] Update the status in `README.md`, `docs/en/README.md` and `docs/defense/README.md`: defended and approved on 2026-11-25, final grade 6.7 (document 6.6, presentation 6.8).
- [x] Copy the description and topics of `.standard.yml` to the GitHub About panel.
- [x] Delete the branches of the merged pull requests 2 to 6. GitHub keeps their commits in each pull request.
- [x] Archive the two unmerged October branches and the local backup branch as `archive/*` tags, then delete the branches.
- [x] Tag `defended-2026-11-25` on 6e0f427, the state on the day of the defense, and publish a release with the thesis PDF and the slides PDF.
- [x] Confirm `docs/how-it-works.md`. The owner reviewed it on 2026-11-26 and found it correct.

## Organize the defense folder

Scope agreed with the owner on 2026-11-26: make the final deck easy to find and keep the earlier version and the support files apart.

- [x] Write `docs/goals.md` from the proposal the owner approved, and regenerate `AGENTS.md`.
- [x] Move the slides, PDF and script used in the defense to `docs/defense/final/` as `defense-slides.pptx`, `defense-slides.pdf` and `defense-script.md`.
- [x] Move the v2 slides, PDF and script to `docs/defense/previous/v2/`, and extend the LFS pattern to `.pptx` files in subfolders.
- [x] Move the rehearsal audio script to `docs/defense/tools/generate_rehearsal_audio.py`, writing to the ignored `rehearsal-audio/`. `images/` stays, since credits and the slide index point there.

## Review after the defense

Scope agreed with the owner on 2026-11-26 after a full review. The thesis text stays frozen, and the "Revalidación v18" never enters it.

- [x] Credit the images of the v2 slides in `docs/credits.md`, searched one by one with Google Lens.
- [x] Link the code repository, its path map, the explainer guide and the defense template from both READMEs.
- [x] Make the offline build work in VS Code with a workspace setting, document the tested toolchain and discard the build assumption.
- [x] Match the audio script docstring to the final deck and ignore `*.loa`.
- [x] Keep the signed grade page and the filled authorization form out of the repository, as a non-goal.
- [ ] BLOCKED: remove the 21 standalone Microsoft 365 icon SVGs from `docs/defense/images/`? They stay inside the v2 deck, where Microsoft allows them.
- [ ] BLOCKED: replace `slide-08-desktop-computer.png` (Vecteezy Pro) and `slide-08-navigation-arrow.png` (app icon, no license), or keep them credited?
