# Releasing the Python SDK

Releases are intentionally manual during the MVP. The repository provides a
guarded publisher, but it does not create commits, tags, GitHub releases, or
PyPI credentials.

## One-time PyPI setup

1. Create a PyPI account, verify its email address, enable two-factor
   authentication, and save the recovery codes.
2. Create an account-scoped API token for the first release. A project-scoped
   token cannot be created until `albus-sdk` exists on PyPI.
3. After the first release, invite another Albus maintainer as an owner and
   replace the account-scoped token with a token limited to `albus-sdk`.

TestPyPI has separate accounts and API tokens. It is useful for proving the
upload path, but its package and dependency data are independent from PyPI.

Never put an API token in this repository, a command-line argument, a shell
history entry, or a pull request.

## Prepare a release

1. Regenerate the SDK on a branch using the new normalized PEP 440 version:

   ```bash
   ./tools/generate /path/to/albus/api/openapi.yaml 0.1.0
   ```

2. Review the OpenAPI snapshot and generated diff, then merge the pull request.
3. On a clean, up-to-date `master`, validate the complete release:

   ```bash
   ./tools/publish --dry-run 0.1.0
   ```

The publisher checks that all generated version sources agree, the worktree is
clean, the current commit is pushed, and the build contains exactly one wheel
and one source distribution. It also runs the complete test suite and prints
the SHA-256 digest of each artifact.

## Publish

Read the token without displaying it or storing it in shell history:

```bash
read -s UV_PUBLISH_TOKEN
export UV_PUBLISH_TOKEN
```

An optional TestPyPI upload uses the same checks and requires a separate
TestPyPI token:

```bash
./tools/publish --testpypi 0.1.0
```

Publish to production from `master`:

```bash
./tools/publish 0.1.0
```

Both upload commands require typing the exact repository and version shown in
the confirmation prompt. Unset the credential immediately afterward:

```bash
unset UV_PUBLISH_TOKEN
```

Finally, verify that the exact release installs from PyPI:

```bash
uv run \
  --isolated \
  --no-project \
  --with albus-sdk==0.1.0 \
  python -c 'import albus_sdk; print(albus_sdk.VERSION)'
```

Published PyPI versions and files are immutable. Fix a bad release with a new
version rather than trying to replace its artifacts.
