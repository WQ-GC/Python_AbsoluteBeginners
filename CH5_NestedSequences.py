#Nested Sequences
import random

myNestedList = [[1,2,3], [4,5,6], [111,222,333]]
print(myNestedList)
for eachList in myNestedList:
    print(eachList)
print("==========================================")

myNestedList2 = ["Hello", "World", "Today"]
print(myNestedList2)
for eachList in myNestedList2:
    print(eachList)

print("==========================================")

myNestedList3 = []
mySubList = [1,2,3]
myNestedList3.append(mySubList)
myNestedList3.append(mySubList)
myNestedList3.append(mySubList)
print(myNestedList3)
for eachList in myNestedList3:
    print(eachList)
    
print("==========================================")
database = list()

print("Create database: ")
for i in range(3):
    personItem = (
        random.randint(0,1000), #ID    
        str(random.randint(0,1000)),#PW
    )
    print(personItem)
    database.append(personItem)


print()
print("Reprint database: ")
for eachPerson in database:
    print(eachPerson)
    print("  ID: ", eachPerson[0])
    print("  PW: ", eachPerson[1])

print("--------------")
for i in range(0, len(database)):
    print("  ID: ", database[i][0])
    print("  PW: ", database[i][1])

print("==========================================")
#Unpacking (decode each element into nested sub elements)
for i in range(0, len(database)):
    print("size of element: ", len(database[i]))
    database_id, database_pw = (database[i][0], database[i][1])
    print("ID: ", database_id)
    print("PW: ", database_pw)


print("==========================================")
myList5 = list()
for i in range(3):
    myTuple = ("data1", "data2", "data3", "data4", "data5")
    myList5.append(myTuple)

print("length of each item in list: ", len(myList5[0]))

for i in range(len(myList5)):
    print()
    for j in range(len(myList5[0])):
        print(i, ": ", myList5[i][j])
    
   




