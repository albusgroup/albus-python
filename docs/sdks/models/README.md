# Models

## Overview

Discover the models available to run agents on.

### Available Operations

* [list_models](#list_models) - List models

## list_models

Returns available models and their providers.

### Example Usage

<!-- UsageSnippet language="python" operationID="listModels" method="get" path="/models" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.models.list_models()

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

        res = await albus.models.list_models()

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |

### Response

**[models.ListModelsResponse](../../models/listmodelsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
