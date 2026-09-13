# Billing

## Overview

Buy the prepaid credits agent sessions run on.

### Available Operations

* [create_checkout](#create_checkout) - Buy prepaid credits
* [get_credit_balance](#get_credit_balance) - Read your credit balance
* [list_credit_ledger](#list_credit_ledger) - List your credit history
* [get_spend](#get_spend) - Get your spend breakdown

## create_checkout

Creates a purchase and returns its payment URL. Credits are added when payment completes.


### Example Usage

<!-- UsageSnippet language="python" operationID="createCheckout" method="post" path="/billing/checkout" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.billing.create_checkout(amount_usd=421255, success_url="https://flimsy-apricot.com/", cancel_url="https://silent-formamide.name")

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

        res = await albus.billing.create_checkout(amount_usd=421255, success_url="https://flimsy-apricot.com/", cancel_url="https://silent-formamide.name")

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `amount_usd`                                                                            | *int*                                                                                   | :heavy_check_mark:                                                                      | Whole US dollars of credit to buy (e.g. 20).                                            |
| `success_url`                                                                           | *str*                                                                                   | :heavy_check_mark:                                                                      | Where the buyer's browser goes after paying. Must be https (or http on localhost).<br/> |
| `cancel_url`                                                                            | *str*                                                                                   | :heavy_check_mark:                                                                      | Where the buyer's browser goes if they back out. Must be https (or http on localhost).<br/> |

### Response

**[models.CreateCheckoutResponse](../../models/createcheckoutresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrUnavailable    | 503                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## get_credit_balance

Returns your organization's current prepaid credit balance in USD.


### Example Usage

<!-- UsageSnippet language="python" operationID="getCreditBalance" method="get" path="/billing/balance" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.billing.get_credit_balance()

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

        res = await albus.billing.get_credit_balance()

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |

### Response

**[models.CreditBalanceResponse](../../models/creditbalanceresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## list_credit_ledger

Returns purchases, grants, usage charges, and adjustments newest first, with the signed USD amount of each balance change.


### Example Usage

<!-- UsageSnippet language="python" operationID="listCreditLedger" method="get" path="/billing/ledger" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.billing.list_credit_ledger(limit=100)

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

        res = await albus.billing.list_credit_ledger(limit=100)

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

**[models.ListCreditLedgerResponse](../../models/listcreditledgerresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## get_spend

Returns what your usage cost, split by UTC day and by what was used: each model at each provider, and compute time. Each line carries the quantities it was charged for.


### Example Usage

<!-- UsageSnippet language="python" operationID="getSpend" method="get" path="/billing/spend" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.billing.get_spend()

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

        res = await albus.billing.get_spend()

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `since`                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                           | :heavy_minus_sign:                                                                                             | Include usage from the UTC day containing this time onward. Defaults to 31 days before `until`.<br/>           |
| `until`                                                                                                        | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                           | :heavy_minus_sign:                                                                                             | Include usage through the end of the UTC day containing this time. Defaults to now and must be after `since`.<br/> |

### Response

**[models.SpendResponse](../../models/spendresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
