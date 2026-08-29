# Memories

## Overview

Read and delete what your agents remember.

### Available Operations

* [list_memories](#list_memories) - List a group's memories
* [delete_memory_group](#delete_memory_group) - Delete a group's memories
* [delete_memory](#delete_memory) - Delete one memory

## list_memories

Lists the memories of one memory group, newest first: both the memories agents currently read and those a later memory has replaced. A group nothing has been remembered in yet is an empty list, not an error.

Page with `after` and `limit`: pass the response's `next_cursor` as the next request's `after`, and keep requesting while `next_cursor` is present — you have reached the end when it is absent.


### Example Usage

<!-- UsageSnippet language="python" operationID="listMemories" method="get" path="/memories" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.memories.list_memories(group="<value>", limit=100)

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

        res = await albus.memories.list_memories(group="<value>", limit=100)

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `group`                                                                                                                             | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | The memory group to read or delete — the `memory.group` value the agents sharing those memories run with.<br/>                      |
| `after`                                                                                                                             | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Opaque pagination cursor. Return only items positioned after it; pass a value obtained from a previous page to fetch the next one.<br/> |
| `limit`                                                                                                                             | *Optional[int]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Maximum number of items to return.                                                                                                  |

### Response

**[models.ListMemoriesResponse](../../models/listmemoriesresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## delete_memory_group

Deletes every memory of one memory group. Agents bound to the group remember nothing from before the call and can remember again after it. A group that holds no memories is deleted just the same, so the call is safe to repeat.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteMemoryGroup" method="delete" path="/memories" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    albus.memories.delete_memory_group(group="<value>")

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

        await albus.memories.delete_memory_group(group="<value>")

        # Use the SDK ...

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `group`                                                                                                    | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The memory group to read or delete — the `memory.group` value the agents sharing those memories run with.<br/> |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## delete_memory

Deletes one memory of a memory group. Agents bound to the group stop reading it, and the deletion is permanent. A memory the group does not hold is a `404`.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteMemory" method="delete" path="/memories/{id}" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    albus.memories.delete_memory(id="<id>", group="<value>")

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

        await albus.memories.delete_memory(id="<id>", group="<value>")

        # Use the SDK ...

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                       | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The memory's identifier, as returned by `GET /memories`.                                                   |
| `group`                                                                                                    | *str*                                                                                                      | :heavy_check_mark:                                                                                         | The memory group to read or delete — the `memory.group` value the agents sharing those memories run with.<br/> |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
