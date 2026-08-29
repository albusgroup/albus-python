# Traces

## Overview

Find your agent invocations and read what they did.

### Available Operations

* [list_traces](#list_traces) - Search traces
* [get_trace](#get_trace) - Get one invocation's trace

## list_traces

Lists your organization's agent invocations, newest first, without their spans. Filter by agent name, agent revision, status, session, or start time to find the invocation you want, then read it with `GET /traces/{invocation_key}`. An invocation is listed as soon as it starts, and a filter that matches nothing returns an empty page rather than an error — except `session_id`, which is a `404` when your organization has no such session.

Page with `after` and `limit`: pass the response's `next_cursor` as the next request's `after`, and keep requesting while `next_cursor` is present — you have reached the end when it is absent. A page can hold fewer invocations than `limit`, or none at all, and still have a `next_cursor`; a short page is not the end of the results.

A listing covers the window given by `since` and `until`, and omitting `since` searches the last 31 days. The window is fixed when the first page is requested, so paging with `after` keeps returning results from the window that page used: `after` carries that window and the filters it was made with, so send it with no filters, or with every filter repeated exactly, and expect a `400` otherwise.


### Example Usage

<!-- UsageSnippet language="python" operationID="listTraces" method="get" path="/traces" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.traces.list_traces(limit=10)

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

        res = await albus.traces.list_traces(limit=10)

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                                                   | Type                                                                                                                                                        | Required                                                                                                                                                    | Description                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `agent_name`                                                                                                                                                | *Optional[str]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                          | Return only invocations of this agent (e.g. "support-triage"). Invocations with no recorded agent name are not matched.<br/>                                |
| `agent_revision`                                                                                                                                            | *Optional[str]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                          | Return only invocations of this exact agent revision (e.g. "a1b2c3d4"). Combines with `agent_name`. Invocations with no recorded revision are not matched.<br/> |
| `status`                                                                                                                                                    | [Optional[models.TraceStatus]](../../models/tracestatus.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                          | Return only invocations with this outcome. An invocation whose spans have aged out is still matched by the outcome it recorded.<br/>                        |
| `session_id`                                                                                                                                                | *Optional[str]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                          | Return only invocations of this session — the session identifier you ran it with. A session you do not have is a `404`.<br/>                                |
| `since`                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                        | :heavy_minus_sign:                                                                                                                                          | Return only invocations that started at or after this time. Defaults to 31 days ago; pass it to search further back.<br/>                                   |
| `until`                                                                                                                                                     | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                        | :heavy_minus_sign:                                                                                                                                          | Return only invocations that started at or before this time. Defaults to now, and must be after `since`; an earlier `until` is a `400`.<br/>                |
| `after`                                                                                                                                                     | *Optional[str]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                          | Opaque pagination cursor. Return only items positioned after it; pass a value obtained from a previous page to fetch the next one.<br/>                     |
| `limit`                                                                                                                                                     | *Optional[int]*                                                                                                                                             | :heavy_minus_sign:                                                                                                                                          | Maximum number of traces to return. A page can be shorter, so page while `next_cursor` is present.<br/>                                                     |

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

Returns one agent invocation and a page of its spans in chronological order — the model calls it made and the tool calls they requested, with their payloads.

Page with `after` and `limit`: pass the response's `next_cursor` as the next request's `after`, and keep requesting while `next_cursor` is present — you have reached the end when it is absent. A page can hold fewer spans than `limit`, or none at all, and still have a `next_cursor`; a short page is not the end of the spans.

An invocation that was retried has more than one attempt, and by default only the spans of the latest attempt come back — the one that produced its outcome, or the one still in flight: the attempts before it are hidden, so a retried invocation reads as one history. They are hidden, not absent — every attempt ran, spent tokens, and may have made tool calls whose effects stand — so `attempts` lists all of them with their own outcomes and token usage, and `attempts=all` returns their spans too, each marked `superseded`.

A span becomes readable seconds after it happens, so an invocation still in flight can return fewer spans than it has already taken. A payload can come back shortened, or left out when it is too large — `input` and `output` say when, and `*_bytes`, `*_sha256` and `*_truncated` describe the complete value where the span carries them. Reading the shape of an invocation without its payloads is a request with `payloads=false`: the same spans with their timings, statuses and token usage, and `limit` up to 500, so a whole trace usually fits in one request. Spans age out after a retention window: past it `spans_expired` is true and no spans come back, while the invocation itself stays readable.


### Example Usage

<!-- UsageSnippet language="python" operationID="getTrace" method="get" path="/traces/{invocation_key}" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.traces.get_trace(invocation_key="<value>", payloads=True, attempts="final")

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

        res = await albus.traces.get_trace(invocation_key="<value>", payloads=True, attempts="final")

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Required                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `invocation_key`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | *str*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The invocation's key — the value sent as its Idempotency-Key, or the one the server returned in that header when it was omitted.<br/>                                                                                                                                                                                                                                                                                                                                                                                                           |
| `payloads`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | *Optional[bool]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Whether to include what each span was given and produced. `true`, the default, returns `input` and `output` and the fields that describe them. `false` returns the same spans without them — everything the span recorded about itself: `id`, `parent_id`, `type`, `name`, `status`, `started_at`, `ended_at` and `usage` — which is the cheap way to read an invocation's shape, and it lets `limit` go up to 500. `after` carries the mode it was made with, so page with the same `payloads` you started with and expect a `400` otherwise.<br/> |
| `attempts`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Optional[operations.Attempts]](../../operations/attempts.md)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Which attempts to return spans for. `final`, the default, returns only the spans of the latest attempt — the one that produced the invocation's outcome, or the one still in flight; `all` also returns the spans of the attempts before it, each marked `superseded`. Either way `attempts` in the response lists every attempt that ran.<br/>                                                                                                                                                                                                 |
| `after`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Opaque pagination cursor. Return only items positioned after it; pass a value obtained from a previous page to fetch the next one.<br/>                                                                                                                                                                                                                                                                                                                                                                                                         |
| `limit`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Maximum number of spans to return. With payloads at most 25, which is also the default; with `payloads=false` at most 500, and 500 by default, so one request usually returns a whole trace. A `limit` above the bound for the mode you asked for is a `400`. A page can be shorter, so page while `next_cursor` is present.<br/>                                                                                                                                                                                                               |

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
