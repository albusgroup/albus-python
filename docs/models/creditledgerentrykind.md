# CreditLedgerEntryKind

What moved the balance: a paid purchase, an operator grant, a usage charge, or a manual adjustment.


## Example Usage

```python
from albus_sdk.models import CreditLedgerEntryKind

# Open enum: unrecognized values are captured as UnrecognizedStr
value: CreditLedgerEntryKind = "purchase"
```


## Values

This is an open enum. Unrecognized values will not fail type checks.

- `"purchase"`
- `"grant"`
- `"usage_burn"`
- `"adjustment"`
