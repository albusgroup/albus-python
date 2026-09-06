# ErrForbidden


## Fields

| Field                                                 | Type                                                  | Required                                              | Description                                           | Example                                               |
| ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- |
| `message`                                             | *str*                                                 | :heavy_check_mark:                                    | Human-readable error message                          | this action requires the admin role                   |
| `code`                                                | *str*                                                 | :heavy_check_mark:                                    | Machine-readable reason (e.g. "forbidden_not_admin"). | forbidden_not_admin                                   |