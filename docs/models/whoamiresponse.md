# WhoamiResponse


## Fields

| Field                                   | Type                                    | Required                                | Description                             | Example                                 |
| --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| `user_id`                               | *str*                                   | :heavy_check_mark:                      | Unique user identifier                  | user_123                                |
| `email`                                 | *str*                                   | :heavy_check_mark:                      | User's email address                    | user@example.com                        |
| `name`                                  | *Optional[str]*                         | :heavy_minus_sign:                      | User's display name                     | John Doe                                |
| `roles`                                 | List[*str*]                             | :heavy_minus_sign:                      | User's roles                            | [<br/>"admin",<br/>"user"<br/>]         |
| `issued_at`                             | *Optional[int]*                         | :heavy_minus_sign:                      | Token issue timestamp (Unix epoch)      |                                         |
| `expires_at`                            | *Optional[int]*                         | :heavy_minus_sign:                      | Token expiration timestamp (Unix epoch) |                                         |