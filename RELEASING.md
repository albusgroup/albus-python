# Releasing the Python SDK

Run everything below from `clients/albus-python/` in the Albus repository,
which is where the SDK is developed; the public `albus-python` repository is a
mirror written by the release.

A release is a maintainer running the scripts below from a clean, up-to-date
`master` checkout: they run `./tools/check`, upload to PyPI or TestPyPI, push
the released tree to the public mirror as a single tagged commit, and close the
mirror issues the release fixes. Nothing publishes from CI, on push, on tag, or
on merge.

## One-time PyPI setup

1. Create a PyPI account, verify its email address, enable two-factor
   authentication, and save the recovery codes.
2. Ask an existing owner to add the maintainer to the `albus-sdk` project.
3. Create an API token limited to the `albus-sdk` project, and store it in a
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
   ./tools/generate 0.1.0
   ```

   The source is this repository's `api/openapi.yaml`.

2. Review the OpenAPI snapshot and generated diff, then merge the pull request.
   Give any commit that fixes a publicly reported bug a
   `Mirror-Issue: albusgroup/albus-python#<number>` trailer — that trailer is
   what closes the reporter's issue when the fix ships.
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

## The public mirror

`albusgroup/albus-python` is written by the release, never edited directly:

```bash
./tools/mirror-release --dry-run 0.1.0 /path/to/albus-python
./tools/mirror-release 0.1.0 /path/to/albus-python
```

The script replaces the mirror's tree with the tracked contents of
`clients/albus-python` (minus `AGENTS.md` and `.vscode/`), commits it as one
commit recording the released `Source-Commit`, tags it `v<version>`, pushes
`master` and the tag atomically, and then closes every
`albusgroup/albus-python` issue named by a `Mirror-Issue` trailer added since
the previous release, commenting with the published version.

It needs push access to the mirror and a `gh` login that can close its issues —
the same credentials a maintainer already has, since the release does not run
from CI.

The checkout you pass is only read: the release commit is built in a throwaway
clone of it, so a rejected push leaves nothing to unwind and the command is
simply run again. Pull the checkout afterwards to see the release in it.
