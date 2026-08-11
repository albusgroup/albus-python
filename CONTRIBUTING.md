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

## This repository is a mirror

The SDK is developed in the private Albus repository, alongside the
`api/openapi.yaml` contract it is generated from, and each release is copied
here. This repository does not accept pull requests: a change merged here is
removed by the next release, so one opened here is commented on and closed
automatically.

Issues are the right channel, and they are read. Maintainers fix the problem
upstream, and the fix arrives in the next published version, which closes the
issue.

## Generated-code ownership

Speakeasy generates the SDK implementation, model and endpoint documentation,
package metadata, and the generation lock files from the OpenAPI contract.
Everything under `src/` and `docs/` is generated output, so a fix belongs in
the specification or in the generator configuration, never in the generated
file.

See [RELEASING.md](RELEASING.md) for how a version is produced and published.
