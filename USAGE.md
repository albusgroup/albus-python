<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asynchronous requests by importing asyncio.

```python
# Asynchronous Example
from albus_sdk import Albus, models
import asyncio
import os

async def main():

    async with Albus(
        security=models.Security(
            bearer_auth=os.getenv("ALBUS_BEARER_AUTH", ""),
        ),
    ) as albus:

        res = await albus.secrets.list_secrets_async()

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->