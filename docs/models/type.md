# Type

The kind of event (e.g. "llm_call" for a model call and the tool calls it requested, "tool_result" for a tool's output).


## Example Usage

```python
from albus_sdk.models import Type

# Open enum: unrecognized values are captured as UnrecognizedStr
value: Type = "llm_call"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"llm_call"`
- `"tool_result"`
- `"harness_exit"`
- `"run_failed"`
- `"run_succeeded"`
