# Invite


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *str*                                                                | :heavy_check_mark:                                                   | Invitation identifier                                                |
| `email`                                                              | *str*                                                                | :heavy_check_mark:                                                   | Invited email address                                                |
| `role`                                                               | *str*                                                                | :heavy_check_mark:                                                   | Role the invitee will be granted                                     |
| `expires_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | When the invitation stops being redeemable                           |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | When the invitation was created                                      |