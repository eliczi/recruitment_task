# Pandas Virtual Columns

A utility function to dynamically add calculated columns to a pandas DataFrame using string expressions.

## Quick Start

```python
from solution import add_virtual_column

# Adds 'total' column by multiplying 'qty' and 'price'
result_df = add_virtual_column(df, "qty * price", "total")
