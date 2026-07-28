# RunSessionRequest


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `user_prompt`                                                    | *str*                                                            | :heavy_check_mark:                                               | The user prompt driving this invocation.                         |
| `model`                                                          | [models.Model](../models/model.md)                               | :heavy_check_mark:                                               | N/A                                                              |
| `tools`                                                          | List[*str*]                                                      | :heavy_minus_sign:                                               | Names of the tools the model may call (e.g. "WEB_SEARCH").       |
| `system_prompt`                                                  | *Optional[str]*                                                  | :heavy_minus_sign:                                               | System instructions for the model. Uses a default if omitted.    |
| `max_steps`                                                      | *Optional[int]*                                                  | :heavy_minus_sign:                                               | Max model steps before the run stops. Uses a default if omitted. |
| `mcp_servers`                                                    | List[[models.MCPServer](../models/mcpserver.md)]                 | :heavy_minus_sign:                                               | MCP servers whose tools are offered to the model.                |