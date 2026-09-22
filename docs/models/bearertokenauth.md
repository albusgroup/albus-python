# BearerTokenAuth

A static bearer token sent with every request.


## Fields

| Field                                                                                     | Type                                                                                      | Required                                                                                  | Description                                                                               |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `type`                                                                                    | *Literal["bearer"]*                                                                       | :heavy_check_mark:                                                                        | N/A                                                                                       |
| `token`                                                                                   | *str*                                                                                     | :heavy_check_mark:                                                                        | The token, as a secret reference (e.g. "albus.sh/secrets/mcp-token"), never a raw value.<br/> |