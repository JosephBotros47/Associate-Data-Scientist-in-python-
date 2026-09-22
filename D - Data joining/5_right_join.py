import numpy as np
import pandas as pd

### 1. Right Join

# Core Concept: Retains all rows from the right table and includes only matching rows from the left table. 
# It is the exact mirror opposite of a left join.

# Missing Values (NaN): If a row in the right table has no match in the left table, columns from the left 
# table are filled with NaN.

# Different Key Column Names: When key columns have different names across tables (e.g., id in movies vs. 
# movie_id in tv_genre), use left_on and right_on to specify them:

### syntax = tv_movies = movies.merge(tv_genre, left_on='id', right_on='movie_id', how='right')
