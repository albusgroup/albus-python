# Traces

## Overview

Find your agent invocations and read what they did.

### Available Operations

* [list_traces](#list_traces) - Search traces
* [get_trace](#get_trace) - Get one invocation's trace

## list_traces

Returns invocations newest first, without their spans. Running invocations are included.


### Example Usage

<!-- UsageSnippet language="python" operationID="listTraces" method="get" path="/traces" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.traces.list_traces(limit=10)

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

        res = await albus.traces.list_traces(limit=10)

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_name`                                                                                                                                                     | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Return only invocations of this agent (e.g. "support-triage").<br/>                                                                                              |
| `agent_revision`                                                                                                                                                 | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Return only invocations of this agent revision (e.g. "a1b2c3d4"). Combines with `agent_name`.<br/>                                                               |
| `status`                                                                                                                                                         | [Optional[models.TraceStatus]](../../models/tracestatus.md)                                                                                                      | :heavy_minus_sign:                                                                                                                                               | Return only invocations with this status.<br/>                                                                                                                   |
| `session_id`                                                                                                                                                     | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Return only invocations in this session. An unknown session returns `404`.<br/>                                                                                  |
| `since`                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Return only invocations that started at or after this time. Defaults to 31 days ago.<br/>                                                                        |
| `until`                                                                                                                                                          | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                             | :heavy_minus_sign:                                                                                                                                               | Return only invocations that started at or before this time. Defaults to now and must be after `since`.<br/>                                                     |
| `after`                                                                                                                                                          | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Continue after this cursor. For list responses, pass the preceding page's `next_cursor`; for session messages, pass the preceding page's last message `cursor`.<br/> |
| `limit`                                                                                                                                                          | *Optional[int]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Maximum number of traces to return.                                                                                                                              |

### Response

**[models.ListTracesResponse](../../models/listtracesresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## get_trace

Returns an invocation and its spans in chronological order. Spans may appear shortly after they occur and expire before the invocation does.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTrace" method="get" path="/traces/{invocation_key}" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.traces.get_trace(invocation_key="<value>", payloads=True, attempts="final")

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

        res = await albus.traces.get_trace(invocation_key="<value>", payloads=True, attempts="final")

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `invocation_key`                                                                                                                                                 | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | Invocation key sent or returned in the `Idempotency-Key` header.<br/>                                                                                            |
| `payloads`                                                                                                                                                       | *Optional[bool]*                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                               | Whether to include span inputs and outputs. Disabling payloads raises the maximum `limit` to 500. Use the same value on every page.<br/>                         |
| `attempts`                                                                                                                                                       | [Optional[operations.Attempts]](../../operations/attempts.md)                                                                                                    | :heavy_minus_sign:                                                                                                                                               | Attempts whose spans to return. `final` returns only the latest; `all` includes earlier spans marked `superseded`.<br/>                                          |
| `after`                                                                                                                                                          | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Continue after this cursor. For list responses, pass the preceding page's `next_cursor`; for session messages, pass the preceding page's last message `cursor`.<br/> |
| `limit`                                                                                                                                                          | *Optional[int]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Maximum spans to return. Defaults to 25 with payloads and 500 without; these are also the respective maximums.<br/>                                              |

### Response

**[operations.GetTraceResponse](../../operations/gettraceresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.ErrUnavailable    | 503                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
