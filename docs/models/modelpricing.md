# ModelPricing

What the model currently costs, as decimal USD strings per one million tokens (e.g. "1.25"). Absent when the model is not yet priced.



## Fields

| Field                                          | Type                                           | Required                                       | Description                                    |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| `input_usd_per_mtok`                           | *str*                                          | :heavy_check_mark:                             | Price per million input tokens.                |
| `cached_input_usd_per_mtok`                    | *str*                                          | :heavy_check_mark:                             | Price per million cached input tokens.         |
| `output_usd_per_mtok`                          | *str*                                          | :heavy_check_mark:                             | Price per million output tokens.               |
| `thoughts_usd_per_mtok`                        | *str*                                          | :heavy_check_mark:                             | Price per million reasoning (thinking) tokens. |