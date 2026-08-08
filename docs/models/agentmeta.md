# AgentMeta

A row in the agent list — an agent's identity and activity.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `name`                                                               | *str*                                                                | :heavy_check_mark:                                                   | The agent's name.                                                    |
| `revision_count`                                                     | *int*                                                                | :heavy_check_mark:                                                   | Number of distinct revisions of this agent.                          |
| `created_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | When the agent first ran.                                            |
| `updated_at`                                                         | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | When the agent last ran.                                             |