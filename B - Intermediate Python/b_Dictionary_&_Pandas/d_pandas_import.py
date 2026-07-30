import pandas as pd

# Import cvc file 
df = pd.read_csv("data.csv")
print(df) # fead and tail data
print(df.to_string()) # all data

# Import json file 
df = pd.read_csv("data.json")
### Importing Files 
## CSV
df = pd.read_csv("data.csv")
print(df)
print(df.to_string())# to display all data

## Json
df = pd.read_json("data.json")
print(df)