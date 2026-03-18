# Security Policy

## Reporting a vulnerability

If you discover a security vulnerability in fialr, report it responsibly.

**Do not** open a public GitHub issue for security vulnerabilities.

Email: security@fialr.com

Include:

- Description of the vulnerability
- Steps to reproduce
- Affected versions
- Any potential impact assessment

We aim to acknowledge receipt promptly and will provide an initial assessment as soon as practical.

## Scope

In scope:

- Vulnerabilities that could lead to data loss, data corruption, or unauthorized file access
- Bypass of sensitivity tier enforcement
- Bypass of dry-run / reviewed flag safety gates
- SQLite injection or operations ledger tampering
- License validation bypass

Out of scope:

- Vulnerabilities in third-party dependencies (report upstream)
- Issues requiring physical access to the machine
- Social engineering
- The documentation website
