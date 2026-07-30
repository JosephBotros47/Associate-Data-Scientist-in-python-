# Series = A pandas 1-dimensional labeled array that an hold any data type 
#          think of it like a single column in a spreadsheet (a-dimensional)

import pandas as pd

data1 = [100,102,104]
series1 = pd.Series(data1)
print(series1)

data2 = [100.2,102.5,104.9]
series2 = pd.Series(data2)
print(series2)

data3 = [100,102,"Joseph"]
series3 = pd.Series(data3)
print(series3)

data4 = ["joseph","Botros","Jo"]
series4 = pd.Series(data4)
print(series4)

# change the index   0  1  2
data4 = ["joseph","Botros","Jo"]
series4 = pd.Series(data4,index=["a","b","c"])
print(series4)

# print specific value using his location
print(series4.loc["a"]) # Joseph
print(series4.loc["b"]) # Botros

# change the values of series
series4.loc["a"] = 100
series4.loc["b"] = 200
series4.loc["c"] = 300

listOfKeys =["a","b","c"]
for item in listOfKeys:
    print(series4.loc[item])

# iloc
for item in range(0,3):
    print(series4.iloc[item])

# take from dictionary
dict = {
    "#1 :":100,
    "#2 :":200,
    "#3 :":300
}

dict1 = pd.Series(dict) # index = keys of dictionary
print(dict1.loc["#1 :"])
print(dict1.iloc[0])

dict1.iloc[0] +=50
print(dict1.iloc[0])