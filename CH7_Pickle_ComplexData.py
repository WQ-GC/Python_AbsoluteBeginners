#Test Pickle module

import pickle, shelve

myList1 = [1,2,3,4,5]
myList2 = ["abc", "def", "hij"]
print(myList1)
print(myList2)

pickleFile = open("PickleDataFile.dat", "wb")
print("pickleFile created")

pickle.dump(myList1, pickleFile)
pickle.dump(myList2, pickleFile)

pickleFile.close()
print("pickleFile closed")

print("\n============================")
pickleFile = open("PickleDataFile.dat", "rb")
print("pickleFile open")

getList1 = pickle.load(pickleFile)
print(getList1)
getList2 = pickle.load(pickleFile)
print(getList2)

pickleFile.close()
