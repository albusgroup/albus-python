# ErrConflict


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `message`                                            | *str*                                                | :heavy_check_mark:                                   | Human-readable error message                         | Idempotency key reused with a different request body |
| `code`                                               | *Optional[str]*                                      | :heavy_minus_sign:                                   | Machine-readable reason (e.g. "last_admin").         | last_admin                                           |