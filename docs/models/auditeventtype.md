# AuditEventType

The kind of event (e.g. "agent_invocation" for the request that started the invocation, "agent_step" for one turn, how it ended, and how long it took, "model_call" for a model call and the tool calls it requested, "tool_call" for an executed tool call and its output). Events recorded earlier use "llm_call", "tool_result", "run_failed" and "run_succeeded" for four of those kinds.


## Example Usage

```python
from albus_sdk.models import AuditEventType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: AuditEventType = "agent_invocation"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"agent_invocation"`
- `"agent_step"`
- `"model_call"`
- `"tool_call"`
- `"harness_exit"`
- `"invocation_failed"`
- `"invocation_succeeded"`
- `"llm_call"`
- `"tool_result"`
- `"run_failed"`
- `"run_succeeded"`
