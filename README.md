# albus-sdk

Official, type-safe Python SDK for the Albus API.

[![Built by Speakeasy](https://img.shields.io/badge/Built_by-SPEAKEASY-374151?style=for-the-badge&labelColor=f3f4f6)](https://www.speakeasy.com/?utm_source=albus-sdk&utm_campaign=python)
[![License: MIT](https://img.shields.io/badge/LICENSE_//_MIT-3b5bdb?style=for-the-badge&labelColor=eff6ff)](https://opensource.org/licenses/MIT)

## Quickstart

Install the SDK from PyPI:

```bash
pip install albus-sdk
```

Session operations use an organization API key:

```python
import os

from albus_sdk import Albus, models


with Albus(
    api_key=os.environ["ALBUS_API_KEY_AUTH"],
) as albus:
    response = albus.sessions.list_sessions()
    print(response.sessions)
```

Run or resume a session by ID, and wait for the assistant response:

```python
import os

from albus_sdk import Albus, models


with Albus(
    api_key=os.environ["ALBUS_API_KEY_AUTH"],
    timeout_ms=130_000,
) as albus:
    response = albus.sessions.run_session(
        id="support-triage-1",
        user_prompt="Summarize the latest ticket.",
        agent_name="support-triage",
        agent=models.AgentConfig(
            model=models.Model(name="gemini-3.6-flash"),
        ),
        wait_timeout_seconds=120,
    )
    print(response.result.messages)
```

Omit `wait_timeout_seconds` to return as soon as the invocation is accepted, and
pass 0 to wait until the response arrives. Waiting long-polls, so construct the
client with a `timeout_ms` above the longest wait — it is a client-wide setting,
and the underlying HTTP client otherwise gives up after its own 5-second default.

User and token operations use a user bearer token. `AsyncAlbus` exposes the same
operations as coroutines:

```python
import asyncio
import os

from albus_sdk import AsyncAlbus, models


async def main() -> None:
    async with AsyncAlbus(
        access_token=os.environ["ALBUS_BEARER_AUTH"],
    ) as albus:
        response = await albus.auth.whoami()
        print(response)


asyncio.run(main())
```

Secret operations accept either credential. The SDK also reads
`ALBUS_API_KEY_AUTH` and `ALBUS_BEARER_AUTH` directly from the environment, so
`Albus()` is sufficient when the appropriate variable is set. Production
requests use `https://albus.sh/api` by default.

<!-- Start Summary [summary] -->
## Summary

Albus API: Albus service REST API
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [albus-sdk](#albus-sdk)
  * [Quickstart](#quickstart)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Regeneration](#regeneration)
  * [Checks](#checks)
  * [Releases](#releases)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with *uv*, *pip*, or *poetry* package managers.

### uv

*uv* is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's recommended for its speed and modern Python tooling capabilities.

```bash
uv add albus-sdk
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install albus-sdk
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add albus-sdk
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from albus-sdk python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "albus-sdk",
# ]
# ///

from albus_sdk import Albus

sdk = Albus(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.secrets.list_secrets()

    # Handle response
    print(res)
```

</br>

An Async SDK client can also be used to make asynchronous requests by importing it and asyncio.

```python
# Asynchronous Example
from albus_sdk import AsyncAlbus, models
import asyncio
import os

async def main():

    async with AsyncAlbus(
        access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
    ) as albus:

        res = await albus.secrets.list_secrets()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security schemes globally:

| Name           | Type | Scheme      | Environment Variable |
| -------------- | ---- | ----------- | -------------------- |
| `bearer_auth`  | http | HTTP Bearer | `ALBUS_BEARER_AUTH`  |
| `api_key_auth` | http | HTTP Bearer | `ALBUS_API_KEY_AUTH` |

Pass an organization API key with `api_key`, or a user access token with `access_token`. The SDK sends the corresponding bearer credential for every operation that supports it. For example:
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.secrets.list_secrets()

    # Handle response
    print(res)
```

</br>

An Async SDK client can also be used to make asynchronous requests by importing it and asyncio.

```python
# Asynchronous Example
from albus_sdk import AsyncAlbus, models
import asyncio
import os

async def main():

    async with AsyncAlbus(
        access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
    ) as albus:

        res = await albus.secrets.list_secrets()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Agents](docs/sdks/agents/README.md)

* [list_agents](docs/sdks/agents/README.md#list_agents) - List agents
* [get_agent](docs/sdks/agents/README.md#get_agent) - Get an agent by name
* [get_agent_revision](docs/sdks/agents/README.md#get_agent_revision) - Get a specific revision of an agent

### [Auth](docs/sdks/auth/README.md)

* [whoami](docs/sdks/auth/README.md#whoami) - Get current user information

### [Health](docs/sdks/health/README.md)

* [health](docs/sdks/health/README.md#health) - Health check endpoint

### [Invites](docs/sdks/invites/README.md)

* [create_invite](docs/sdks/invites/README.md#create_invite) - Invite a user by email

### [Models](docs/sdks/models/README.md)

* [list_models](docs/sdks/models/README.md#list_models) - List models

### [Secrets](docs/sdks/secrets/README.md)

* [list_secrets](docs/sdks/secrets/README.md#list_secrets) - List all secrets
* [create_secret](docs/sdks/secrets/README.md#create_secret) - Create a secret
* [get_secret](docs/sdks/secrets/README.md#get_secret) - Get a secret by name
* [update_secret](docs/sdks/secrets/README.md#update_secret) - Update a secret by name
* [delete_secret](docs/sdks/secrets/README.md#delete_secret) - Delete a secret by name

### [Sessions](docs/sdks/sessions/README.md)

* [list_sessions](docs/sdks/sessions/README.md#list_sessions) - List all sessions
* [get_session](docs/sdks/sessions/README.md#get_session) - Get a session with its messages
* [run_session](docs/sdks/sessions/README.md#run_session) - Run or resume a session
* [delete_session](docs/sdks/sessions/README.md#delete_session) - Delete a session
* [get_session_audit](docs/sdks/sessions/README.md#get_session_audit) - List a session's audit log

### [Tokens](docs/sdks/tokens/README.md)

* [list_tokens](docs/sdks/tokens/README.md#list_tokens) - List all API tokens. Never returns token values, only metadata.
* [create_token](docs/sdks/tokens/README.md#create_token) - Create an API token. The token value is returned only in this response.
* [get_token](docs/sdks/tokens/README.md#get_token) - Get token metadata by ID. Never returns the token value.
* [delete_token](docs/sdks/tokens/README.md#delete_token) - Revoke an API token by ID

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Only `run_session` supports retries. Configure its default retry policy with
`retry_config` when constructing the SDK, or pass `retry_config` directly to a
single `run_session` invocation. Omit it to inherit the SDK default; pass
`None` to disable retries for that invocation.
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`AlbusError`](./src/albus_sdk/errors/albuserror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](#error-classes). |

### Example
```python
# Synchronous Example
from albus_sdk import Albus, errors, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:
    res = None
    try:

        res = albus.secrets.list_secrets()

        # Handle response
        print(res)


    except errors.AlbusError as e:
        # The base class for HTTP error responses
        print(e.message)
        print(e.status_code)
        print(e.body)
        print(e.headers)
        print(e.raw_response)

        # Depending on the method different errors may be thrown
        if isinstance(e, errors.ErrUnauthorized):
            print(e.data.message)  # str
```

</br>

An Async SDK client can also be used to make asynchronous requests by importing it and asyncio.

```python
# Asynchronous Example
from albus_sdk import AsyncAlbus, errors, models
import asyncio
import os

async def main():

    async with AsyncAlbus(
        access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
    ) as albus:
        res = None
        try:

            res = await albus.secrets.list_secrets()

            # Handle response
            print(res)


            except errors.AlbusError as e:
                # The base class for HTTP error responses
                print(e.message)
                print(e.status_code)
                print(e.body)
                print(e.headers)
                print(e.raw_response)

                # Depending on the method different errors may be thrown
                if isinstance(e, errors.ErrUnauthorized):
                    print(e.data.message)  # str

asyncio.run(main())
```

### Error Classes
**Primary errors:**
* [`AlbusError`](./src/albus_sdk/errors/albuserror.py): The base class for HTTP error responses.
  * [`ErrUnauthorized`](./src/albus_sdk/errors/errunauthorized.py): Status code `401`. *

<details><summary>Less common errors (13)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`AlbusError`](./src/albus_sdk/errors/albuserror.py)**:
* [`ErrNotFound`](./src/albus_sdk/errors/errnotfound.py): Not found. Status code `404`. Applicable to 10 of 21 methods.*
* [`ErrBadRequest`](./src/albus_sdk/errors/errbadrequest.py): Status code `400`. Applicable to 6 of 21 methods.*
* [`ErrConflict`](./src/albus_sdk/errors/errconflict.py): Status code `409`. Applicable to 2 of 21 methods.*
* [`ErrLocked`](./src/albus_sdk/errors/errlocked.py): Another invocation is currently running for this session. Status code `423`. Applicable to 1 of 21 methods.*
* [`ErrQuotaExceeded`](./src/albus_sdk/errors/errquotaexceeded.py): The organization has reached its invocation quota. Status code `429`. Applicable to 1 of 21 methods.*
* [`ErrRunFailed`](./src/albus_sdk/errors/errrunfailed.py): The harness run failed instead of producing a response (only possible while waiting for a response, or when replaying a failed invocation). The body carries the failure kind and detail. Status code `502`. Applicable to 1 of 21 methods.*
* [`HealthResponseError`](./src/albus_sdk/errors/healthresponseerror.py): Service is healthy. Status code `503`. Applicable to 1 of 21 methods.*
* [`ErrTimeout`](./src/albus_sdk/errors/errtimeout.py): Timed out waiting for the assistant response. Status code `504`. Applicable to 1 of 21 methods.*
* [`ResponseValidationError`](./src/albus_sdk/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](#available-resources-and-operations) to see if the error is applicable.
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| #   | Server                  | Description              |
| --- | ----------------------- | ------------------------ |
| 0   | `https://albus.sh/api`  | Production server        |
| 1   | `http://localhost:8080` | Local development server |

#### Example

```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    server_idx=0,
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.secrets.list_secrets()

    # Handle response
    print(res)
```

</br>

An Async SDK client can also be used to make asynchronous requests by importing it and asyncio.

```python
# Asynchronous Example
from albus_sdk import AsyncAlbus, models
import asyncio
import os

async def main():

    async with AsyncAlbus(
        server_idx=0,
        access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
    ) as albus:

        res = await albus.secrets.list_secrets()

        # Handle response
        print(res)

asyncio.run(main())
```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    server_url="http://localhost:8080",
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.secrets.list_secrets()

    # Handle response
    print(res)
```

</br>

An Async SDK client can also be used to make asynchronous requests by importing it and asyncio.

```python
# Asynchronous Example
from albus_sdk import AsyncAlbus, models
import asyncio
import os

async def main():

    async with AsyncAlbus(
        server_url="http://localhost:8080",
        access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
    ) as albus:

        res = await albus.secrets.list_secrets()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from albus_sdk import Albus
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Albus(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from albus_sdk import Albus
from albus_sdk.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Albus(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Albus` and `AsyncAlbus` classes implement the context manager protocol and register finalizer functions to close the underlying HTTPX clients they use under the hood. This will close HTTP connections, release memory and free up other resources held by the SDKs. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create SDK instances via [context managers][context-manager] and reuse them across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from albus_sdk import Albus, AsyncAlbus, models
import os
def main():

    with Albus(
        access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
    ) as albus:
        # Rest of application here...


# Or when using async:
async def amain():

    async with AsyncAlbus(
        access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
    ) as albus:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from albus_sdk import Albus
import logging

logging.basicConfig(level=logging.DEBUG)
s = Albus(debug_logger=logging.getLogger("albus_sdk"))
```

You can also enable a default debug logger by setting an environment variable `ALBUS_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Regeneration

Regeneration requires `uv`, Speakeasy authentication, and the Speakeasy CLI
version pinned in `.speakeasy/workflow.yaml`.

Run the generator with the SDK version to produce:

```bash
./tools/generate 0.1.0
```

The source is the authoritative `api/openapi.yaml` in the Albus repository,
where this SDK is developed; pass a path as a second argument only to preview
against a different specification.

The command copies the exact specification snapshot into this repository,
generates the SDK without uploading the specification, normalizes known
generator metadata, and runs the complete local check. Review and commit the
specification, generated code, documentation, and lock files together.

## Checks

Install `uv` and the pinned Speakeasy CLI, then run the complete local check:

```bash
./tools/check
```

This lints the OpenAPI snapshot, checks the generated package with MyPy and
Pyright, runs the handwritten tests, builds both package formats, validates
their metadata, and installs the wheel on Python 3.10 and 3.14.

## Releases

Publishing is manual during the MVP. Follow [RELEASING.md](RELEASING.md) to
validate and publish a generated version with the guarded local script.

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation.
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release.

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=albus-sdk&utm_campaign=python)
