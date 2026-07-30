### ------- List methods p1 -------- 
## append() for adding new items
Myfriends = ["ahmed","Alaa","Youssef"]
print(Myfriends)
Myfriends.append("Seed")
print(Myfriends[3])
Myfriends.append(99)
print(Myfriends[4])
Myfriends.append(True)
Myfriends.append(9.87)
print(Myfriends[6])
# you can put or append another list as a one item in your list
MyNewfriends =["Youssef","Mostafa","Makary"]
Myfriends.append(MyNewfriends)
# appended to the end item in list 
print(f"My Newest Friends are {Myfriends[7]}")
print(f"My first newest friend is {Myfriends[7][0]}")
print(f"My second newest friend is {Myfriends[7][1]}")
print(f"My third newest friend is {Myfriends[7][2]}")

## extend() merge list inside list 
a = [2 , 3 , True]
b = ["First","Second"]
c = ["one","Two"]
a.extend(b)
print(a)
print(b)
a.extend(c)
print(a)

## remove() remove a specific element in list
x = [1,2,3,4,5,"Joseph","Web",True]
x.remove("Web")
print(x)

## del remove a specific element in list
del x[6]

## sort() arrange the same data type list
y = [1,2,100,120,-10,17,29]
y.sort() # by default arrange the list from minimum number to maximum one
print(y)
y.sort(reverse=True) #arrange the list from maximum number to minimum one
print(y)
s = ['N','B','C','D','A','F']
s.sort()
print(s)
s.sort(reverse=True)
print(s)

## reverse() just reverse 
s.reverse()
print(s)