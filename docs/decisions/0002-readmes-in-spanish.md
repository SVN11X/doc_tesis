# 0002. READMEs in Spanish, with an English copy of the main one

- Status: accepted
- Date: 2026-11-22
- Proposed by: the owner
- Accepted by: the owner, in the Claude Code session of 2026-11-22

## Context

The standard writes the README files in English, and its rule for the docs profile keeps everything outside `content/` in English. The thesis and its readers are Spanish speaking, and the owner asked for the README files in Spanish, plus an English README.

## Decision

- Every `README.md` in the repository is written in Spanish. Folder names, file names and code stay in English.
- The main README also exists in English at `docs/en/README.md`. Both link to each other.
- The English copy lives in `docs/en/` because the standard allows only `README.md` among the README files at the repository root.

## Alternatives considered

- `README.en.md` at the root is the usual convention, but the standard check rejects any root file it does not list.
- Keeping the README files in English follows the standard, but does not serve the readers of a Spanish thesis.

## Consequences

When the main README changes, `docs/en/README.md` must change in the same commit. Other documents (`AGENTS.md`, `docs/how-it-works.md`, decisions) stay in English. To undo it, restore the English text from the commit before this decision.
