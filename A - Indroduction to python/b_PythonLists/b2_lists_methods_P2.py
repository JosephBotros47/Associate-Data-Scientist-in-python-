### ------- List methods p2 -------- 
## clear() remove all element values in list 
a = [10,20,30,40]
a.clear()
print(a)

## copy() to copy the main to another list
Main = [10 ,20 ,30, 40 ,50]
c = Main.copy()

## implicit copy : that make if I copy list1 to list2 and 
#                  chane list2 so list1 change too
c = Main 

## explicit copy : That make if I copy list1 to list2 and
#                  change list2 so list1 does not effect 
c = Main[:]
# or
c = list(Main)
 
print(c)
print(Main)
c.append(60)
c[0] =0
print(Main)
print(c)

# count() count the time of appearance element in list
print(Main.count(10))

# index() to know the index of element in list
e = ["Joseph","Ramy","Isen","Hani"]
e.index("Joseph")

# insert()
f = [1,2,3,4,5,6,7]
f.insert(3,3)
print(f)
