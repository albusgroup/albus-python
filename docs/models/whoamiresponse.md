# WhoamiResponse

The caller a credential authenticates. Exactly one of user or api_key is present.



## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `user`                                                                   | [Optional[models.AuthenticatedUser]](../models/authenticateduser.md)     | :heavy_minus_sign:                                                       | The signed-in user, when calling with a user session.                    |
| `api_key`                                                                | [Optional[models.AuthenticatedAPIKey]](../models/authenticatedapikey.md) | :heavy_minus_sign:                                                       | The API key, when calling with an API key.                               |