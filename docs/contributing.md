# Contributing

fialr is proprietary software. Source code is not distributed in the public
repository; that repository serves as the public issue tracker and the home for this
documentation. This page documents the engineering process the project holds itself
to — the toolchain, the merge gates, and the working discipline — for contributors and
for anyone reviewing how the project is built.

## Reporting issues

- [Report a bug](https://github.com/fialr-com/fialr/issues/new?template=bug_report.yml)
- [Request a feature](https://github.com/fialr-com/fialr/issues/new?template=feature_request.yml)

For security vulnerabilities, do not open a public issue. Email `security@fialr.com`
(see [Security](security.md)). For billing and licensing issues, email
`licensing@fialr.com`.

## Toolchain

- **Python 3.12.** Python is pinned to 3.12 via `.python-version`. The project
  standardizes on uv-managed 3.12, which matches the CI matrix.
- **uv** manages the environment. The dependency graph is locked in `uv.lock`.

```bash
# One-time: install uv (https://docs.astral.sh/uv/)
brew install uv

# Create or refresh the environment from the lockfile (core + dev group).
uv sync

# Full dev environment, including enrichment + cloud extras:
uv sync --all-extras

# Run anything inside the env without activating it:
uv run fialr --help
```

Runtime extras stay in `[project.optional-dependencies]` so end-user installs
(`fialr[enrichment]`, `[cloud]`, `[tui]`) keep working. Dev tooling lives in the
`[dependency-groups].dev` group and is synced by default. The standard library comes
first: before adding a dependency, check whether it is already covered.

## Merge gates

The following gates run in CI and in the local pre-commit/pre-release suite. They are
enforced, not aspirational. A change that fails any gate does not merge.

| Gate | What it checks |
|------|----------------|
| **ruff** | Linting and formatting (`ruff check`, `ruff format --check`), including the `S` (bandit) security ruleset. |
| **mypy** | Static type checking. All public functions carry complete type annotations. |
| **pytest + coverage** | The full test suite with a coverage floor. Tests use synthetic fixtures only — never real user files — and never make network calls or run live inference. |
| **doc-parity** | App, internal architecture doc, and the published docs must agree on commands, options, schema, XATTR keys, license gating, and brand. Drift is a hard failure. |
| **gitleaks** | Scans for committed secrets, with synthetic test fixtures allowlisted. |

### Doc-parity and the feature manifest

Public and private docs must never drift from the app's actual feature set.
`feature-manifest.json` is the code-derived source of truth — commands, command
groups, documented options, license sets, database tables, and XATTR keys. It is
regenerated from the modules and committed; CI fails if it drifts. The public
repository vendors `feature-manifest.json` and validates its MkDocs documentation and
README against it, so public docs cannot drift either. When you change a command,
option, schema, or feature, update the docs and regenerate the manifest in the same
change.

## Working discipline

- **PR-enforced trunk.** Changes land via pull request with the required checks
  green. Branch protection on the private repository is enforced through pre-commit
  hooks and required CI checks.
- **Signed commits.** Commits are made under a dedicated project identity.
- **Atomic commits.** One logical change per commit. Commit messages describe the
  change, not just the files touched, and reference the relevant decision-log entry.
- **Read before write.** Read a file before modifying it; verify APIs and formats
  rather than guessing.
- **Interface-first.** Define the interface and type contracts, write the tests, then
  implement.

## The decision log

The project keeps an append-only decision and session log (`docs/log.yaml`) as its
institutional memory. Every decision, troubleshooting path, blocker, and outcome is
recorded there with enough detail — exact errors, commands, and paths — that later
work is grounded in documented history rather than guesswork. Entries are never
deleted; when a blocker is resolved, a new entry references the original. Commit
messages reference the relevant log entry IDs.

## Coding conventions

- All configuration in TOML; no hardcoded paths or values.
- All path operations via `pathlib`; no `os.path`.
- Structured logging for debug and audit; user-facing output via the `Output` class;
  no `print()`.
- The append-only `operations` ledger is sacred. Every file operation hashes before,
  executes, hashes after, and logs both.
- No bare `except:` blocks; errors carry context (path, operation, job UUID).
- f-strings for formatting; 88-character line length.
