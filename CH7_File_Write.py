#File Write

filename = "fileWrite.txt"
fileWrite = open(filename, "w")

fileWrite.write("Test1\n")
fileWrite.write("Test2\n")
fileWrite.write("Test3\n")

print(filename, "written")
fileWrite.close()

print("====================")
print("Write line")
filename = "fileWrite2.txt"
fileWrite = open(filename, "w")

myLines = ["Line1 data\n",
           "Line2 data\n", 
           "Line3 data\n"] 

fileWrite.writelines(myLines)
print(filename, "written")
fileWrite.close()
