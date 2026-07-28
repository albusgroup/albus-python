# Token

API token metadata. Never includes the token value.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `id`                                                                       | *str*                                                                      | :heavy_check_mark:                                                         | Globally unique lookup identifier (the first segment of the token string). |
| `name`                                                                     | *str*                                                                      | :heavy_check_mark:                                                         | Human-readable display name for the token.                                 |
| `created_at`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_check_mark:                                                         | N/A                                                                        |
| `last_used_at`                                                             | [date](https://docs.python.org/3/library/datetime.html#date-objects)       | :heavy_minus_sign:                                                         | Timestamp of the last time this token was used for authentication.         |