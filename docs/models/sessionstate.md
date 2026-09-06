# SessionState

Lifecycle state of the session: `RUNNING` while an invocation is in flight, otherwise how its latest invocation ended.


## Example Usage

```python
from albus_sdk.models import SessionState

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SessionState = "RUNNING"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"RUNNING"`
- `"DONE"`
- `"FAILED"`
- `"CANCELED"`
