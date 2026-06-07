# Verifying Releases

fialr release binaries are signed and checksummed so that a download can be verified
before it is run. This page describes how releases are signed and how to verify an
artifact you have downloaded.

!!! note "Binaries are a planned release artifact"
    Distributable binaries are produced by the release pipeline and published to
    GitHub Releases and the product site. Until the first release is published, the
    public keys and checksums shown here are placeholders. Always verify against the
    public key published with the release you are verifying.

## How releases are signed

Every release produces platform binaries:

| Platform | Filename pattern | Architecture |
|----------|------------------|--------------|
| macOS (Apple Silicon) | `fialr-{version}-macos-arm64` | aarch64 |
| macOS (Intel) | `fialr-{version}-macos-x64` | x86_64 |
| Linux | `fialr-{version}-linux-x64` | x86_64 |

Two integrity artifacts ship alongside each binary:

- **A minisign signature.** Each binary has a detached Ed25519 signature produced with
  [minisign](https://jedisct1.github.io/minisign/). The signing key is held as a CI
  secret (`MINISIGN_SECRET_KEY`), sourced from 1Password, written only to an ephemeral
  CI file, and removed after signing. It is never stored on disk beyond that step.
- **BLAKE3 checksums.** A `checksums-blake3.txt` file lists the BLAKE3 hash of each
  binary in the release.

The signing process, per platform, in CI:

1. Build the binary on the platform runner.
2. Compute the BLAKE3 checksum.
3. Sign the binary with minisign.
4. Upload the binary, its `.sig`, and the checksums file as release artifacts.

The release public key is published in multiple places so it can be cross-checked:
the product site, the repository, and the GitHub release itself.

## Verifying a download

You need two tools: `minisign` for the signature, and a BLAKE3 hasher such as
[`b3sum`](https://github.com/BLAKE3-team/BLAKE3) for the checksum. Verify both.

### 1. Verify the signature

Download the binary and its detached `.sig`, then verify against the published public
key:

```bash
minisign -Vm fialr-1.0.0-macos-arm64 -P <RELEASE_PUBLIC_KEY>
```

Replace `<RELEASE_PUBLIC_KEY>` with the public key published for that release.
Alternatively, if you have saved the public key to a file:

```bash
minisign -Vm fialr-1.0.0-macos-arm64 -p fialr-minisign.pub
```

A successful verification prints that the signature and the comment are trusted. If
verification fails, do not run the binary.

### 2. Verify the BLAKE3 checksum

Download `checksums-blake3.txt` and confirm the binary's hash matches the listed
value:

```bash
b3sum -c checksums-blake3.txt
```

Or compute the hash directly and compare it by eye against the entry in
`checksums-blake3.txt`:

```bash
b3sum fialr-1.0.0-macos-arm64
```

The checksums file has one line per artifact:

```
a1b2c3d4e5f6...  fialr-1.0.0-macos-arm64
e5f6a7b8c9d0...  fialr-1.0.0-macos-x64
c9d0e1f2a3b4...  fialr-1.0.0-linux-x64
```

The hashes above are illustrative. Use the real values from the release you are
verifying.

## Key rotation

If the release signing key is rotated, the new public key is republished everywhere
users verify against it — the repository, the product site, and the release notes —
and the rotation is announced in the changelog with the new key, its fingerprint, and
the last version signed with the old key. Retired public keys are kept marked as
retired so previously downloaded artifacts remain verifiable.

If a published release ever fails verification against the documented public key, do
not run the binary. Report it to `security@fialr.com`.
