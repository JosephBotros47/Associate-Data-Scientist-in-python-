import pandas as pd

# This lesson covers the concept of a Self Join in the pandas library, 
# which involves merging a table with itself as if you are working with 
# two identical copies of the data.

# syntax 
original_sequels = sequels.merge(sequels, left_on = 'sequel' , right_on = 'id'
                                 , suffixes = ("_org","_seq"))
print(original_sequels)