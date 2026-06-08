# CLI Reference

The fialr command surface is organized into six groups, as shown in `fialr --help`.
Every command runs in dry-run mode by default where it performs filesystem writes;
execution requires an explicit `--execute` flag or confirmation.

Some commands are available without a license; others require an active license. The
split is noted per group below.

!!! note "Grounded in the feature manifest"
    The commands and flags on this page are taken from the project's
    `feature-manifest.json`, the code-derived source of truth for the command surface.
    No command or flag is listed here that is not present in that manifest.

## WORKFLOW

Multi-step pipelines. Dry-run by default; pass `--execute` to apply.

| Command | Description |
|---------|-------------|
| `process` | End-to-end pipeline over a target: scan, enrich, rename, and organize. Dry-run by default. |
| `organize` | Schema-driven reorganization of a target into the configured directory structure. |
| `cleanup` | Combined dedup and validate pass to tidy a corpus. |

Common flags include `--execute`, `--reviewed`, `--jobs-dir PATH`, `--schema PATH`,
`--sensitivity-rules PATH`, and `-o, --output-dir PATH`. `process` also accepts
`--no-enrich` and `--no-rename`; `cleanup` accepts `--no-dedup` and `--no-validate`.

## DISCOVER

Inventory and search. Read-only.

| Command | Description |
|---------|-------------|
| `scan` | Walk a target, build a file inventory, and classify sensitivity. |
| `search` | Query the corpus: keyword (FTS5), AI-expanded, or semantic. |

`scan` accepts `--include-cloud`, `--no-classify`, `--sensitivity-rules PATH`, and
`-o, --output PATH`. `search` accepts `--ai`, `--semantic`, `--similar FILE`,
`--category CAT`, `--sensitivity N`, `--threshold F`, `--limit N`, and `--reindex`.

## ENRICH

AI metadata and naming.

| Command | Description |
|---------|-------------|
| `enrich` | Run local (or opt-in cloud) AI enrichment to produce metadata and embeddings. |
| `rename` | Apply the template-driven naming convention to files (and, with `--dirs`, directories). |

`enrich` accepts `--execute`, `--embed-only`, `--cloud-refine`,
`--sensitivity-rules PATH`, `--jobs-dir PATH`, and `-y, --yes`. `rename` accepts
`--execute`, `--dirs`, `--prefix`, `--template`, `--from PATH`, `--skip PATTERNS`,
and `-o, --output PATH`.

## TOOLS

Utility operations.

| Command | Description |
|---------|-------------|
| `hash` | Compute the BLAKE3 (or specified) hash of a file. |
| `export` | Export sidecar metadata for files in JSON, YAML, Markdown, or CSV. |
| `vault` | Create, mount, and manage an encrypted vault (APFS or age). |
| `validate` | Verify corpus integrity against recorded hashes and manifests. |
| `undo` | Roll back prior move, rename, or archive operations. |
| `dedup` | Detect exact and near-duplicate files and stage non-canonical copies. |

`hash` accepts `--algorithm ALGO` and `--json`. `export` accepts `--format FORMAT`,
`--batch`, and `-o, --output PATH`. `vault` accepts `--backend`, `--vault PATH`,
`--dest PATH`, `--size`, and `--execute`. `validate` accepts `--check CHECK`. `undo`
accepts `--last N`, `--job UUID`,
`--op UUID`, `--execute`, and `--force`. `dedup` accepts `--strategy STRATEGY`,
`--jobs-dir PATH`, and `--execute`.

## STATUS

Interactive shell and inspection.

| Command | Description |
|---------|-------------|
| `tui` | Launch the Textual interactive shell (dashboard, browser, review, search, pipeline). |
| `status` | Show corpus health: file counts, enrichment percentage, embeddings, last job, database size, and license state. |
| `config` | Show or set configuration values, including the AI provider. |

`config` accepts `--show`, `--provider NAME`, and `--key KEY`, plus a `key value`
positional form.

## LICENSE

License management.

| Command | Description |
|---------|-------------|
| `activate` | Activate a license key, binding it to this machine via `api.fialr.com`. |
| `deactivate` | Release this machine's activation slot and remove local license state. |
| `license` | Show current license status. |

## License gating

A subset of commands runs without a license; the rest require an active license.

**Available without a license:** `activate`, `config`, `deactivate`, `hash`,
`license`, `rename`, `scan`, `search`, `status`, `tui`, `undo`, `validate`.

**Require a license:** `cleanup`, `dedup`, `enrich`, `export`, `organize`,
`process`, `vault`.

The license check runs between argument parsing and dispatch. Activation is a
one-time online step; the tool is fully offline afterward. See
[Verifying releases](verifying-releases.md) for how downloads are signed and checked.
