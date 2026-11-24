# 0004. Embed the public demo video in the defense slides

- Status: accepted
- Date: 2026-11-23
- Proposed by: Claude Code
- Accepted by: the owner, in the Claude Code session that built `slides-v3.pptx`, on 2026-11-23

## Context

The v3 defense slides open with a 48 s video of a real exploration run. The video lives in `videos/youtube/final/`, and `videos/` is private and ignored by git. This repository is public, so embedding the video in a committed deck publishes it.

## Decision

Embed a compressed, silent copy (H.264, 1920 px wide, about 7 MB) of `videos/youtube/final/20260929_tesis_yt.mp4` in `docs/defense/slides-v3.pptx`. The owner confirmed this video is already public on YouTube. Every other file in `videos/` and `defense-rehearsals/` stays private.

## Alternatives considered

- Keep the deck with the video only on the owner's computer and commit a copy with a still image. Simple, but leaves two decks to keep in sync.
- Link the YouTube video from the slide. It needs an internet connection during the defense.

## Consequences

The committed deck plays the video offline and the deck grows to about 14 MB, stored with Git LFS. To undo it, replace the video on slide 2 with `images/v3/slide-02-demo-poster.jpg` and commit the deck again. The video stays in the git history, so treat it as published.
