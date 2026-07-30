# program 1 
name1 = input("enter the first name : ")
name1 = name1.title()
name2 = input("enter the second name : ")
name = name1+' '+name2
print (name)

# program 2 
birthyear = int(input("Enter your birth year"))
year = 2026-birthyear
print(f"Your age is : {year}")

# program 3 
course = "Object Orianted Programming"
print(course[0])
print(course[-1])
print(course[7:15])

# program 4
print (f"My name is \"Joseph\" \n\tI love \\Python\\")

# program 5
dirty_text = "@@@python is powerful@@@"
print((dirty_text.strip('@')).upper())