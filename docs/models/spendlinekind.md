# SpendLineKind

What was used: a model billed to your credits, a model called with your own provider credential, or the compute an invocation ran on.


## Example Usage

```python
from albus_sdk.models import SpendLineKind

# Open enum: unrecognized values are captured as UnrecognizedStr
value: SpendLineKind = "model"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"model"`
- `"model_byok"`
- `"hardware"`
