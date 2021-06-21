#List Operations
import random

myList = list()
print(type(myList), end=": ")
print(myList)

for i in range(10):
    myList.append(random.randint(0,9))
    print("myList.append(): ", myList)


print()
print("Number of 1s: ", str(myList.count(1)))


myList2 = myList.copy()
print()
print("myList1.copy() to myList2", end=": ")
print(myList2)
    
myList.clear()
print()
print("myList.clear(): ")
print("myList:  ", myList)
print("myList2: ", myList2)

myList = (1,2,3)
myList2.extend(myList)
print()
print("myList2.extend(): ", myList2)

print()
print("idx of first 1: " , str(myList2.index(1)))

print()
for i in range(len(myList2)):
    myList2.pop()
    print(myList2)



myList3 = [1,2,3,3,3,4]
print()
print(myList3)

myList3.remove(3)
print("Remove 3 from list: ", myList3)

del myList3[2]
print("remove at [2]: ", myList3)

myList3.insert(len(myList3), 5)
print("insert 5 to list: ", myList3)



myList4 = [1,2,3,4,5,6,7,8,9]
print()
print(myList4)

for i in range(len(myList4)):    
    getRandom = random.randint(0, len(myList4) - 1)
    delItem = myList4[getRandom]
    del myList4[getRandom]  #remove from 0th element
    print("removed ", delItem, " at: [", format(getRandom), "]   ", myList4)

print()
myList5 = list()
for i in range(0,5):
    myList5.append(random.randint(0,99))
print(myList5)
myList5.sort()
print("Sort myList5: ", myList5)

myList5.sort(reverse = True)
print("Reverse sort myList5: ", myList5)

#myList5.reverse()
#print("Reverse sort myList5: ", myList5)
