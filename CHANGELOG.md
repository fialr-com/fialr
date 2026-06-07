# Changelog

All notable changes to fialr are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [1.0.0] — Unreleased

Initial release.

### Added

- Filesystem inventory with BLAKE3 and SHA256 hashing
- Sensitivity classification (3 tiers: Restricted, Sensitive, Internal)
- Dry-run plan generation with naming convention enforcement
- Schema-driven reorganization with pre/post hash verification
- Hash-based and near-duplicate detection
- Local AI enrichment via Ollama (OCR, text extraction, metadata inference)
- Append-only audit ledger (SQLite)
- Job checkpoint and resume
- Cross-platform support: macOS, Linux
- Extended attribute metadata (macOS, Linux) with SQLite fallback
- CLI organized into six command groups (workflow, discover, enrich, tools, status, license) plus an interactive TUI
- Sidecar export (JSON, Markdown, CSV)
- Ed25519 binary signatures via minisign
- BLAKE3 checksums for release artifacts
