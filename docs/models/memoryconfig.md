# MemoryConfig

Configures durable memory shared by invocations in the same group.



## Fields

| Field                                              | Type                                               | Required                                           | Description                                        |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `group`                                            | *str*                                              | :heavy_check_mark:                                 | Key identifying invocations that share memory.     |
| `generation`                                       | List[[models.Generation](../models/generation.md)] | :heavy_check_mark:                                 | Points when this agent may generate memories.      |