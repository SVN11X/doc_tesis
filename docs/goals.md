# Goals

<!-- Written by the owner. AI tools may format or translate this file, never invent its content. Replace every TODO(owner) line. -->

## Vision

Keep the defended thesis readable, buildable and reusable as a public record.

## Users

The committee, readers of the thesis, and the author reusing its material.

## Objectives

- The thesis PDF and the slides open without building anything.
- The source builds the same PDF with one command, on the owner's computer and in CI.
- The defense material lives next to the thesis, with its sources and credits.

## Non-goals

- Change the thesis text after its approval.
- Publish the rehearsal recordings.

## Success criteria

- CI builds the PDF with no undefined reference.
- The standard check passes.

## Priorities

1. The approved text stays unchanged over any improvement.
2. Clarity for readers over keeping every intermediate version.

## Constraints

- XeLaTeX with biber and makeglossaries, and the Arial and TeX Gyre Pagella fonts.
- Files over 5 MB go to Git LFS.
- Rehearsal recordings and videos stay private, only on the owner's computer.
