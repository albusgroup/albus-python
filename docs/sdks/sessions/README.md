# Sessions

## Overview

Run and inspect agent sessions.

### Available Operations

* [list_sessions](#list_sessions) - List all sessions
* [get_session](#get_session) - Get a session with its messages
* [run_session](#run_session) - Run or resume a session
* [delete_session](#delete_session) - Delete a session
* [get_session_audit](#get_session_audit) - List a session's audit log

## list_sessions

List all sessions

### Example Usage

<!-- UsageSnippet language="python" operationID="listSessions" method="get" path="/sessions" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.sessions.list_sessions()

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

        res = await albus.sessions.list_sessions()

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |

### Response

**[models.ListSessionsResponse](../../models/listsessionsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## get_session

Returns the session's metadata and a page of its messages ordered by cursor ascending. Use `after` and `limit` to page through messages.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSession" method="get" path="/sessions/{id}" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.sessions.get_session(id="<id>", limit=100)

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

        res = await albus.sessions.get_session(id="<id>", limit=100)

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Client-provided session identifier. Use the same value across requests to continue the same agent session.                          |
| `after`                                                                                                                             | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Opaque pagination cursor. Return only items positioned after it; pass a value obtained from a previous page to fetch the next one.<br/> |
| `limit`                                                                                                                             | *Optional[int]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Maximum number of items to return.                                                                                                  |

### Response

**[models.SessionResponse](../../models/sessionresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## run_session

Runs the session with the given ID, creating it if it does not exist and resuming it otherwise. Each call is a single invocation, optionally identified by the Idempotency-Key header. Supplying a key makes the call safe to retry: retrying with the same key and an identical body re-attaches to the in-flight invocation and returns its current state; a differing body for the same key returns 409; a new key while another invocation is still running returns 423. Omitting the header starts a fresh, non-idempotent invocation each time; the server generates a key and returns it in the Idempotency-Key response header.

With `wait_timeout_seconds` the request long-polls: it blocks until the invocation's assistant response is available and returns it in `message`. Omit it to wait up to 30 minutes, or pass 0 to return as soon as the invocation is accepted. A positive value bounds the wait in seconds; if it elapses first the request fails with 504 and a JSON body, letting the client distinguish an expected server-side timeout from a transport error; the client may retry.


### Example Usage

<!-- UsageSnippet language="python" operationID="runSession" method="post" path="/sessions/{id}" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.sessions.run_session(id="<id>", user_prompt="<value>", agent_name="<value>", agent={
        "model": {
            "name": "<value>",
        },
    }, wait_timeout_seconds=1800)

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

        res = await albus.sessions.run_session(id="<id>", user_prompt="<value>", agent_name="<value>", agent={
            "model": {
                "name": "<value>",
            },
        }, wait_timeout_seconds=1800)

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                    | Client-provided session identifier. Use the same value across requests to continue the same agent session.                                                                                                                                                                                                                            |
| `user_prompt`                                                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                    | The user prompt driving this invocation.                                                                                                                                                                                                                                                                                              |
| `agent_name`                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                    | Human-readable name identifying the agent (e.g. "support-triage"). Runs sharing a name are grouped as one agent; each distinct configuration under it becomes a revision.<br/>                                                                                                                                                        |
| `agent`                                                                                                                                                                                                                                                                                                                               | [models.AgentConfig](../../models/agentconfig.md)                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                    | The agent configuration for a run: the model, tools, instructions, and MCP servers that define its behavior. Runs with the same configuration share a revision.<br/>                                                                                                                                                                  |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                    | Optional but strongly encouraged. Uniquely identifies this invocation of the session; reuse the same value to safely retry a request, and a new value starts a new invocation. When omitted, the server generates a key for the invocation and returns it in the Idempotency-Key response header, but the request is not retry-safe.<br/> |
| `wait_timeout_seconds`                                                                                                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                    | Wait up to this many seconds for the assistant response. Omit to wait up to 30 minutes; use 0 to return after the invocation is accepted.<br/>                                                                                                                                                                                        |
| `retry_config`                                                                                                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                    | Override the SDK retry configuration for this invocation.                                                                                                                                                                                                                                                                   |

### Response

**[operations.RunSessionResponse](../../operations/runsessionresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrConflict       | 409                      | application/json         |
| errors.ErrLocked         | 423                      | application/json         |
| errors.ErrQuotaExceeded  | 429                      | application/json         |
| errors.ErrRunFailed      | 502                      | application/json         |
| errors.ErrTimeout        | 504                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## delete_session

Delete a session

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSession" method="delete" path="/sessions/{id}" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    albus.sessions.delete_session(id="<id>")

    # Use the SDK ...
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

        await albus.sessions.delete_session(id="<id>")

        # Use the SDK ...

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                       | *str*                                                                                                      | :heavy_check_mark:                                                                                         | Client-provided session identifier. Use the same value across requests to continue the same agent session. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## get_session_audit

Returns the session's audit log — an immutable, time-ordered record of what happened during its agent runs (LLM calls, tool results, and run outcomes). Events are ordered by the time they occurred. Use `after` and `limit` to page through them; pass the response's `next_cursor` as the next request's `after` to fetch the following page.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSessionAudit" method="get" path="/sessions/{id}/audit" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.sessions.get_session_audit(id="<id>", limit=100)

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

        res = await albus.sessions.get_session_audit(id="<id>", limit=100)

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Client-provided session identifier. Use the same value across requests to continue the same agent session.                          |
| `after`                                                                                                                             | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Opaque pagination cursor. Return only items positioned after it; pass a value obtained from a previous page to fetch the next one.<br/> |
| `limit`                                                                                                                             | *Optional[int]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Maximum number of items to return.                                                                                                  |

### Response

**[models.ListAuditEventsResponse](../../models/listauditeventsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
