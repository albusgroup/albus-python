# TraceSpanType

The kind of span (e.g. "invocation" for the invocation itself, "step" for one step, "model_call" for a model call, "tool_call" for a tool call it requested).


## Example Usage

```python
from albus_sdk.models import TraceSpanType

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TraceSpanType = "invocation"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"invocation"`
- `"step"`
- `"model_call"`
- `"tool_call"`
