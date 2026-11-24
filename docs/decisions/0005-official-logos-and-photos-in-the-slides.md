# 0005. Official logos and photos in the defense slides

- Status: accepted
- Date: 2026-11-23
- Proposed by: Claude Code
- Accepted by: the owner, in the Claude Code session that revised `slides-v3.pptx`, on 2026-11-23

## Context

The owner asked for the logos of the companies the slides name (Codelco, Glencore, Vale, Boston Dynamics and others) and for photos of the robots and procedures they describe. Most of those logos and photos are not under an open license, and this repository is public under CC BY 4.0.

## Decision

Store the official logos and product photos in `docs/defense/images/v3/` and embed them in `slides-v3.pptx`. Each one is listed in `docs/credits.md` with its owner, source and license, and with a note that logos are trademarks used only to identify the companies. Icons come from Lucide, Tabler and Simple Icons, whose licenses allow redistribution with the notice kept in `docs/credits.md`.

## Alternatives considered

- Use only openly licensed images from Wikimedia Commons or Openverse. It avoids any claim, but several logos have no open version.
- Keep a deck with the official images only on the owner's computer and commit a version without them. It leaves two decks to keep in sync.

## Consequences

The public repository holds images it has no license to redistribute beyond identification. If an owner objects, remove that file, replace it on the slide with the company name and an icon, and update `docs/credits.md`. The files stay in the git history, so treat them as published.
