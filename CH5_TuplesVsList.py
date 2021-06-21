#Tuples VS List

myTuple = (1,2,3,4,5)   
myList = [1,2,3,4,5]    #similar to arrays

############################################
#Tuples are IMMUTABLE
print("Tuples are IMMUTABLE")
print("Tuples are FASTER than list")
print("Tuples are good for holding CONSTANT values")

print(type(myTuple), end=": ")
print(myTuple)

#But Tuples allow new object instantiation
print("Tuple data are IMMUTABLE***")
#myTuple[0] = 99 #tuple does NOT Support mutability
#print(myTuple)

myTuple = (11,22,33,44,55)  
print(type(myTuple), end=": new Object - ")
print(myTuple)

myConstantTuple = (3.1415, 5)
print("CONSTANT: ", myConstantTuple[0])
print("CONSTANT: ", myConstantTuple[1])

print("==========================================")
###################################################
#List are MUTABLE
print("List data are MUTABLE")
print(type(myList), end=": ")
print(myList)

myList[0] = 99
print(type(myList), end=": ")
print(myList)

myList.append(999)
print(type(myList), end=": ")
print(myList)

