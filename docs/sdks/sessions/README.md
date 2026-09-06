# Sessions

## Overview

Run and inspect agent sessions.

### Available Operations

* [list_sessions](#list_sessions) - List sessions
* [get_session](#get_session) - Get a session with its messages
* [run_session](#run_session) - Run or resume a session
* [delete_session](#delete_session) - Delete a session
* [cancel_session](#cancel_session) - Cancel a session's running invocation
* [get_session_audit](#get_session_audit) - List a session's audit log

## list_sessions

Lists your organization's sessions, most recently used first. Filter by agent name, agent revision, invocation state, time window, or an invocation it ran: a session matches when any of its invocations does, and a filtered listing is ordered by each session's most recent matching invocation. A filter that matches nothing returns an empty page rather than an error.

Page with `after` and `limit`: pass the response's `next_cursor` as the next request's `after`, and keep requesting while `next_cursor` is present — you have reached the end when it is absent. A page can hold fewer sessions than `limit`, or none at all, and still have a `next_cursor`; a short page is not the end of the results.

A listing covers the window given by `since` and `until`, and omitting `since` searches the last 31 days. The window is fixed when the first page is requested, so paging with `after` keeps returning results from the window that page used: `after` carries that window and the filters it was made with, so send it with no filters, or with every filter repeated exactly, and expect a `400` otherwise.


### Example Usage

<!-- UsageSnippet language="python" operationID="listSessions" method="get" path="/sessions" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    x_albus_organization="<value>",
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.sessions.list_sessions(limit=25)

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
        x_albus_organization="<value>",
        access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
    ) as albus:

        res = await albus.sessions.list_sessions(limit=25)

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                                                                                      | Type                                                                                                                                                                                           | Required                                                                                                                                                                                       | Description                                                                                                                                                                                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_name`                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                             | Return only sessions that ran this agent (e.g. "support-triage").<br/>                                                                                                                         |
| `agent_revision`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                             | Return only sessions that ran this exact agent revision (e.g. "a1b2c3d4"). Requires `agent_name`; a revision without an agent name is a `400`.<br/>                                            |
| `status`                                                                                                                                                                                       | [Optional[models.SessionState]](../../models/sessionstate.md)                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                             | Return only sessions with an invocation that ended this way, or is `RUNNING` now. `DONE` matches a successful invocation.<br/>                                                                 |
| `invocation_key`                                                                                                                                                                               | *Optional[str]*                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                             | Return only the session that ran this invocation, whether it is still running or has ended.<br/>                                                                                               |
| `since`                                                                                                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                             | Return only sessions with an invocation that started at or after this time. Without `since` or `until`, the listing covers sessions used in the last 31 days; pass it to search further back.<br/> |
| `until`                                                                                                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                             | Return only sessions with an invocation that started at or before this time. Defaults to now, and must be after `since`; an earlier `until` is a `400`.<br/>                                   |
| `after`                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                             | Opaque pagination cursor. Return only items positioned after it; pass a value obtained from a previous page to fetch the next one.<br/>                                                        |
| `limit`                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                             | Maximum number of sessions to return. A page can be shorter, so page while `next_cursor` is present.<br/>                                                                                      |

### Response

**[models.ListSessionsResponse](../../models/listsessionsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
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
    x_albus_organization="<value>",
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
        x_albus_organization="<value>",
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

Runs the session with the given ID, creating it if it does not exist and resuming it otherwise. Each call is a single invocation, optionally named by the Idempotency-Key header, whose value is the invocation's key. Supplying a key makes the call safe to retry: retrying with the same key and an identical body re-attaches to the in-flight invocation and returns its current state; a differing body for the same key returns 409; a new key while another invocation is still running returns 423. Omitting the header starts a fresh, non-idempotent invocation each time; the server generates a key and returns it in the Idempotency-Key response header.

With `wait_timeout_seconds` the request long-polls: it blocks until the invocation's assistant response is available and returns it in `message`. Omit it to wait up to 30 minutes, or pass 0 to return as soon as the invocation is accepted. A positive value bounds the wait in seconds; if it elapses first the request fails with 504 and a JSON body, letting the client distinguish an expected server-side timeout from a transport error; the client may retry.


### Example Usage

<!-- UsageSnippet language="python" operationID="runSession" method="post" path="/sessions/{id}" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    x_albus_organization="<value>",
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
        x_albus_organization="<value>",
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

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                    | Client-provided session identifier. Use the same value across requests to continue the same agent session.                                                                                                                                                                                                                                                                                                                            |
| `user_prompt`                                                                                                                                                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                    | The user prompt driving this invocation.                                                                                                                                                                                                                                                                                                                                                                                              |
| `agent_name`                                                                                                                                                                                                                                                                                                                                                                                                                          | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                    | Human-readable name identifying the agent (e.g. "support-triage"). Invocations sharing a name are grouped as one agent; each distinct configuration under it becomes a revision.<br/>                                                                                                                                                                                                                                                 |
| `agent`                                                                                                                                                                                                                                                                                                                                                                                                                               | [models.AgentConfig](../../models/agentconfig.md)                                                                                                                                                                                                                                                                                                                                                                                     | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                    | The agent configuration for an invocation: the model, tools, instructions, and MCP servers that define its behavior. Invocations with the same configuration share a revision.<br/>                                                                                                                                                                                                                                                   |
| `invocation_key`                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                    | Optional but strongly encouraged. The key naming this invocation of the session, unique within your organization: reuse the same value to safely retry a request, read the invocation back with `GET /traces/{invocation_key}`, and use a new value to start a new invocation. When omitted, the server generates a key for the invocation and returns it in the Idempotency-Key response header, but the request is not retry-safe.<br/> |
| `wait_timeout_seconds`                                                                                                                                                                                                                                                                                                                                                                                                                | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                    | Wait up to this many seconds for the assistant response. Omit to wait up to 30 minutes; use 0 to return after the invocation is accepted.<br/>                                                                                                                                                                                                                                                                                        |
| `retry_config`                                                                                                                                                                                                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                    | Override the SDK retry configuration for this invocation.                                                                                                                                                                                                                                                                                                                                                                   |

### Response

**[operations.RunSessionResponse](../../operations/runsessionresponse.md)**

### Errors

| Error Type                   | Status Code                  | Content Type                 |
| ---------------------------- | ---------------------------- | ---------------------------- |
| errors.ErrBadRequest         | 400                          | application/json             |
| errors.ErrUnauthorized       | 401                          | application/json             |
| errors.ErrInsufficientCredit | 402                          | application/json             |
| errors.ErrConflict           | 409                          | application/json             |
| errors.ErrInvocationCanceled | 410                          | application/json             |
| errors.ErrLocked             | 423                          | application/json             |
| errors.ErrInvocationFailed   | 502                          | application/json             |
| errors.ErrTimeout            | 504                          | application/json             |
| errors.AlbusDefaultError     | 4XX, 5XX                     | \*/\*                        |

## delete_session

Delete a session

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSession" method="delete" path="/sessions/{id}" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    x_albus_organization="<value>",
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
        x_albus_organization="<value>",
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

## cancel_session

Requests cancellation of the invocation currently running for the session. Cancellation is asynchronous: the call returns once the request is accepted, and the invocation resolves as canceled shortly after, unlocking the session for new invocations. A request waiting on the invocation receives its terminal outcome. Returns 409 when the session has no invocation running.


### Example Usage

<!-- UsageSnippet language="python" operationID="cancelSession" method="post" path="/sessions/{id}/cancel" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    x_albus_organization="<value>",
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.sessions.cancel_session(id="<id>")

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
        x_albus_organization="<value>",
        access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
    ) as albus:

        res = await albus.sessions.cancel_session(id="<id>")

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                       | *str*                                                                                                      | :heavy_check_mark:                                                                                         | Client-provided session identifier. Use the same value across requests to continue the same agent session. |

### Response

**[models.CancelSessionResponse](../../models/cancelsessionresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.ErrConflict       | 409                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## get_session_audit

Returns the session's audit log — an immutable, time-ordered record of what happened during its invocations (LLM calls, tool results, and invocation outcomes). Events are ordered by the time they occurred. Use `after` and `limit` to page through them; pass the response's `next_cursor` as the next request's `after` to fetch the following page.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSessionAudit" method="get" path="/sessions/{id}/audit" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    x_albus_organization="<value>",
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
        x_albus_organization="<value>",
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
