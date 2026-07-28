# State

Lifecycle state of the session.

## Example Usage

```python
from albus_sdk.models import State

# Open enum: unrecognized values are captured as UnrecognizedStr
value: State = "RUNNING"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"RUNNING"`
- `"DONE"`
- `"FAILED"`
- `"CANCELED"`
