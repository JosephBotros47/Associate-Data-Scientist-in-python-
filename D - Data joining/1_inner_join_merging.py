import numpy as np
import pandas as pd

# joining = merging 
# Merging vs. Joining: Refers to the same process. 
# Pandas calls it merging, while databases 
# usually refer to it as joining.
# ------------------------------

# wards DataFrame: 50 rows and 4 columns containing local government office 
# information for Chicago's 50 wards.
# 
# census DataFrame: 50 rows and 6 columns 
# containing population data (2000–2010 changes) and ward center addresses.
# -----------------------------------

# inner merge 
# Inner Join Mechanics 
# Joining Key (on): Uses the common ward column 
# to match rows across both tables.

# Inner Join Logic: 
# Keeps only rows that have matching values in both DataFrames.

# Syntax: Called using 
# wards_merge = wards.merge(census, on ='ward')
# merge wards and census with ward column
# -----------------------------------

# Column Arrangement: Columns from the left DataFrame (wards) appear first, 
# followed by columns from the right DataFrame (census).
# ------------------------------------

# Handling Duplicate Columns (Suffixes)
# Problem: Both tables have overlapping column names (address and zip), 
# so pandas defaults to adding _x and _y.

# Solution: Pass custom suffixes via suffixes=('_ward', '_cen') to yield clean, 
# readable column names like address_ward and address_cen.

# --------------- Data Camp Exercises ------------------
# Merge the taxi_owners and taxi_veh tables
#- taxi_own_veh = taxi_owners.merge(taxi_veh ,on = 'vid')

# Print the column names of the taxi_own_veh
#- print(taxi_own_veh.columns)

#-----------------
# Merge the taxi_owners and taxi_veh tables setting a suffix
#- taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the column names of taxi_own_veh
#- print(taxi_own_veh.columns)

#-------------------
# Merge the taxi_owners and taxi_veh tables setting a suffix
#_ taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the value_counts to find the most popular fuel_type
#_ print(taxi_own_veh['fuel_type'].value_counts())

#---------------------
# Merge the wards and census tables on the ward column
#_ wards_census = wards.merge(census ,on = 'ward')

# Print the shape of wards_census
#_ print('wards_census table shape:', wards_census.shape)

#----------------------
# Print the first few rows of the wards_altered table to view the change 
#_ print(wards_altered[['ward']].head())

# Merge the wards_altered and census tables on the ward column
#_ wards_altered_census = wards_altered.merge(census, on ='ward')

# Print the shape of wards_altered_census
#_ print('wards_altered_census table shape:', wards_altered_census.shape)

#------------------------
# Print the first few rows of the census_altered table to view the change 
#_ print(census_altered[['ward']].head())

# Merge the wards and census_altered tables on the ward column
#_ wards_census_altered = wards.merge(census_altered,on = 'ward')

# Print the shape of wards_census_altered
#_ print('wards_census_altered table shape:', wards_census_altered.shape)