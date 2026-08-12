# Invites

## Overview

### Available Operations

* [create_invite](#create_invite) - Invite a user by email

## create_invite

Creates a pending invitation for an email address. Omit organization_id to invite the user as the founder of a new organization that is created on their first sign-in; provide it to invite them into an existing organization. The invitation is redeemed automatically the first time the invitee signs in with that email.


### Example Usage

<!-- UsageSnippet language="python" operationID="createInvite" method="post" path="/invites" -->
```python
# Synchronous Example
from albus_sdk import Albus, models
import os


with Albus(
    access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
) as albus:

    res = albus.invites.create_invite(email="Cassie27@hotmail.com")

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
        access_token=os.getenv("ALBUS_BEARER_AUTH", ""),
    ) as albus:

        res = await albus.invites.create_invite(email="Cassie27@hotmail.com")

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `email`                                                                                                                          | *str*                                                                                                                            | :heavy_check_mark:                                                                                                               | Email address of the person to invite.                                                                                           |
| `role`                                                                                                                           | [Optional[models.CreateInviteRequestRole]](../../models/createinviterequestrole.md)                                              | :heavy_minus_sign:                                                                                                               | Role to grant the invitee. Defaults to admin when inviting to a new organization and member when inviting into an existing one.<br/> |
| `organization_id`                                                                                                                | *Optional[str]*                                                                                                                  | :heavy_minus_sign:                                                                                                               | Organization to invite the user into (e.g. "42"). Omit to create a new organization for the user on their first sign-in.<br/>    |

### Response

**[models.Invite](../../models/invite.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrConflict       | 409                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
