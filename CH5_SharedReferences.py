#Shared References

myList = [1,2,3,4,5]
print(type(myList), " myList: ", myList)

myListRef1 = myList
myListRef2 = myListRef1
print(type(myListRef1), " myListRef1 is a reference to myList")
print(type(myListRef2), " myListRef2 is a reference to myList")

for item in myList:
    item = 111
    #print("item: ", item)
    #Item is not a reference

print("item is NOT a reference variable")
print()    

########################################################
#Change myList[i] changes references
for i in range(5):
    myList[i] = i * 111
#    print(i, ": ", myList[i])    
print("modify myList: ", myList)
print("myListRef1   : ", myListRef1)
print("myListRef2   : ", myListRef2)

print()
print("===========================================")
print("Changing through reference var: myListRef1")
for i in range(5):
    myListRef1[i] = i * 1
#    print(i, ": ", myListRef1[i])
print("myList           : ", myList)
print("modify myListRef1: ", myListRef1)
print("myListRef2       : ", myListRef2)
    
print()
print("===========================================")
print("Changing through reference var: myListRef2")
for i in range(5):
    myListRef2[i] = i * 3
#    print(i, ": ", myListRef2[i])
print("myList           : ", myList)
print("myListRef1       : ", myListRef1)
print("modify myListRef2: ", myListRef2)


print()
print("*******************************************")
print("Making a Copy of an object does NOT reference the original")
myCopyList = myList.copy()
for i in range(5):
    myCopyList[i] = 111

print("copy to myCopyList: ", myCopyList)
print("myList            : ", myList)













