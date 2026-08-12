# Tokens

## Overview

Manage organization API keys.

### Available Operations

* [list_tokens](#list_tokens) - List all API tokens. Never returns token values, only metadata.
* [create_token](#create_token) - Create an API token. The token value is returned only in this response.
* [get_token](#get_token) - Get token metadata by ID. Never returns the token value.
* [delete_token](#delete_token) - Revoke an API token by ID

## list_tokens

List all API tokens. Never returns token values, only metadata.

### Example Usage

<!-- UsageSnippet language="python" operationID="listTokens" method="get" path="/tokens" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.tokens.list_tokens()

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
        security=models.Security(
            bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
        ),
    ) as albus:

        res = await albus.tokens.list_tokens()

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |

### Response

**[models.ListTokensResponse](../../models/listtokensresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## create_token

Create an API token. The token value is returned only in this response.

### Example Usage

<!-- UsageSnippet language="python" operationID="createToken" method="post" path="/tokens" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.tokens.create_token(name="<value>")

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
        security=models.Security(
            bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
        ),
    ) as albus:

        res = await albus.tokens.create_token(name="<value>")

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |

### Response

**[models.CreateTokenResponse](../../models/createtokenresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## get_token

Get token metadata by ID. Never returns the token value.

### Example Usage

<!-- UsageSnippet language="python" operationID="getToken" method="get" path="/tokens/{id}" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.tokens.get_token(id="<id>")

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
        security=models.Security(
            bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
        ),
    ) as albus:

        res = await albus.tokens.get_token(id="<id>")

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The token's lookup ID (the identifier portion of the token string). |

### Response

**[models.Token](../../models/token.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## delete_token

Revoke an API token by ID

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteToken" method="delete" path="/tokens/{id}" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    albus.tokens.delete_token(id="<id>")

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
        security=models.Security(
            bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
        ),
    ) as albus:

        await albus.tokens.delete_token(id="<id>")

        # Use the SDK ...

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The token's lookup ID.                                              |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
