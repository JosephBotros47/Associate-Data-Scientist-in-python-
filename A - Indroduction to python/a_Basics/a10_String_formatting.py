### String formatting
## the old way
name = "Joseph"
hoppy = "Sport"
print("My name is : %s and my hoppy is : %s" % (name, hoppy))
age = 19
print("My age is : %s "% age)# as a string not number
print("My age is : %d "% age)# as a number
degree = 2.47
print("My degree is : %d "% degree)
print("My degree is : %f "% degree)
print("My degree is : %.2f "% degree)
print("Hello world Iam %s and my age is %d and I got %.2f in my school "
      %(name,age,degree))

## the New way
name = "Joseph"
hoppy = "Sport"
print("My name is : {} and my hoppy is : {}" .format(name, hoppy))
age = 19
print("My age is : {} ".format(age))# as a string not number
print("My age is : {} ".format(age))# as a number
degree = 2.47
print("My degree is : {} ".format(degree))
print("My degree is : {} ".format(degree))
print("My degree is : {} ".format(degree))
print("Hello world Iam {} and my age is {:d} and I got {:f} in my school "
      .format(name,age,degree))
# {:d} for numbers
# {:s} or {} for string values
# {:f} for floating values to control its points {:.2f}
num = 4.12345
print("the number is {:.2f}".format(num))
print("the number is {:.3f}".format(num))
print("the number is {:.4f}".format(num))

# Money format
Mymoney = 9858690000
print("My money in bank is {:_d}".format(Mymoney))
print("My money in bank is {:,d}".format(Mymoney))

# rearrange items
a , b ,c = "one","two","three"
print("hello {} {} {}".format(a,b,c)) #hello one two three
print("hello {2} {1} {0}".format(a,b,c)) #hello three two one
print("Hello there I am {1:s} and my age is {0:d} I got {3:.2f} degree in my school " \
      "and I have {2:_d} dollar in my bank account".format(age,name,Mymoney,degree))

## Format in the newest way
print(f"Hello there I am {name:s} and my age is {age:d} I got {degree:.2f} degree in my school " \
      f"and I have {Mymoney:_d} dollar in my bank account")

print(f"Hello there I am {name} and my age is {age} I got {degree} degree in my school " \
      f"and I have {Mymoney} dollar in my bank account")
