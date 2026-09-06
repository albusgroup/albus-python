# Invites

## Overview

### Available Operations

* [list_invites](#list_invites) - List pending invitations
* [create_invite](#create_invite) - Invite a user by email
* [revoke_invite](#revoke_invite) - Revoke a pending invitation

## list_invites

Lists the unexpired invitations into your organization. Requires the admin role.


### Example Usage

<!-- UsageSnippet language="python" operationID="listInvites" method="get" path="/organization/invites" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    x_albus_organization="<value>",
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.invites.list_invites()

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

        res = await albus.invites.list_invites()

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                               | Type                                                                    | Required                                                                | Description                                                             |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `request`                                                               | [operations.ListInvitesRequest](../../operations/listinvitesrequest.md) | :heavy_check_mark:                                                      | The request object to use for the request.                              |

### Response

**[models.ListInvitesResponse](../../models/listinvitesresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrForbidden      | 403                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## create_invite

Invites an email address into your organization. The invitation is redeemed automatically the next time the invitee signs in with that email, and expires after 14 days. Requires the admin role.


### Example Usage

<!-- UsageSnippet language="python" operationID="createInvite" method="post" path="/organization/invites" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    x_albus_organization="<value>",
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.invites.create_invite(email="Cassie27@hotmail.com", role="member")

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
from albus_sdk import Albus, models
import os


with Albus(
    x_albus_organization="<value>",
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    albus.invites.revoke_invite(id="<id>")

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
        x_albus_organization="<value>",
        access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
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
