#----- string methods -----
#      --------------
#1 len(the_string) : to knowing the length of string
my_string = "###I love Python###"
print(len(my_string))#1

#2 strip() |  rstrip() | lstrip()
print(my_string.strip())
print(my_string.rstrip())
print(my_string.lstrip())
my_string = "###I love Python###"
print(my_string.strip("#")) # delete all # in string
print(my_string.rstrip("#"))# delete just the left # in string
print(my_string.lstrip("#"))# delete just the right # in string

#3 title() : make all first title of the word is capital
print(my_string.title())

#4 capitalize() make the first title of the string is capital
my_string = "I love Python###"
print(my_string.capitalize())

#5 upper()
print(my_string.upper())

#6 lower()
print(my_string.lower())