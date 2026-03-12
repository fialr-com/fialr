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

We will acknowledge receipt within 48 hours and provide an initial assessment within 7 days.

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
