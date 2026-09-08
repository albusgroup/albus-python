# Organization

## Overview

View and manage the organization you are acting in.

### Available Operations

* [get_organization](#get_organization) - Get the current organization
* [update_organization](#update_organization) - Rename the current organization
* [list_organization_members](#list_organization_members) - List organization members
* [remove_organization_member](#remove_organization_member) - Remove an organization member
* [set_organization_member_role](#set_organization_member_role) - Set an organization member's role

## get_organization

Get the current organization

### Example Usage

<!-- UsageSnippet language="python" operationID="getOrganization" method="get" path="/organization" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.organization.get_organization()

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

        res = await albus.organization.get_organization()

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |

### Response

**[models.Organization](../../models/organization.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## update_organization

Requires the admin role.

### Example Usage

<!-- UsageSnippet language="python" operationID="updateOrganization" method="patch" path="/organization" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.organization.update_organization(name="Acme Corp")

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

        res = await albus.organization.update_organization(name="Acme Corp")

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `name`                                                              | *str*                                                               | :heavy_check_mark:                                                  | New organization display name.                                      | Acme Corp                                                           |

### Response

**[models.Organization](../../models/organization.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrForbidden      | 403                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## list_organization_members

List organization members

### Example Usage

<!-- UsageSnippet language="python" operationID="listOrganizationMembers" method="get" path="/organization/members" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.organization.list_organization_members()

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

        res = await albus.organization.list_organization_members()

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |

### Response

**[models.ListOrganizationMembersResponse](../../models/listorganizationmembersresponse.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrForbidden      | 403                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## remove_organization_member

Requires the admin role. The last admin cannot be removed.


### Example Usage

<!-- UsageSnippet language="python" operationID="removeOrganizationMember" method="delete" path="/organization/members/{user_id}" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    albus.organization.remove_organization_member(user_id="<id>")

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

        await albus.organization.remove_organization_member(user_id="<id>")

        # Use the SDK ...

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The member's user identifier.                                       |

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrForbidden      | 403                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.ErrConflict       | 409                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |

## set_organization_member_role

Requires the admin role. The last admin cannot be demoted.


### Example Usage

<!-- UsageSnippet language="python" operationID="setOrganizationMemberRole" method="put" path="/organization/members/{user_id}/role" -->
```python
# Synchronous Example
from albus_sdk import Albus
import os


with Albus(
    api_key=os.getenv("ALBUS_API_KEY", ""),
) as albus:

    res = albus.organization.set_organization_member_role(user_id="<id>", role="admin")

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

        res = await albus.organization.set_organization_member_role(user_id="<id>", role="admin")

        # Handle response
        print(res)

asyncio.run(main())
```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `user_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | The member's user identifier.                                       |
| `role`                                                              | [models.Role](../../models/role.md)                                 | :heavy_check_mark:                                                  | A member's role in an organization.                                 |

### Response

**[models.OrganizationMember](../../models/organizationmember.md)**

### Errors

| Error Type               | Status Code              | Content Type             |
| ------------------------ | ------------------------ | ------------------------ |
| errors.ErrBadRequest     | 400                      | application/json         |
| errors.ErrUnauthorized   | 401                      | application/json         |
| errors.ErrForbidden      | 403                      | application/json         |
| errors.ErrNotFound       | 404                      | application/json         |
| errors.ErrConflict       | 409                      | application/json         |
| errors.AlbusDefaultError | 4XX, 5XX                 | \*/\*                    |
