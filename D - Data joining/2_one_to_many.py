import pandas as pd
import numpy as np

# 1. Relationship Types Comparison

# One-to-One: Every row in the left table corresponds to exactly one row in the 
# right table (e.g., each entry in wards has only one population record in census).

# One-to-Many: A single row in the left table corresponds to one or more rows in the 
# right table (e.g., one ward in wards contains many businesses in licenses).

# Pandas handles one-to-many merges automatically using the same code structure 
# as one-to-one joins: 
# wards.merge(licenses, on='ward')

# The original wards DataFrame contains only 50 rows, 
# but merging it with licenses expands the output to 10,000 rows.

# -------------------- Data camp exercises -------------------
# Merge the licenses and biz_owners table on account
#- licenses_owners = lenceses.merge(biz_owners , on ='account')

# Group the results by title then count the number of accounts
#_ counted_df = licenses_owners.groupby(licenses_owners).agg({'account':'count'})

# Sort the counted_df in descending order
#_ sorted_df = counted_df.sort_values(descending = True)

# Use .head() method to print the first few rows of sorted_df
#_ print(sorted_df.head())

# -------------------------------
# Merge the licenses and biz_owners table on account
#- licenses_owners = licenses.merge(biz_owners , on ='account')

# Group the results by title then count the number of accounts
#- counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in descending order
#_ sorted_df = counted_df.sort_values('account',ascending = False)

# Use .head() method to print the first few rows of sorted_df
#- print(sorted_df.head())