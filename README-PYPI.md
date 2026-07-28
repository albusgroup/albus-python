# albus-sdk

Official, type-safe Python SDK for the Albus API.

[![Built by Speakeasy](https://img.shields.io/badge/Built_by-SPEAKEASY-374151?style=for-the-badge&labelColor=f3f4f6)](https://www.speakeasy.com/?utm_source=albus-sdk&utm_campaign=python)
[![License: MIT](https://img.shields.io/badge/LICENSE_//_MIT-3b5bdb?style=for-the-badge&labelColor=eff6ff)](https://opensource.org/licenses/MIT)

<!-- Start Summary [summary] -->
## Summary

Albus API: Albus service REST API
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [albus-sdk](https://github.com/albusgroup/albus-python/blob/master/#albus-sdk)
  * [SDK Installation](https://github.com/albusgroup/albus-python/blob/master/#sdk-installation)
  * [IDE Support](https://github.com/albusgroup/albus-python/blob/master/#ide-support)
  * [SDK Example Usage](https://github.com/albusgroup/albus-python/blob/master/#sdk-example-usage)
  * [Authentication](https://github.com/albusgroup/albus-python/blob/master/#authentication)
  * [Available Resources and Operations](https://github.com/albusgroup/albus-python/blob/master/#available-resources-and-operations)
  * [Retries](https://github.com/albusgroup/albus-python/blob/master/#retries)
  * [Error Handling](https://github.com/albusgroup/albus-python/blob/master/#error-handling)
  * [Server Selection](https://github.com/albusgroup/albus-python/blob/master/#server-selection)
  * [Custom HTTP Client](https://github.com/albusgroup/albus-python/blob/master/#custom-http-client)
  * [Resource Management](https://github.com/albusgroup/albus-python/blob/master/#resource-management)
  * [Debugging](https://github.com/albusgroup/albus-python/blob/master/#debugging)
* [Development](https://github.com/albusgroup/albus-python/blob/master/#development)
  * [Maturity](https://github.com/albusgroup/albus-python/blob/master/#maturity)
  * [Contributions](https://github.com/albusgroup/albus-python/blob/master/#contributions)

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
uv add git+https://github.com/albusgroup/albus-python.git
```

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+https://github.com/albusgroup/albus-python.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+https://github.com/albusgroup/albus-python.git
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
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.secrets.list_secrets()

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
from albus_sdk import Albus, models
import asyncio
import os

async def main():

    async with Albus(
        security=models.Security(
            bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
        ),
    ) as albus:

        res = await albus.secrets.list_secrets_async()

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

You can set the security parameters through the `security` optional parameter when initializing the SDK client instance. The selected scheme will be used by default to authenticate with the API for all operations that support it. For example:
```python
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.secrets.list_secrets()

    # Handle response
    print(res)

```
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [Auth](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/auth/README.md)

* [whoami](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/auth/README.md#whoami) - Get current user information

### [Health](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/health/README.md)

* [health](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/health/README.md#health) - Health check endpoint

### [Secrets](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/secrets/README.md)

* [list_secrets](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/secrets/README.md#list_secrets) - List all secrets
* [create_secret](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/secrets/README.md#create_secret) - Create a secret
* [get_secret](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/secrets/README.md#get_secret) - Get a secret by name
* [update_secret](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/secrets/README.md#update_secret) - Update a secret by name
* [delete_secret](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/secrets/README.md#delete_secret) - Delete a secret by name

### [Sessions](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/sessions/README.md)

* [list_sessions](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/sessions/README.md#list_sessions) - List all sessions
* [get_session](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/sessions/README.md#get_session) - Get a session with its messages
* [run_session](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/sessions/README.md#run_session) - Run or resume a session
* [delete_session](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/sessions/README.md#delete_session) - Delete a session
* [get_session_audit](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/sessions/README.md#get_session_audit) - List a session's audit log

### [Tokens](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/tokens/README.md)

* [list_tokens](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/tokens/README.md#list_tokens) - List all API tokens. Never returns token values, only metadata.
* [create_token](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/tokens/README.md#create_token) - Create an API token. The token value is returned only in this response.
* [get_token](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/tokens/README.md#get_token) - Get token metadata by ID. Never returns the token value.
* [delete_token](https://github.com/albusgroup/albus-python/blob/master/docs/sdks/tokens/README.md#delete_token) - Revoke an API token by ID

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from albus_sdk import Albus, models
from albus_sdk.utils import BackoffStrategy, RetryConfig
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.secrets.list_secrets(,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from albus_sdk import Albus, models
from albus_sdk.utils import BackoffStrategy, RetryConfig
import os


with Albus(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.secrets.list_secrets()

    # Handle response
    print(res)

```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

[`AlbusError`](https://github.com/albusgroup/albus-python/blob/master/./src/albus_sdk/errors/albuserror.py) is the base class for all HTTP error responses. It has the following properties:

| Property           | Type             | Description                                                                             |
| ------------------ | ---------------- | --------------------------------------------------------------------------------------- |
| `err.message`      | `str`            | Error message                                                                           |
| `err.status_code`  | `int`            | HTTP response status code eg `404`                                                      |
| `err.headers`      | `httpx.Headers`  | HTTP response headers                                                                   |
| `err.body`         | `str`            | HTTP body. Can be empty string if no body is returned.                                  |
| `err.raw_response` | `httpx.Response` | Raw HTTP response                                                                       |
| `err.data`         |                  | Optional. Some errors may contain structured data. [See Error Classes](https://github.com/albusgroup/albus-python/blob/master/#error-classes). |

### Example
```python
from albus_sdk import Albus, errors, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
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

### Error Classes
**Primary errors:**
* [`AlbusError`](https://github.com/albusgroup/albus-python/blob/master/./src/albus_sdk/errors/albuserror.py): The base class for HTTP error responses.
  * [`ErrUnauthorized`](https://github.com/albusgroup/albus-python/blob/master/./src/albus_sdk/errors/errunauthorized.py): Status code `401`. *

<details><summary>Less common errors (12)</summary>

<br />

**Network errors:**
* [`httpx.RequestError`](https://www.python-httpx.org/exceptions/#httpx.RequestError): Base class for request errors.
    * [`httpx.ConnectError`](https://www.python-httpx.org/exceptions/#httpx.ConnectError): HTTP client was unable to make a request to a server.
    * [`httpx.TimeoutException`](https://www.python-httpx.org/exceptions/#httpx.TimeoutException): HTTP request timed out.


**Inherit from [`AlbusError`](https://github.com/albusgroup/albus-python/blob/master/./src/albus_sdk/errors/albuserror.py)**:
* [`ErrNotFound`](https://github.com/albusgroup/albus-python/blob/master/./src/albus_sdk/errors/errnotfound.py): Not found. Status code `404`. Applicable to 8 of 16 methods.*
* [`ErrBadRequest`](https://github.com/albusgroup/albus-python/blob/master/./src/albus_sdk/errors/errbadrequest.py): Status code `400`. Applicable to 5 of 16 methods.*
* [`ErrConflict`](https://github.com/albusgroup/albus-python/blob/master/./src/albus_sdk/errors/errconflict.py): Idempotency key reused with a different request body. Status code `409`. Applicable to 1 of 16 methods.*
* [`ErrLocked`](https://github.com/albusgroup/albus-python/blob/master/./src/albus_sdk/errors/errlocked.py): Another invocation is currently running for this session. Status code `423`. Applicable to 1 of 16 methods.*
* [`ErrRunFailed`](https://github.com/albusgroup/albus-python/blob/master/./src/albus_sdk/errors/errrunfailed.py): The harness run failed instead of producing a response (only possible with wait=true, or when replaying a failed invocation). The body carries the failure kind and detail. Status code `502`. Applicable to 1 of 16 methods.*
* [`HealthResponseError`](https://github.com/albusgroup/albus-python/blob/master/./src/albus_sdk/errors/healthresponseerror.py): Service is healthy. Status code `503`. Applicable to 1 of 16 methods.*
* [`ErrTimeout`](https://github.com/albusgroup/albus-python/blob/master/./src/albus_sdk/errors/errtimeout.py): Timed out waiting for the assistant response. Status code `504`. Applicable to 1 of 16 methods.*
* [`ResponseValidationError`](https://github.com/albusgroup/albus-python/blob/master/./src/albus_sdk/errors/responsevalidationerror.py): Type mismatch between the response data and the expected Pydantic model. Provides access to the Pydantic validation error via the `cause` attribute.

</details>

\* Check [the method documentation](https://github.com/albusgroup/albus-python/blob/master/#available-resources-and-operations) to see if the error is applicable.
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
from albus_sdk import Albus, models
import os


with Albus(
    server_idx=0,
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.secrets.list_secrets()

    # Handle response
    print(res)

```

### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from albus_sdk import Albus, models
import os


with Albus(
    server_url="http://localhost:8080",
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.secrets.list_secrets()

    # Handle response
    print(res)

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

The `Albus` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from albus_sdk import Albus, models
import os
def main():

    with Albus(
        security=models.Security(
            bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
        ),
    ) as albus:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Albus(
        security=models.Security(
            bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
        ),
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

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation.
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release.

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=albus-sdk&utm_campaign=python)
