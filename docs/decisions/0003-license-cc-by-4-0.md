# 0003. License the thesis under CC BY 4.0

- Status: accepted
- Date: 2026-11-22
- Proposed by: Claude Code (repo-improve)
- Accepted by: the owner, in the Claude Code session of 2026-11-22

## Context

The repository is public. The owner first chose no license, but the standard check fails on a public repository without one, and the merge script never merges with a failing check.

## Decision

License the repository under Creative Commons Attribution 4.0 International (CC BY 4.0): `LICENSE` at the root, `license: CC-BY-4.0` in `.standard.yml`.

## Alternatives considered

- No license, all rights reserved: keeps every right, but the standard check stays red and every merge waits for the owner.
- A private repository: passes the check without a license, but hides the thesis, the submitted PDF and the defense material.

## Consequences

Anyone may share and adapt the thesis, even commercially, as long as they credit the author. Copies made under CC BY 4.0 keep that license, so changing it later only affects new copies.
