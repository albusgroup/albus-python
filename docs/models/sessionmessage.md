# SessionMessage


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `cursor`                                                             | *int*                                                                | :heavy_check_mark:                                                   | Monotonic per-session position of this message.                      |
| `invocation_id`                                                      | *str*                                                                | :heavy_check_mark:                                                   | The invocation that produced this message.                           |
| `role`                                                               | [models.SessionMessageRole](../models/sessionmessagerole.md)         | :heavy_check_mark:                                                   | N/A                                                                  |
| `content`                                                            | *str*                                                                | :heavy_check_mark:                                                   | N/A                                                                  |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | N/A                                                                  |