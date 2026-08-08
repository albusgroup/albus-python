# Agent

An agent identified by name, with its current revision's full configuration and the list of all its revisions newest first.



## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `name`                                                           | *str*                                                            | :heavy_check_mark:                                               | The agent's name.                                                |
| `current`                                                        | [models.AgentRevision](../models/agentrevision.md)               | :heavy_check_mark:                                               | One revision of an agent, with its full configuration.           |
| `revisions`                                                      | List[[models.AgentRevisionMeta](../models/agentrevisionmeta.md)] | :heavy_check_mark:                                               | All revisions of the agent, newest first.                        |