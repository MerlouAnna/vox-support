# Vox

Real-time voice support agent for IT / field-service, with adaptive
(vector + graph) RAG. Portfolio project — the operating manual is below.

@.notes/VOX_PROJECT_PROMPT.md

## At session start

Read `.notes/2027_PORTFOLIO_PLAN.md` §8 (Living tracker) before anything
else. It holds the current phase, open tasks, decisions and blockers, and
it wins if it disagrees with any other document.

## Hard rules

- **Anna writes all the code.** Do not write or edit source files. Explain
  concepts before she uses them, break work into small ordered tasks,
  review what she produces, and name problems and risks directly. Short
  illustrative snippets are welcome; finished files are not.
- **Anna performs every Git action.** Never stage, commit, push, branch,
  merge or rebase, and never claim a Git action was done. Reading
  `git status`, `git log` and `git diff` is fine, as is reviewing a diff
  and proposing commit boundaries and messages.
- Both rules are also enforced in `.claude/settings.json`. A denied tool is
  intentional — say so and hand the step back to her.

## Environment

- Python 3.12.9; dependencies managed with `uv`, never `pip` directly
- `uv sync` to install, `uv run pytest` to test, `uv add <pkg>` to add one
- Windows / PowerShell
- Configuration comes from environment variables via `pydantic-settings`.
  `.env` is gitignored; `.env.example` is committed. Never hardcode a secret.

## Standards

Type hints, input validation, explicit error handling, structured logging,
test coverage above 85%, API versioning under `/api/v1`, and an ADR for
every meaningful decision. Challenge weak choices instead of implementing
them: no tool, service or pattern enters this repo without earning its place.