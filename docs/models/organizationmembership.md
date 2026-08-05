# OrganizationMembership


## Fields

| Field                                     | Type                                      | Required                                  | Description                               | Example                                   |
| ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- | ----------------------------------------- |
| `id`                                      | *str*                                     | :heavy_check_mark:                        | Organization identifier                   | 42                                        |
| `name`                                    | *str*                                     | :heavy_check_mark:                        | Organization display name                 | Acme Corp                                 |
| `roles`                                   | List[*str*]                               | :heavy_check_mark:                        | Roles the user holds in this organization | [<br/>"admin"<br/>]                       |