import numpy as np
import pandas as pd

### definition of left join 
# A Left Join in pandas combines two tables by keeping all 
# rows from the left (first) table and pulling matching data 
# from the right (second) table based on a shared key column.

### Core Concept
# Left Table: Every single row is retained in the final output, 
# regardless of whether a match exists in the right table.

# Right Table: Data is brought in only when its key matches a key in the left table.

# Missing Values (NaN): If a row in the left table has no corresponding match in the right table,
# pandas fills the right table's columns with NaN (null values).

### Syntax :
#- movies_taglines = movies.merge(taglines, on='id', how='left')
