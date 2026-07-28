# Secrets

## Overview

Manage secrets available to agent sessions.

### Available Operations

* [list_secrets](#list_secrets) - List all secrets
* [create_secret](#create_secret) - Create a secret
* [get_secret](#get_secret) - Get a secret by name
* [update_secret](#update_secret) - Update a secret by name
* [delete_secret](#delete_secret) - Delete a secret by name

## list_secrets

List all secrets

### Example Usage

<!-- UsageSnippet language="python" operationID="listSecrets" method="get" path="/secrets" -->
```python
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.secrets.list_secrets()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListSecretsResponse](../../models/listsecretsresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## create_secret

Create a secret

### Example Usage

<!-- UsageSnippet language="python" operationID="createSecret" method="post" path="/secrets" -->
```python
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.secrets.create_secret(name="<value>", value="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `value`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The secret value.                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Secret](../../models/secret.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## get_secret

Get a secret by name

### Example Usage

<!-- UsageSnippet language="python" operationID="getSecret" method="get" path="/secrets/{name}" -->
```python
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.secrets.get_secret(name="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Secret](../../models/secret.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## update_secret

Update a secret by name

### Example Usage

<!-- UsageSnippet language="python" operationID="updateSecret" method="put" path="/secrets/{name}" -->
```python
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    res = albus.secrets.update_secret(name="<value>", value="<value>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `value`                                                             | *str*                                                               | :heavy_check_mark:                                                  | The new secret value.                                               |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.Secret](../../models/secret.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## delete_secret

Delete a secret by name

### Example Usage

<!-- UsageSnippet language="python" operationID="deleteSecret" method="delete" path="/secrets/{name}" -->
```python
from albus_sdk import Albus, models
import os


with Albus(
    security=models.Security(
        bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
    ),
) as albus:

    albus.secrets.delete_secret(name="<value>")

    # Use the SDK ...

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |