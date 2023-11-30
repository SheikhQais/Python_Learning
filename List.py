lis = [1,2,3,4,5,6,7,1,3,2]
num = len(lis)
print(num, lis[5],lis[6])
lis[6]= 0
print(lis)
print(type(lis))
new = list(("banana","apple","orange","water-melon","stawberry"))
print(new[-4:-1])
new.insert(2,"Avocado")
print(new)
new.append("Avocado")
print(new)
new.extend(("onion","cabbage","pear"))
print(new,len(new))
new.remove("Avocado")
print(new)
new.remove("Avocado")
print(new)

# for loop in List
for x in new:
    print(x)
for i in range (len(new)):
    print(i)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

indices = range(4)

print(indices[0])
print(indices[1])
print(indices[2])
print(indices[3])

# Joining Two Lists
# lis3= fruits + lis
# print(lis3)

#Using List Methods 
fruits.extend(lis)
print(fruits)

list5 = fruits.copy()
# list5.sort()
print(list5)