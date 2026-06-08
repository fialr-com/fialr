# Security

fialr is a local-first archival tool. The default posture is that user file content
never leaves the machine. Cloud paths exist, but they are gated, opt-in, and — for
the most sensitive tier — require two independent confirmations.

This page summarizes the threat model: the assets, the trust boundaries, and the key
mitigations. The full model — with per-component attack surfaces, residual risks, and
secret-rotation procedures — is maintained alongside the source.

## Assets

Ordered by sensitivity.

| Asset | Where it lives | Why it matters |
|-------|----------------|----------------|
| User file content, Tier 1 (RESTRICTED) | The filesystem; optionally an encrypted vault | Tax records, identity documents, medical and legal files. Disclosure is the worst outcome. |
| User file content, Tier 2 / Tier 3 | The filesystem | Sensitive and internal material; lower blast radius than Tier 1 but still private. |
| SQLite ledger and audit trail | `fialr.db` (path configurable) | Source of truth for metadata and the append-only `operations` ledger. Provenance and recoverability depend on it. |
| License key | `~/.config/fialr/license.json` (0600) | A paid, machine-bound, server-validated credential. |
| Release signing key (minisign) | 1Password / CI secret, never on disk | Compromise lets an attacker sign malicious releases. |
| Cloud API key | OS keychain (keyring) or `ANTHROPIC_API_KEY` env | A billable credential; leakage is a financial and abuse risk. |
| License-server data and Worker secrets | Cloudflare D1 and Worker secrets | License keys, activations, and customer email; admin and webhook secrets. |

The `operations` table is treated as sacred: append-only and non-rebuildable. XATTRs
are a derived cache rebuilt from SQLite, never the reverse.

## Trust boundaries

There are five trust zones. The local machine is trusted — fialr does not defend
against a compromised host (see [accepted risks](#out-of-scope-and-accepted-risks)).
Raw user content is permitted to cross only one boundary, under explicit conditions.

The boundary-crossing rules the code enforces:

- **Local → Ollama.** Raw text crosses, but the endpoint is validated to be
  `localhost` / `127.0.0.1` / `::1` only. A non-local Ollama endpoint fails at
  construction.
- **Local → cloud (direct BYOK).** Only for Tier 2/3, and only when the provider is
  explicitly configured. Tier 1 is blocked here at the orchestrator.
- **Local → cloud (two-step).** Only sanitized metadata crosses. Raw file text never
  leaves the machine in the two-step path.
- **Local → license Worker.** Only the license key, the BLAKE3-hashed machine ID, the
  platform string, and the version cross, over TLS.
- **Stripe → Worker.** Every webhook body is HMAC-verified before any state change.

See the [architecture page](architecture.md#trust-boundaries-and-data-flow) for a
diagram of the local data flow.

## Key mitigations

### Filesystem ingest

- Paths are constructed with `pathlib` against a resolved target root; a static check
  flags string-concatenated paths in the executor.
- Symlinked directories are not recursed into (`followlinks=False`).
- A layered exclusion system prunes sensitive subtrees; every excluded path is
  recorded in the manifest with a reason — nothing is silently skipped.
- Identity is the BLAKE3 content hash, not the path. The executor verifies the hash
  before and after a move and rolls the file back on a post-move mismatch.

### Local and cloud AI

- The Ollama endpoint is validated to be local; non-local endpoints are rejected.
- Tier 1 results from a local provider are always routed to the review queue,
  regardless of confidence — nothing is auto-applied.
- Tier 1 cloud requires two independent gates, both required: the config flag
  `allow_tier1_cloud = true` and the CLI flag `--allow-tier1`. The override uses AND
  logic, statically verified.
- In the two-step path, raw text goes only to local Ollama; only sanitized metadata
  is sent to the cloud. Sanitization redacts SSNs, EINs, Luhn-valid credit-card
  numbers, and account/routing numbers, while preserving names, institutions, record
  types, dates, and tags.
- Cloud batches surface a cost estimate and confirmation prompt before running.

### License server

- Stripe webhooks are HMAC-verified in constant time, with replay protection.
- Admin endpoints require a constant-time-compared admin key and fail closed.
- Per-IP rate limiting guards against enumeration and brute force.
- All D1 access uses prepared statements; input is strictly validated against
  format patterns.
- Responses carry `no-store`, `nosniff`, `DENY` framing, and scoped CORS.

### Vault and local credentials

- Vault passwords are delivered to the backend via stdin (APFS) or a pseudo-terminal
  (age), never as CLI arguments, and are never written to disk or the ledger.
- On rehydrate, the restored file's BLAKE3 is recomputed and compared; a mismatch
  unlinks the output and records the failure.
- `license.json` is written `0600` in a `0700` directory; activation uses
  certificate-verified HTTPS; the machine ID is a BLAKE3 hash, never the raw hardware
  identifier.

### Supply chain

- Floor versions in `pyproject.toml`, exact resolution pinned in `uv.lock`.
- gitleaks scans for committed secrets; ruff's bandit ruleset and a project security
  audit provide static checks; an SBOM is generated in CI.
- Release artifacts ship with checksums and minisign signatures. See
  [Verifying releases](verifying-releases.md).

## Out of scope and accepted risks

These are conscious decisions.

- **Compromised host.** fialr trusts the machine it runs on. An attacker with the
  user's account, root, or physical access is out of scope.
- **Local feature gating is not anti-piracy.** Command gating reads the cached
  license file; activation limits are enforced server-side. Local gating is best
  effort.
- **LLM provider trust.** When cloud enrichment is used, the user accepts that
  sanitized metadata (two-step) or Tier 2/3 raw text (direct BYOK) is processed by the
  provider under that provider's terms.
- **Sanitization is best-effort, not a guarantee.** It covers the enumerated
  identifier classes. The Tier 1 two-confirmation gate is the primary control.

## Reporting a vulnerability

If you discover a security vulnerability in fialr, report it responsibly.

**Do not** open a public GitHub issue for security vulnerabilities.

Email: `security@fialr.com`

Include:

- A description of the vulnerability.
- Steps to reproduce.
- Affected versions.
- Any potential impact assessment.

We aim to acknowledge receipt promptly and will provide an initial assessment as soon
as practical.

### Scope

**In scope:**

- Vulnerabilities that could lead to data loss, data corruption, or unauthorized file
  access.
- Bypass of sensitivity tier enforcement.
- Bypass of dry-run / reviewed-flag safety gates.
- SQLite injection or operations-ledger tampering.
- License validation bypass.

**Out of scope:**

- Vulnerabilities in third-party dependencies (report upstream).
- Issues requiring physical access to the machine.
- Social engineering.
- The documentation website.
