# TraceSpanStatus

Whether the span succeeded. Only finished spans are returned.


## Example Usage

```python
from albus_sdk.models import TraceSpanStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TraceSpanStatus = "SUCCEEDED"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"SUCCEEDED"`
- `"FAILED"`
