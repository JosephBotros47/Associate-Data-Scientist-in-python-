# Directory of python scripts
# each script = module
# specify functions, methods, types
# Thousands of packages available in python
#       numpy
#       matplotlib
#       pandas
#       sckit-learn

# install packages using pip
# pip install numpy

# import packages using import statement
import numpy 

numpy.array([1,2,3]) # Output: array([1, 2, 3])

import numpy as np
np.array([1,2,3]) # Output: array([1, 2, 3])

from numpy import array
array([1,2,3]) # Output: array([1, 2, 3])

# Import the math package
import math

# ___________________________________________________

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))