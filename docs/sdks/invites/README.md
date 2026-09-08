# Invites

## Overview

### Available Operations

* [list_invites](#list_invites) - List pending invitations
* [create_invite](#create_invite) - Invite a user by email
* [revoke_invite](#revoke_invite) - Revoke a pending invitation

## list_invites

Returns unexpired invitations. Requires the admin role.


### Example Usage

<!-- UsageSnippet language="python" operationID="listInvites" method="get" path="/organization/invites" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.invites.list_invites()

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

        res = await albus.invites.list_invites()

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |

### Response

**[models.ListInvitesResponse](../../models/listinvitesresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrForbidden      | 403                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## create_invite

The invitation is accepted when the recipient signs in and expires after 14 days. Requires the admin role.


### Example Usage

<!-- UsageSnippet language="python" operationID="createInvite" method="post" path="/organization/invites" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.invites.create_invite(email="Cassie27@hotmail.com", role="member")

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

        res = await albus.invites.create_invite(email="Cassie27@hotmail.com", role="member")

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `email`                                                                             | *str*                                                                               | :heavy_check_mark:                                                                  | Email address of the person to invite.                                              |
| `role`                                                                              | [Optional[models.CreateInviteRequestRole]](../../models/createinviterequestrole.md) | :heavy_minus_sign:                                                                  | Role to grant the invitee.                                                          |

### Response

**[models.Invite](../../models/invite.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrForbidden      | 403                      | application/json         |
| errors.ErrConflict       | 409                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## revoke_invite

Requires the admin role.

### Example Usage

<!-- UsageSnippet language="python" operationID="revokeInvite" method="delete" path="/organization/invites/{id}" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    albus.invites.revoke_invite(id="<id>")

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

        await albus.invites.revoke_invite(id="<id>")

        # Use the SDK ...

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The invitation identifier.                                          |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrForbidden      | 403                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
