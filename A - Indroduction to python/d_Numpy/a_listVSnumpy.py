## List 
# Powerful
# Collection of values
# Hold different types
# change , add, remove
# not for Data Sceince

height = [10,20,34,50,33]

weight = [10,20,34,50,33]

# error = weight / height ** 2

## Numpy array
# numeric python
# Alternative to python list: Numpy array
# Calculations over entire arrays
# easy and fast
# For Data Sceince
import numpy as np
np_height = np.array(height)
np_weight = np.array(weight)

# not error
bmi = np_weight / np_height ** 2
print(bmi)