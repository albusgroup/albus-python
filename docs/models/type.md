# Type

The kind of event (e.g. "agent_invocation" for the request that started the run, "model_call" for a model call and the tool calls it requested, "tool_call" for an executed tool call and its output). Events recorded earlier use "llm_call" and "tool_result" for those same two kinds.


## Example Usage

```python
from albus_sdk.models import Type

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Type = "agent_invocation"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"agent_invocation"`
- `"model_call"`
- `"tool_call"`
- `"harness_exit"`
- `"run_failed"`
- `"run_succeeded"`
- `"llm_call"`
- `"tool_result"`
