# fialr

AI-native archival infrastructure for files that matter.

fialr treats files as long-term digital assets with local AI at the foundation. It
assigns cryptographic identity, classifies sensitivity, generates vector embeddings
for semantic discovery, and structures a corpus into an adaptive, machine-native
archive.

Every file is enriched by local AI that learns from the corpus. Every operation is
logged to an append-only ledger. Every file is hash-verified before and after
modification. Nothing moves without a dry-run review first.

This site is the public documentation for developers, contributors, and security
researchers. The product itself is proprietary; source code is not distributed in
the public repository, which serves as the issue tracker and the home for these
docs.

## Design pillars

- **Provenance over convenience.** Every operation is recorded in an append-only
  SQLite ledger (`operations`). The original state of a file — its name, path, and
  hash — is always recoverable. The ledger is treated as sacred: append-only and
  non-rebuildable.
- **Content-hash identity.** The BLAKE3 hash of file content is the stable
  identifier. Filenames and paths are mutable metadata. Deduplication, rename, and
  reorganization are all coherent under this model. SHA256 is kept as a secondary
  hash for cross-tool and archival verification.
- **SQLite as source of truth.** The SQLite database is authoritative for all
  metadata and audit history on every platform. Extended attributes (XATTRs) are a
  derived cache, rebuilt from SQLite — never the reverse. Where XATTRs are
  unsupported, metadata is written to SQLite only and the skip is logged; no
  functionality is lost.
- **Tier-gated enrichment.** Files are classified into three sensitivity tiers. All
  tiers are enriched by local AI (Ollama) by default. Cloud enrichment is opt-in for
  the lower tiers and, for the most sensitive tier, requires two independent
  confirmations.
- **Safety by default.** Every module runs in dry-run mode by default. Destructive
  execution requires an explicit flag or confirmation. No file operation runs
  without human approval.

## How it fits together

- **Content hash as identity.** BLAKE3 is the canonical identifier; SHA256 is the
  archival secondary.
- **Local AI, adaptive corpus.** Enrichment and vector embeddings run locally via
  Ollama. Each file indexed improves semantic search, deduplication, and metadata
  quality across the corpus. Cloud providers are available as opt-in for
  non-restricted files.
- **Infrastructure, not organizer.** A structured, vector-indexed corpus is a
  reliable input to future applications: AI agents, semantic search, automation
  pipelines, and tools that do not yet exist.

## Platform and license

- **Platforms:** macOS and Linux. Windows support is tracked but the primary targets
  are macOS (Apple Silicon and Intel) and Linux (x64).
- **License:** proprietary. A license is required to run the gated commands; a set of
  core commands is available without a license (see the [CLI reference](cli.md)).
  Activation is a one-time online step via `api.fialr.com`; the tool is fully offline
  thereafter.

## Where to go next

- [Architecture](architecture.md) — module map, job execution model, the SQLite and
  XATTR data model, sensitivity tiers, and the enrichment pipeline.
- [CLI reference](cli.md) — the command surface, grouped.
- [Security](security.md) — threat model summary and how to report a vulnerability.
- [Verifying releases](verifying-releases.md) — minisign signatures and BLAKE3
  checksums.
- [Contributing](contributing.md) — toolchain, the merge gates, and the decision log.

## Links

- Repository and issue tracker: [github.com/fialr-com/fialr](https://github.com/fialr-com/fialr)
- Product site and licensing: [fialr.com](https://fialr.com)
- Security contact: `security@fialr.com`
- Licensing and billing: `licensing@fialr.com`
