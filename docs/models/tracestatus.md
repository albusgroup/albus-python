# TraceStatus

How an invocation or one of its attempts ended, or `RUNNING` while it is still in flight. `CANCELED` means it was stopped on request before it answered.


## Example Usage

```python
from albus_sdk.models import TraceStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: TraceStatus = "RUNNING"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"RUNNING"`
- `"SUCCEEDED"`
- `"FAILED"`
- `"CANCELED"`
