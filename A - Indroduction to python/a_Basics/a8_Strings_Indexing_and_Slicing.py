#---- Strings Indexing & Slicing ----
# [1] All Data in python is Objects
# [2] Object contain Elements
# [3] Every element has its only Index
# [4] python use Zero Based Indexing (Index start from 0 zero)
# [5] Use Square brackets [INDEX] To access element
# [6] Enable Accessing parts of strings, Tuples ar lists
#             ----------------------------

#1 Indexing (Access single item)
my_string = "I love Python"
#            0123456789
#            0   1  2  3  4  5  6  7  8  9
print(my_string[0])#I
print(my_string[2])#l
print(my_string[7])#P
#           -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
print(my_string[-1])#n
print(my_string[-6])#P
print(my_string[-13])#I

# Indexing (Access Multiple item)
# [start:end]
print(my_string[:]) # from the start to end
print(my_string[2:6]) # index 2 to index 6
print(my_string[-13:-7]) # start from -13 to index -7
# [start:end:steps]
print(my_string[::2]) # from the start to end and the steps is two
print(my_string[2:6:2])
print(my_string[-13:-7:2])



