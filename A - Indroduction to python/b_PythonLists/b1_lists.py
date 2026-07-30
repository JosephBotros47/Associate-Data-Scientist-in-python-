### ------- Lists -------
## [1] List Items are enclosed in square brackets
## [2] List are ordered, to use index to access item
## [3] List are Mutable => Add, Delete, Edit
## [4] List items is not unique
## [5] List can have different data types 

myList = ["Joseph","Botros",19,2.471114,True]
# index  [   0    ,    1   , 2,   3    , 4  ]
print(myList)
print(f"Iam {myList[:2]} and Iam {myList[2]:d}"\
      f"\nand I got {myList[3]:.2f} degree in university")

#=> mylist[1:3]
#output = 'Botros',19

## so [start:end]
# inclusive : exlusive

## Editing values
myList[0] = "Joseph Botros"
myList[1] =" "
myList[0:2] =["Joseph Botros Wilson"," "]
print(f"Iam {myList[0]} and Iam {myList[2]:d}"\
      f"\nand I got {myList[3]:.2f} degree in university")