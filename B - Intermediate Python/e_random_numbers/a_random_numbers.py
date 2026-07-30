import numpy as np

rnum = np.random.rand()  # pseudo-random numbers
print(rnum)

# setting of random numbers 
np.random.seed(123) # start the random numbers from 123

coin = np.random.ranint(0,2) # randomly generate 0 or 1
coin = np.random.ranint(0,5) # randomly generate 0 , 1 , 2, 3 or 4


# -------- Exercises ---------
# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
num = np.random.rand()
print(num)

# ---------------------------
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
dice = np.random.randint(1,7)
print(dice)

# Use randint() again
again = np.random.randint(1,7)
print(again)
# ---------------------------
# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice< 6 :
    step += 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

# ---------------------------