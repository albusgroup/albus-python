# Releasing the Python SDK

Releases are intentionally manual during the MVP. The repository provides a
guarded publisher, but it does not create commits, tags, GitHub releases, or
PyPI credentials.

## One-time PyPI setup

1. Create a PyPI account, verify its email address, enable two-factor
   authentication, and save the recovery codes.
2. Ask an existing owner to add the maintainer to the `albus-sdk` project.
3. Create an API token limited to the `albus-sdk` project and store it in a
   password manager. Revoke any account-scoped token used to bootstrap the
   first release.

TestPyPI has separate accounts and API tokens. It is useful for proving the
upload path, but its package and dependency data are independent from PyPI.

Never put an API token in this repository, a command-line argument, a shell
history entry, or a pull request.

## Choose a version

Use a normalized PEP 440 version. During the pre-1.0 MVP:

- Increment the patch version for compatible SDK fixes, documentation-only
  regeneration, and other compatible changes.
- Increment the minor version for additive API changes.
- Increment the minor version for intentional breaking API changes and call
  out the breakage in the pull request.

Confirm the version before generation. Published versions cannot be reused.

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

Finally, verify that the exact release installs from PyPI in a clean
environment:

```bash
python3 -m venv .tmp/albus-sdk-verify
.tmp/albus-sdk-verify/bin/python -m pip install albus-sdk==0.1.0
.tmp/albus-sdk-verify/bin/python -c \
  'import albus_sdk; print(albus_sdk.VERSION)'
```

If another package manager does not see a release that is visible on PyPI,
refresh its package-index cache before retrying.

Published PyPI versions and files are immutable. Fix a bad release with a new
version rather than trying to replace its artifacts.
