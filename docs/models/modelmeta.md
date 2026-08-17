# ModelMeta

A model Albus can run, and the provider serving it.


## Fields

| Field                                                                                  | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `name`                                                                                 | *str*                                                                                  | :heavy_check_mark:                                                                     | Model identifier to send as the agent's model name (e.g. "gemini-3.6-flash").<br/>     |
| `provider`                                                                             | *str*                                                                                  | :heavy_check_mark:                                                                     | Provider serving this model (e.g. "gemini", or "open_weight" for open-weight models).<br/> |