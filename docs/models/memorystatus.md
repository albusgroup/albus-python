# MemoryStatus

`active` while agents read this memory, `invalidated` once a later memory replaced it.


## Example Usage

```python
from albus_sdk.models import MemoryStatus

# Open enum: unrecognized values are captured as UnrecognizedStr
value: MemoryStatus = "active"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"active"`
- `"invalidated"`
