# Health

## Overview

Check service availability.

### Available Operations

* [health](#health) - Health check endpoint

## health

Returns 200 OK if the service is healthy

### Example Usage

<!-- UsageSnippet language="python" operationID="health" method="get" path="/health" -->
```python
# Synchronous Example
from albus_sdk import Albus


with Albus() as albus:

    res = albus.health.health()

    # Handle response
    print(res)
```

</br>

An Async SDK client can also be used to make asynchronous requests by importing it and asyncio.

```python
# Asynchronous Example
from albus_sdk import AsyncAlbus
import asyncio

async def main():

    async with AsyncAlbus() as albus:

        res = await albus.health.health()

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.HealthResponse](../../models/healthresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HealthResponseError | 503                        | application/json           |
| errors.AlbusDefaultError   | 4XX, 5XX                   | \*/\*                      |