# fialr

AI-native archival infrastructure for files that matter.

**[Documentation](https://fialr.com)** · **[Purchase](https://fialr.com/licensing/)** · **[Issues](https://github.com/fialr-com/fialr/issues)**

---

fialr treats files as long-term digital assets with local AI at the foundation. It assigns cryptographic identity, classifies sensitivity, generates vector embeddings for semantic discovery, and structures your corpus into an adaptive, machine-native archive.

Every file is enriched by local AI that learns from your corpus. Every operation is logged to an append-only ledger. Every file is hash-verified before and after modification. Nothing moves without a dry-run review first.

## Key properties

- **Content hash as identity.** BLAKE3 hash is the stable identifier. Filenames and paths are mutable metadata.
- **Local AI, adaptive corpus.** Enrichment and vector embeddings run locally via Ollama. Each file indexed improves semantic search, deduplication, and metadata quality across the entire corpus. Cloud providers available as opt-in for non-restricted files.
- **Safety by default.** Every module has dry-run mode on by default. Execution requires explicit confirmation.
- **Infrastructure, not organizer.** A structured, vector-indexed corpus is a reliable input to future applications: AI agents, semantic search, automation pipelines, and tools that do not yet exist.

## Install

Purchase a license at [fialr.com/licensing](https://fialr.com/licensing/) to receive a download link and license key.

| Platform | Binary |
|---|---|
| macOS (Apple Silicon) | `fialr-1.0.0-macos-arm64` |
| macOS (Intel) | `fialr-1.0.0-macos-x64` |
| Linux (x64) | `fialr-1.0.0-linux-x64` |

## Activate

```
fialr activate YOUR-LICENSE-KEY
```

One-time activation via `api.fialr.com`. Fully offline after activation.

## Documentation

Full documentation at [fialr.com](https://fialr.com):

- [Installation](https://fialr.com/getting-started/installation/)
- [Quick Start](https://fialr.com/getting-started/quick-start/)
- [CLI Reference](https://fialr.com/cli/overview/)
- [Architecture](https://fialr.com/architecture/overview/)

## Issues

This repository is the public issue tracker for fialr. Use it to report bugs, request features, and ask questions.

- [Report a bug](https://github.com/fialr-com/fialr/issues/new?template=bug_report.yml)
- [Request a feature](https://github.com/fialr-com/fialr/issues/new?template=feature_request.yml)

For security vulnerabilities, do not open a public issue. Email security@fialr.com.

For billing and licensing issues, email licensing@fialr.com.

## License

fialr is proprietary software. See [Terms of Use](https://fialr.com/legal/terms/) and [Licensing](https://fialr.com/licensing/).
