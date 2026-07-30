# Functions : 
# type()
# piece of reusable code 
# call function instead of writing code yourself 

# max()  Find the maximum value in a list or among multiple arguments
fam = [1, 2, 3, 4, 5]
print(max(fam))  # Output: 5

# round()  Round a number to a specified number of decimal places
num = 3.14159
rounded_num = round(num)
print(rounded_num)  # Output: 3
num = 3.5234
rounded_num = round(num)
print(rounded_num)  # Output: 4

# round(integer , ndigits)  Round a number to a specified number of decimal places
num = 3.14159
rounded_num = round(num, 2)
print(rounded_num)  # Output: 3.14
num = 3.5234
rounded_num = round(num, 3)
print(rounded_num)  # Output: 3.523
num = 3.15159
rounded_num = round(num, 1)
print(rounded_num)  # Output: 3.2

# len()  Return the number of items in an object
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5

# int()  Convert a number or string to an integer
num_str = "42"
num_int = int(num_str)
print(num_int)  # Output: 42

## TO know how use a function, you can use the help() function to get information about it. For example, to get help on the max() function, you can do:
help(max)
?max

# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)
