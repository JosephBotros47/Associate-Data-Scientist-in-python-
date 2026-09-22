import numpy as np 
import pandas as pd

### 2. Outer Join

# Core Concept: Returns all rows from both tables, regardless of whether a matching key exists between them.

# Missing Values (NaN): Any unmatched entries from either side will contain NaN in the merged output.

# Handling Overlapping Columns (suffixes): When both tables share identical non-key column names, pass a 
# tuple to suffixes to distinguish their origins:

# syntax = family_comedy = family.merge(comedy, on='movie_id', how='outer', suffixes=('_fam', '_com'))
