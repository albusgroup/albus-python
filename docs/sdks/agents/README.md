# Agents

## Overview

Inspect the agents that have run in your organization.

### Available Operations

* [list_agents](#list_agents) - List agents
* [get_agent](#get_agent) - Get an agent
* [get_agent_revision](#get_agent_revision) - Get an agent revision

## list_agents

Returns agents that have run, with each agent's latest revision.


### Example Usage

<!-- UsageSnippet language="python" operationID="listAgents" method="get" path="/agents" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.agents.list_agents()

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

        res = await albus.agents.list_agents()

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |

### Response

**[models.ListAgentsResponse](../../models/listagentsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## get_agent

Returns the current revision and all revisions newest first.


### Example Usage

<!-- UsageSnippet language="python" operationID="getAgent" method="get" path="/agents/{name}" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.agents.get_agent(name="<value>")

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

        res = await albus.agents.get_agent(name="<value>")

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The agent's name.                                                   |

### Response

**[models.Agent](../../models/agent.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## get_agent_revision

Returns the revision's model, tools, instructions, and MCP servers.


### Example Usage

<!-- UsageSnippet language="python" operationID="getAgentRevision" method="get" path="/agents/{name}/revisions/{revision}" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.agents.get_agent_revision(name="<value>", revision="<value>")

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

        res = await albus.agents.get_agent_revision(name="<value>", revision="<value>")

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | The agent's name.                                                   |
| `revision`                                                          | *str*                                                               | :heavy_check_mark:                                                  | The agent revision to fetch.                                        |

### Response

**[models.AgentRevision](../../models/agentrevision.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
