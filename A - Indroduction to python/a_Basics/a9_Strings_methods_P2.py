#1 split()  :By default divide the string to list of words
a = "Hello World I'm Joseph"
print(a.split()) # looking for spaces and divide word
b = "Hello-World-I'm-Botros"
print(b.split()) # looking for spaces and divide word
print(b.split('-'))# looking for dash '-' and divide word
print(b.split('-',2))# looking for dash '-' and divide word
# for 2 times and make the remaining in one element in the list

#2 center()
name = "Joseph"
print(name.center(10))#'  Joseph  '
print(name.center(10,'*'))#'**Joseph**'

#3 count() # count the number of existed character in a string
f = "I love python"
print(f.count("o"))
print(f.count('o',0,7))# with range

#4 swapcase() make capital small and small capital
g = "I love python"
h = "I love c++"
print(g.swapcase())
print(h.swapcase())

#5 startswith()  check if really the string starts with this character
print(name.startswith("J"))# True
print(name.startswith("o"))# False
print(name.startswith("s",2,5))# True

