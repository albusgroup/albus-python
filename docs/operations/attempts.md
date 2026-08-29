# Attempts

Which attempts to return spans for. `final`, the default, returns only the spans of the latest attempt — the one that produced the invocation's outcome, or the one still in flight; `all` also returns the spans of the attempts before it, each marked `superseded`. Either way `attempts` in the response lists every attempt that ran.


## Example Usage

```python
from albus_sdk.operations import Attempts
value: Attempts = "final"
```


## Values

- `"final"`
- `"all"`
