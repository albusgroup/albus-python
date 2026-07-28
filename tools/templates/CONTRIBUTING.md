# Contributing to albus-python

Thanks for helping improve the Albus Python SDK.

## Report a problem

Open a [GitHub issue](https://github.com/albusgroup/albus-python/issues) with:

- The installed `albus-sdk` and Python versions.
- A minimal example that reproduces the problem.
- The expected and actual behavior.
- The exception type, response status, and sanitized logs when relevant.

Do not include access tokens, organization keys, secret values, or other
sensitive data.

Report suspected vulnerabilities privately by following
[SECURITY.md](SECURITY.md), not by opening a public issue.

## Generated-code ownership

The API contract is maintained in the private Albus repository at
`api/openapi.yaml`. Speakeasy generates the SDK implementation, model and
endpoint documentation, package metadata, and its generation lock files from
that contract.

Changes made directly to generated files under `src/` or `docs/` will be
overwritten. Pull requests should normally change one of these instead:

- The authoritative OpenAPI specification, for API behavior or documentation.
- `.speakeasy/gen.yaml`, for generator behavior.
- `tools/`, `tests/`, or the handwritten sections of `README.md`, for this
  repository's release workflow, checks, and usage guidance.

Maintainers regenerate with:

```bash
./tools/generate /path/to/albus/api/openapi.yaml 0.1.0
```

The specification snapshot, generated output, documentation, and lock files
must be reviewed and committed together. See [RELEASING.md](RELEASING.md) for
the manual publishing process.
