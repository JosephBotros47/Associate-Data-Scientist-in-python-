### Looping on dictionary 
# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for key, value in house:
    print(f"the {key} is {value} sqm")

#-For Dictionary---------------------

# house Dictionary 
house = {"hallway" :11.25, 
         "kitchen" :18.0, 
         "living room": 20.0, 
         "bedroom": 10.75, 
         "bathroom": 9.50}

# Build a for loop from scratch
for keys, values in house.items():
    print(f"the {key} is {value} sqm")

# -For numpy array-------------------
import numpy as np
np_height = np.array([1.73,1.68,1.71,1.89,1.79])
np_weight = np.array([65.4,59.2,63.6,88.4,68.7])
bmi = np_weight / np_height ** 2
for val in bmi:
    print(val)

# ------------------------------------
np_height = np.array([1.73,1.68,1.71,1.89,1.79])
np_weight = np.array([65.4,59.2,63.6,88.4,68.7])
meas = np.array([np_height, np_weight])

for val in meas:
    print(val) # each item in their array 

for val in np.nditer(meas):
    print(val) # each item as one array 
    # height
    # weight
    # and go on 

# ________________Exercises_____________
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items():
    print(f"the capital of {key} is {value}")

# ---------------
# Import numpy as np

# For loop over np_height
for val in np_height:
    print(f"{val} inches")

# For loop over np_baseball
for val in np.nditer(np_baseball):
    print(val)