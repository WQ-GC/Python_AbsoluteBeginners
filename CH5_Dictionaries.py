#CH5 Dictionaries
#Dictionaries have a KEY => VALUE Pair
#Keys are UNIQUE!!!
#Values need NOT be unique
#Keys are IMMUTABLE
#Dictionaries are MUTABLE!
#Tuples        ("data1",1,"abc")
#List          [1,2,3,4]
#Dictionarties {"key" : "Value"}

myTuple = ("data1", 1, "abc")
print("myTuple: ", type(myTuple), " ", myTuple)

myList = [1,2,3]
print("myList: ", type(myList), " ", myList)

myDictionary = {
  "Key1" : "Value1",
  "Key2" : "Value2",
  "Key3" : "Value3",
  "Key4" : "Value4",
  "Key5" : "Value5",  
}
print("\n=======================================")
print("myDictionary: ", type(myDictionary))
print(type(myDictionary), ": myDictionary = ", myDictionary)
print("Keys  : ", myDictionary.keys())
print("Values: ", myDictionary.values())

for getKey in myDictionary: 
    print("Key: ", getKey, "    Value: ", myDictionary[getKey])


print("\n=======================================")
debugMsg = {
    "LEVEL_1" : "System Critical Low Power",
    "LEVEL_2" : "System Low Power",
    "LEVEL_3" : "System Normal Operation",
}
#print(debugMsg)
for eachMsgKey in debugMsg:
    print("Key - ", eachMsgKey, ":    =>       Value - ", debugMsg[eachMsgKey])

print("Dictionaries DO NOT SUPPORT Value => Key direction")

#WRONG: Attempting to use VALUE to access Dictionary
#print(myDictionary["System Critical Low Power"])    
#print(myDictionary["System Low Power"])    
#print(myDictionary["System Normal Operation"])    

print("\n=======================================")
searchKey = ["Hello World", "LEVEL_1", "MY DATA", "LEVEL_2", "LEVEL_3"]
for eachKey in searchKey:
    if eachKey in debugMsg:
        print(eachKey, " IS a Key in database")
    else :   
        print(eachKey, " is NOT a Key in database")


print("\n=======================================")
currPair = {
    "USDEUR": 0.84,
    "USDJPY": 111.02,
    "USDSGD": 1.3,
}

searchCurrPair = ["USDSGD", "BTCUSD", "USDEUR", "USDJPY", "XAUUSD"]
for eachItem in searchCurrPair:
    print(eachItem, ": ", currPair.get(eachItem, "No such Key in database"))

#Add New Item
currPair["XAUUSD"] = 1800
print("\nAdd XAUUSD")
for eachItem in searchCurrPair:
    print(eachItem, ": ", currPair.get(eachItem, "No such Key in database"))


#Add to existing Key
#print()
#getNewKey = input("Input new key: ")
#print(currPair.get(getNewKey, "Key not in database"))
#
#if currPair.get(getNewKey, "Not in database") != "Not in database":
#    print(getNewKey, currPair.get("USDSGD"))
#else:
#    print(getNewKey, ": Not in database")
#    getValue = input("Input value: ")
#    currPair[getNewKey] = getValue
#    print("New Key-Value added: ", getNewKey, ":", currPair[getNewKey]) 
#    
#for eachItem in currPair:
#    print(eachItem, ": ", currPair[eachItem])
    
#Modify existing Key
#print()
#for eachKey in currPair.keys():
#    print(eachKey)
#    getNewValue = input("Set new value: ")
#    currPair[eachKey] = getNewValue    
#    print(eachKey, ": ", currPair[eachKey], " - Value reassigned")
#
#print("Updated Dictionary")
#for eachItem in currPair:
#    print(eachItem, ": ", currPair[eachItem])
#

#Deleting existing Key
print()
print("Deleting all items")

allKeys = currPair.keys()
keyList = list()
for eachKey in allKeys:
    print(type(eachKey), ": ", eachKey)
    keyList.append(eachKey)
#print(keyList)

for i in range(len(currPair)):
    if currPair.get(keyList[i]) != None:
        del currPair[keyList[i]]
        print(keyList[i], ": key exists - deleting key")
        for eachItem in currPair:
            print(currPair.items())
        #    print("  ", eachItem, ": ", currPair[eachItem])
print(currPair, ": size", len(currPair))