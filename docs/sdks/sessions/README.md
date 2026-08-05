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
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.sessions.list_sessions()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

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
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.sessions.get_session(id="<id>", limit=100)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Client-provided session identifier. Use the same value across requests to continue the same agent session.                          |
| `after`                                                                                                                             | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Opaque pagination cursor. Return only items positioned after it; pass a value obtained from a previous page to fetch the next one.<br/> |
| `limit`                                                                                                                             | *Optional[int]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Maximum number of items to return.                                                                                                  |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

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

With `wait=true` the request long-polls: it blocks until the invocation's assistant response is available and returns it in `messages`. `wait_timeout` bounds the wait in seconds; when omitted the request waits indefinitely (until the response arrives or the client disconnects). If the timeout elapses first, the request fails with 504 and a JSON body, letting the client distinguish an expected server-side timeout from a transport error; the client may retry.


### Example Usage

<!-- UsageSnippet language="python" operationID="runSession" method="post" path="/sessions/{id}" -->
```python
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.sessions.run_session(id="<id>", user_prompt="<value>", model={
        "name": "<value>",
    }, wait=False)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                                                                                                  | Required                                                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                                                                                                                                                                                                                  | *str*                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                    | Client-provided session identifier. Use the same value across requests to continue the same agent session.                                                                                                                                                                                                                            |
| `user_prompt`                                                                                                                                                                                                                                                                                                                         | *str*                                                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                    | The user prompt driving this invocation.                                                                                                                                                                                                                                                                                              |
| `model`                                                                                                                                                                                                                                                                                                                               | [models.Model](../../models/model.md)                                                                                                                                                                                                                                                                                                 | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                    | N/A                                                                                                                                                                                                                                                                                                                                   |
| `idempotency_key`                                                                                                                                                                                                                                                                                                                     | *Optional[str]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                    | Optional but strongly encouraged. Uniquely identifies this invocation of the session; reuse the same value to safely retry a request, and a new value starts a new invocation. When omitted, the server generates a key for the invocation and returns it in the Idempotency-Key response header, but the request is not retry-safe.<br/> |
| `wait`                                                                                                                                                                                                                                                                                                                                | *Optional[bool]*                                                                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                    | When true, long-poll: block until the invocation's assistant response is available before returning.<br/>                                                                                                                                                                                                                             |
| `wait_timeout`                                                                                                                                                                                                                                                                                                                        | *Optional[int]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                    | Maximum time in seconds to block when wait=true. Omit to wait indefinitely. Ignored when wait is false.<br/>                                                                                                                                                                                                                          |
| `tools`                                                                                                                                                                                                                                                                                                                               | List[*str*]                                                                                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                    | Names of the tools the model may call (e.g. "WEB_SEARCH").                                                                                                                                                                                                                                                                            |
| `system_prompt`                                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                    | System instructions for the model. Uses a default if omitted.                                                                                                                                                                                                                                                                         |
| `max_steps`                                                                                                                                                                                                                                                                                                                           | *Optional[int]*                                                                                                                                                                                                                                                                                                                       | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                    | Max model steps before the run stops. Uses a default if omitted.                                                                                                                                                                                                                                                                      |
| `mcp_servers`                                                                                                                                                                                                                                                                                                                         | List[[models.MCPServer](../../models/mcpserver.md)]                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                    | MCP servers whose tools are offered to the model.                                                                                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                                      | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                    | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                                   |

### Response

**[models.RunSessionResponse](../../models/runsessionresponse.md)**

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
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    albus.sessions.delete_session(id="<id>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                       | *str*                                                                                                      | :heavy_check_mark:                                                                                         | Client-provided session identifier. Use the same value across requests to continue the same agent session. |
| `retries`                                                                                                  | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                           | :heavy_minus_sign:                                                                                         | Configuration to override the default retry behavior of the client.                                        |

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
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.sessions.get_session_audit(id="<id>", limit=100)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | Client-provided session identifier. Use the same value across requests to continue the same agent session.                          |
| `after`                                                                                                                             | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Opaque pagination cursor. Return only items positioned after it; pass a value obtained from a previous page to fetch the next one.<br/> |
| `limit`                                                                                                                             | *Optional[int]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Maximum number of items to return.                                                                                                  |
| `retries`                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                    | :heavy_minus_sign:                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                 |

### Response

**[models.ListAuditEventsResponse](../../models/listauditeventsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |