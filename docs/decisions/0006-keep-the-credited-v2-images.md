# 0006. Keep the third-party images of the v2 slides with their credits

- Status: accepted
- Date: 2026-11-26
- Proposed by: Claude Code
- Accepted by: the owner, in the Claude Code session of the post-defense review, on 2026-11-26

## Context

The post-defense review found third-party images in `docs/defense/images/` that `docs/credits.md` did not list. A search with Google Lens identified most of them. Three cases have a weak license: 21 Microsoft 365 icons saved as SVG files, which Microsoft allows inside Office files and asks not to save as separate images; `slide-08-desktop-computer.png`, listed under the paid Vecteezy Pro license; and `slide-08-navigation-arrow.png`, the app icon of Guru Track with no license found. The 21 SVG files are byte-identical to images inside `docs/defense/previous/v2/slides.pptx`, and the other two are inside both the v2 deck and `docs/defense/final/defense-slides.pptx`.

## Decision

Keep every one of these files, because the decks use them, and credit each one in `docs/credits.md` with its owner, source, license and the result of the search.

## Alternatives considered

- Delete the 21 standalone SVG files and keep them only inside the v2 deck. It follows Microsoft's wording more closely, but the slide image index would lose files the deck uses.
- Replace the desktop computer and the arrow with icons under an open license. It removes the license doubt, but it changes the decks used in the defense.

## Consequences

The public repository keeps images whose license does not clearly allow redistribution, with their owners named. If an owner objects, remove that file, replace it in the deck with an icon from `docs/defense/images/icons/`, and update `docs/credits.md`. The files stay in the git history, so treat them as published.
