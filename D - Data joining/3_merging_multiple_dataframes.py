import pandas as pd

# Syntax :
# # Three tables 
# grants_licences_ward = grants.merge(licences, on =['address','zip']) \
#                        .merge(wards, on ='ward' , suffixes =('_bus','_ward'))

# Four tables 
# the same 

# Data Camp Exercises 
# Merge licenses and zip_demo, on zip; and merge the wards on ward
#- licenses_zip_ward = licenses.merge(zip_demo , on ='zip') \
#-           			.merge(wards , on = 'ward')

# Print the results by alderman and show median income
#- print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))