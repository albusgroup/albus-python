# Billing

## Overview

Buy the prepaid credits agent sessions run on.

### Available Operations

* [create_checkout](#create_checkout) - Buy prepaid credits
* [get_credit_balance](#get_credit_balance) - Read your credit balance
* [list_credit_ledger](#list_credit_ledger) - List your credit history

## create_checkout

Starts a credit purchase for your organization. Returns the URL of a payment page to send the buyer's browser to; the credits are added to your balance once the payment completes there.


### Example Usage

<!-- UsageSnippet language="python" operationID="createCheckout" method="post" path="/billing/checkout" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    x_albus_organization="<value>",
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.billing.create_checkout(amount_usd=421255, success_url="https://flimsy-apricot.com/", cancel_url="https://silent-formamide.name")

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
from albus_sdk import Albus, models
import os


with Albus(
    x_albus_organization="<value>",
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.billing.get_credit_balance()

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

        res = await albus.billing.get_credit_balance()

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [operations.GetCreditBalanceRequest](../../operations/getcreditbalancerequest.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |

### Response

**[models.CreditBalanceResponse](../../models/creditbalanceresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## list_credit_ledger

Lists your organization's credit ledger, newest first: purchases, grants, usage charges, and adjustments, each with the signed USD amount it moved the balance by. Page with `after` and `limit`: pass the response's `next_cursor` as the next request's `after`, and keep requesting while `next_cursor` is present.


### Example Usage

<!-- UsageSnippet language="python" operationID="listCreditLedger" method="get" path="/billing/ledger" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    x_albus_organization="<value>",
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.billing.list_credit_ledger(limit=100)

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

        res = await albus.billing.list_credit_ledger(limit=100)

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                           | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `after`                                                                                                                             | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Opaque pagination cursor. Return only items positioned after it; pass a value obtained from a previous page to fetch the next one.<br/> |
| `limit`                                                                                                                             | *Optional[int]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Maximum number of items to return.                                                                                                  |

### Response

**[models.ListCreditLedgerResponse](../../models/listcreditledgerresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
