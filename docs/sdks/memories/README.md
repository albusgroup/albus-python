# Memories

## Overview

Read and delete what your agents remember.

### Available Operations

* [list_memory_groups](#list_memory_groups) - List memory groups
* [list_memories](#list_memories) - List a group's memories
* [delete_memory_group](#delete_memory_group) - Delete a group's memories
* [delete_memory](#delete_memory) - Delete one memory

## list_memory_groups

Returns memory groups ordered by key, with each group's active memory count.


### Example Usage

<!-- UsageSnippet language="python" operationID="listMemoryGroups" method="get" path="/memorygroups" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.memories.list_memory_groups(limit=100)

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

        res = await albus.memories.list_memory_groups(limit=100)

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after`                                                                                                                                                          | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Continue after this cursor. For list responses, pass the preceding page's `next_cursor`; for session messages, pass the preceding page's last message `cursor`.<br/> |
| `limit`                                                                                                                                                          | *Optional[int]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Maximum number of items to return.                                                                                                                               |

### Response

**[models.ListMemoryGroupsResponse](../../models/listmemorygroupsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## list_memories

Returns active memories newest first. Replaced memories are omitted.


### Example Usage

<!-- UsageSnippet language="python" operationID="listMemories" method="get" path="/memorygroups/{group}" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.memories.list_memories(group="<value>", limit=100)

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

        res = await albus.memories.list_memories(group="<value>", limit=100)

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                                                        | Type                                                                                                                                                             | Required                                                                                                                                                         | Description                                                                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `group`                                                                                                                                                          | *str*                                                                                                                                                            | :heavy_check_mark:                                                                                                                                               | Memory group to read or delete, matching the agent's `memory.group`.<br/>                                                                                        |
| `after`                                                                                                                                                          | *Optional[str]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Continue after this cursor. For list responses, pass the preceding page's `next_cursor`; for session messages, pass the preceding page's last message `cursor`.<br/> |
| `limit`                                                                                                                                                          | *Optional[int]*                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                               | Maximum number of items to return.                                                                                                                               |

### Response

**[models.ListMemoriesResponse](../../models/listmemoriesresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## delete_memory_group

Removes every memory in the group. Agents can add new memories later.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteMemoryGroup" method="delete" path="/memorygroups/{group}" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    albus.memories.delete_memory_group(group="<value>")

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

        await albus.memories.delete_memory_group(group="<value>")

        # Use the SDK ...

asyncio.run(main())
```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `group`                                                               | *str*                                                                 | :heavy_check_mark:                                                    | Memory group to read or delete, matching the agent's `memory.group`.<br/> |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## delete_memory

Permanently removes the memory from the group.


### Example Usage

<!-- UsageSnippet language="python" operationID="deleteMemory" method="delete" path="/memorygroups/{group}/memories/{id}" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    albus.memories.delete_memory(group="<value>", id="<id>")

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

        await albus.memories.delete_memory(group="<value>", id="<id>")

        # Use the SDK ...

asyncio.run(main())
```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `group`                                                               | *str*                                                                 | :heavy_check_mark:                                                    | Memory group to read or delete, matching the agent's `memory.group`.<br/> |
| `id`                                                                  | *str*                                                                 | :heavy_check_mark:                                                    | Identifier of the memory to delete.                                   |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
