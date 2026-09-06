# Auth

## Overview

Identify the authenticated user.

### Available Operations

* [whoami](#whoami) - Get the authenticated caller

## whoami

Returns the caller a credential authenticates: a signed-in user with every organization they belong to and their roles in each, or the API key that signed the request, along with the organization it acts in.


### Example Usage

<!-- UsageSnippet language="python" operationID="whoami" method="get" path="/whoami" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    x_albus_organization="<value>",
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.auth.whoami()

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

        res = await albus.auth.whoami()

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [operations.WhoamiRequest](../../operations/whoamirequest.md)       | :heavy_check_mark:                                                  | The request object to use for the request.                          |

### Response

**[models.WhoamiResponse](../../models/whoamiresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
