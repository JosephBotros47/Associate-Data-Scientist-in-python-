#  DataFrame = A tabular data structure with rows and columns.(2 Dimensional)
#              Similar to an excel spreadsheet
data = {"Name": ["spongbob","patrick","squidward"]
        ,"Age":[30,35,40]}
import pandas as pd

df = pd.DataFrame(data)
print(df)
df = pd.DataFrame(data,index=["Employee 1","Employee 2","Employee 3"])
print(df)

# print row of index using loc
print(df.loc["Employee 1"])
print(df.loc["Employee 2"])
print(df.loc["Employee 2"])

# print row of index using iloc
print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[2])

## Add a new column 
df["Job"] = ["Software Engineer","Data Scientist Engineer","Ai Engineer"]
print(df)

## Add a new row 
new_row = pd.DataFrame([{"Name":"sandy","Age":28,"Job":"Generative AI Engineer"}],index =["Employee 4"])
# Concate it into df
df = pd.concat([df,new_row])
print(df)

## Add rows
new_row1 = pd.DataFrame([{"Name":"Joseph","Age":19,"Job":"Data Scientist"},{"Name":"Eugene","Age":60,"Job":"Manager"}],index =["Employee 5","Employee 6"])
# concate it into df
df = pd.concat([df,new_row1])
print(df)


# ----------------------------------------------
# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels
# or 
cars = pd.DataFrame(cars_dict, index = row_labels)

# Print cars again
print(cars)

# ----------------------------------------------
# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv',index_col = 0)

# Print out cars
print(cars)

# ----------------------------------------------
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out country column as Pandas Series
print(cars['country'])

# Print out country column as Pandas DataFrame
print(cars[['country']])

# Print out DataFrame with country and drives_right columns
print(cars[['country','drives_right']])

# ----------------------------------------------
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Print out drives_right column as Series
print(cars)
print(cars.loc[:,'drives_right'])
print(cars.iloc[:,2])

# Print out drives_right column as DataFrame
print(cars.loc[:,['drives_right']])
print(cars.iloc[:,[2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:,['cars_per_cap','drives_right']])
