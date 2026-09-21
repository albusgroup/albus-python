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

Returns sessions ordered by their most recent matching invocation.


### Example Usage

<!-- UsageSnippet language="python" operationID="listSessions" method="get" path="/sessions" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.sessions.list_sessions(limit=25)

    # Handle response
    print(res)
```

</br>

An Async SDK client can also be used to make asynchronous requests by importing it and asyncio.

```python
# Asynchronous Example
from albus_sdk import AsyncAlbus
import asyncio
import os

async def main():

    async with AsyncAlbus(
        api_key=os.getenv("ALBUS_API_KEY", ""),
    ) as albus:

        res = await albus.sessions.list_sessions(limit=25)

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_name`                                                                                                                                                     | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Return only sessions that ran this agent (e.g. "support-triage").<br/>                                                                                           |
| `agent_revision`                                                                                                                                                 | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Return only sessions that ran this agent revision (e.g. "a1b2c3d4"). Requires `agent_name`.<br/>                                                                 |
| `status`                                                                                                                                                         | [Optional[models.SessionState]](../../models/sessionstate.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                               | Return only sessions with an invocation in this state. `DONE` matches a successful invocation.<br/>                                                              |
| `invocation_key`                                                                                                                                                 | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Return only the session containing this invocation.<br/>                                                                                                         |
| `since`                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Return only sessions with an invocation that started at or after this time. Defaults to 31 days ago.<br/>                                                        |
| `until`                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Return only sessions with an invocation that started at or before this time. Defaults to now and must be after `since`.<br/>                                     |
| `after`                                                                                                                                                          | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Continue after this cursor. For list responses, pass the preceding page's `next_cursor`; for session messages, pass the preceding page's last message `cursor`.<br/> |
| `limit`                                                                                                                                                          | *Optional[int]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Maximum number of sessions to return.                                                                                                                            |

### Response

**[models.ListSessionsResponse](../../models/listsessionsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## get_session

Returns session metadata and messages in chronological order.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSession" method="get" path="/sessions/{id}" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.sessions.get_session(id="<id>", limit=100)

    # Handle response
    print(res)
```

</br>

An Async SDK client can also be used to make asynchronous requests by importing it and asyncio.

```python
# Asynchronous Example
from albus_sdk import AsyncAlbus
import asyncio
import os

async def main():

    async with AsyncAlbus(
        api_key=os.getenv("ALBUS_API_KEY", ""),
    ) as albus:

        res = await albus.sessions.get_session(id="<id>", limit=100)

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | Client-provided session identifier. Reuse it to continue the session.<br/>                                                                                       |
| `after`                                                                                                                                                          | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Continue after this cursor. For list responses, pass the preceding page's `next_cursor`; for session messages, pass the preceding page's last message `cursor`.<br/> |
| `limit`                                                                                                                                                          | *Optional[int]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Maximum number of items to return.                                                                                                                               |

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

Starts a new session or continues an existing one with another agent invocation.


### Example Usage

<!-- UsageSnippet language="python" operationID="runSession" method="post" path="/sessions/{id}" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
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
from albus_sdk import AsyncAlbus
import asyncio
import os

async def main():

    async with AsyncAlbus(
        api_key=os.getenv("ALBUS_API_KEY", ""),
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

| Parameter                                                                                                                                                                                          | Type                                                                                                                                                                                               | Required                                                                                                                                                                                           | Description                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                               | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | Client-provided session identifier. Reuse it to continue the session.<br/>                                                                                                                         |
| `user_prompt`                                                                                                                                                                                      | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | The user prompt driving this invocation.                                                                                                                                                           |
| `agent_name`                                                                                                                                                                                       | *str*                                                                                                                                                                                              | :heavy_check_mark:                                                                                                                                                                                 | Human-readable name identifying the agent (e.g. "support-triage"). Invocations sharing a name are grouped as one agent; each distinct configuration under it becomes a revision.<br/>              |
| `agent`                                                                                                                                                                                            | [models.AgentConfig](../../models/agentconfig.md)                                                                                                                                                  | :heavy_check_mark:                                                                                                                                                                                 | The agent configuration for an invocation: the model, tools, instructions, and MCP servers that define its behavior. Invocations with the same configuration share a revision.<br/>                |
| `invocation_key`                                                                                                                                                                                   | *Optional[str]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | Names the invocation and makes identical requests safe to retry. Reuse with a different body returns `409`. When omitted, the response returns a generated key and the request is not retry-safe.<br/> |
| `wait_timeout_seconds`                                                                                                                                                                             | *Optional[int]*                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                 | Wait up to this many seconds for the assistant response. Omit to wait 30 minutes; use 0 to return once accepted. A timeout does not stop the invocation.<br/>                                      |
| `retry_config`                                                                                                                                                                                          | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                 | Override the SDK retry configuration for this invocation.                                                                                                                                |

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

Removes the session's messages, invocations, and external resources, marks it deleted, and keeps its audit log readable.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSession" method="delete" path="/sessions/{id}" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    albus.sessions.delete_session(id="<id>")

    # Use the SDK ...
```

</br>

An Async SDK client can also be used to make asynchronous requests by importing it and asyncio.

```python
# Asynchronous Example
from albus_sdk import AsyncAlbus
import asyncio
import os

async def main():

    async with AsyncAlbus(
        api_key=os.getenv("ALBUS_API_KEY", ""),
    ) as albus:

        await albus.sessions.delete_session(id="<id>")

        # Use the SDK ...

asyncio.run(main())
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Client-provided session identifier. Reuse it to continue the session.<br/> |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.ErrConflict       | 409                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## cancel_session

Requests asynchronous cancellation and returns once accepted.


### Example Usage

<!-- UsageSnippet language="python" operationID="cancelSession" method="post" path="/sessions/{id}/cancel" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.sessions.cancel_session(id="<id>")

    # Handle response
    print(res)
```

</br>

An Async SDK client can also be used to make asynchronous requests by importing it and asyncio.

```python
# Asynchronous Example
from albus_sdk import AsyncAlbus
import asyncio
import os

async def main():

    async with AsyncAlbus(
        api_key=os.getenv("ALBUS_API_KEY", ""),
    ) as albus:

        res = await albus.sessions.cancel_session(id="<id>")

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `id`                                                                   | *str*                                                                  | :heavy_check_mark:                                                     | Client-provided session identifier. Reuse it to continue the session.<br/> |

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

Returns an immutable record of session events in chronological order.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSessionAudit" method="get" path="/sessions/{id}/audit" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.sessions.get_session_audit(id="<id>", limit=100)

    # Handle response
    print(res)
```

</br>

An Async SDK client can also be used to make asynchronous requests by importing it and asyncio.

```python
# Asynchronous Example
from albus_sdk import AsyncAlbus
import asyncio
import os

async def main():

    async with AsyncAlbus(
        api_key=os.getenv("ALBUS_API_KEY", ""),
    ) as albus:

        res = await albus.sessions.get_session_audit(id="<id>", limit=100)

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                             | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | Client-provided session identifier. Reuse it to continue the session.<br/>                                                                                       |
| `after`                                                                                                                                                          | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Continue after this cursor. For list responses, pass the preceding page's `next_cursor`; for session messages, pass the preceding page's last message `cursor`.<br/> |
| `limit`                                                                                                                                                          | *Optional[int]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Maximum number of items to return.                                                                                                                               |

### Response

**[models.ListAuditEventsResponse](../../models/listauditeventsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
