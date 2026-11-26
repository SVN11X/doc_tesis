# Assumptions

Things taken as true without confirmation. Review the open ones in every pull request. Status is open, confirmed or discarded.

| Date | Assumption | Made by | Task | Status |
|------|------------|---------|------|--------|
| 2026-11-21 | The owner builds with XeLaTeX, from the folder of the main file, as VS Code LaTeX Workshop does by default. The submitted PDF was produced by xdvipdfmx, the XeLaTeX backend. | Claude Code | Organize the files | discarded: the owner built it on Overleaf. On 2026-11-26 the README command and the VS Code recipe latexmk (xelatex) built the same text offline with MiKTeX, and LaTeX Workshop's first recipe failed with pdfLaTeX |
| 2026-11-21 | Every part of `defensa/` except `ensayo/` and the videos may be public, since the owner only named the feedback as private. | Claude Code | Organize the files | open |
| 2026-11-23 | The `video_1.mp4` the owner named for slide 2 is `videos/youtube/final/20260929_tesis_yt.mp4`, the only 48 s video on disk. | Claude Code | Defense slides v3 | open |
| 2026-11-23 | The v3 slides keep the decimal point of the thesis (3.4 cm), not the decimal comma. | Claude Code | Defense slides v3 | discarded: the owner writes 3,4 cm, so slides use the decimal comma and source lines keep section numbers |
| 2026-11-23 | The script that generated `slides-v3.pptx` stays outside the repository, and later changes are made in PowerPoint. | Claude Code | Defense slides v3 | confirmed |
| 2026-11-23 | "Sin colisiones" on the v3 slides comes from the owner's direct observation of the five valid runs, not from the thesis logs. | Claude Code | Defense slides v3 | discarded: the demo video shows a brief contact at 0:10 to 0:11, so slides say "sin intervención humana" |
| 2026-11-23 | "Sin atascos" on slide 16 comes from the owner's wording for the five valid runs. The thesis records that they ended automatically without manual intervention. | Claude Code | Defense slides v3 revision | open |
