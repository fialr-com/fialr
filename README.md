# fialr

Archival infrastructure for files that matter.

**[Documentation](https://fialr.com)** · **[Purchase](https://fialr.com/licensing/)** · **[Issues](https://github.com/fialr-com/fialr/issues)**

---

fialr assigns cryptographic identity to files, classifies sensitivity, enforces naming conventions, detects duplicates, and structures your corpus for both human discovery and machine-native applications.

Every operation is logged to an append-only ledger. Every file is hash-verified before and after modification. Nothing moves without a dry-run review first.

## Key properties

- **Content hash as identity.** BLAKE3 hash is the stable identifier. Filenames and paths are mutable metadata.
- **Local by default.** All enrichment runs locally via Ollama. Cloud providers (Claude API, BYOK) are opt-in for Tier 2–3 files only. Tier 1 files are local-only unless a triple-gate override is active.
- **Safety by default.** Every module has dry-run mode on by default. Execution requires explicit confirmation.
- **Infrastructure, not organizer.** A structured corpus is a reliable input to future applications.

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
