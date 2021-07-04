#Test Tuple
#Tuples can take different data types
#Tuples are IMMUTABLE!!!
#NOT POSSIBLE: Add or remove from tuples (they are fixed == CONSTANT)
#NOT POSSIBLE: Edit/update tuple index values
#POSSIBLE:  Reassign Tuples (REASSIGNMENT)
#POSSIBLE:  Concatenate BUT RETURNS A NEW TUPLE

#Tuples work like sequences
#Idx access
#len()
import random

#EconomicDataTuple = ()#Create an empty Tuple
EconomicDataTuple = tuple()#Create an empty Tuple
#print(type(EconomicDataTuple))
#print(EconomicDataTuple)

if not EconomicDataTuple:
    print("EconomicDataTuple empty")


################################################################
data1 = "GDP_Growth"
data2 = "Unemployment_Rate"
data3 = "Inflation_rate"

EconomicDataTuple = (
    data1,
    data2,
    data3,
)

print()
print(type(EconomicDataTuple))
print(EconomicDataTuple)

#Randomly choose tuple for 5 times
print("-----------------")
for i in range(5):
    x = random.choice(EconomicDataTuple)
    print("  random " + str(i) + " :", end="")
    print(x)



#for eachData in EconomicDataTuple:
#    print(eachData)

if "GDP_Growth" in EconomicDataTuple:
    print("GDP_Growth is in EconomicDataTuple")




print("=================================================")
#Recreate new tuple entry
EconomicDataTuple = (
    "New Tuple Data 1",  "New Tuple Data 2",  "New Tuple Data 3"
)
print(type(EconomicDataTuple))
print(EconomicDataTuple)
#for eachData in EconomicDataTuple:
#    print(eachData)


print("=================================================")
#Tuples can take different data types (heterogenous)    
RandomTuple = (
    123, "Hello World", 1.234, True,    
)

print("Random Tuple: (Heterogenous - Multiple types)")
print(RandomTuple)
print("Tuple length: " + str(len(RandomTuple)))

count = 0
for eachItem in RandomTuple:
    #Accessing tuple by index
    print("[", count, "]:   ", type(eachItem), end="   ")
    #print(eachItem)
    print(RandomTuple[count])
    count += 1

AnotherTuple = (
    "Another Data1", "Another Data2",
)

RandomTuple += AnotherTuple

print("=================================================")
print("New Random Tuple: ", end="")
print(RandomTuple)
for eachItem in RandomTuple:
    print(type(eachItem), end="   ")
    print(eachItem)


#Randomly choose tuple for 5 times
print("--------------------")
for i in range(5):
    x = random.choice(RandomTuple)
    print(x, end="  ")






