# Tools

The built-in tools the model may call. Include a tool's block to offer it (e.g. {"web_search": {}}); omit it to withhold it.



## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `web_search`                                                     | [Optional[models.WebSearchTool]](../models/websearchtool.md)     | :heavy_minus_sign:                                               | Offers the model web search.                                     |
| `terminal`                                                       | [Optional[models.TerminalTool]](../models/terminaltool.md)       | :heavy_minus_sign:                                               | Offers the model a persistent Linux sandbox to run commands in.<br/> |