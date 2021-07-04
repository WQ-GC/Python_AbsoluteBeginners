#Read S&P500 data
#Pickle data
#Load data
import pickle, shelve

print("=============================")
print("Read GSPC US500.csv")
readFile = open("GSPC US500.csv", "r")
getLines = readFile.readlines() 
readFile.close()


print("=============================")
print("Pickle GSPC US500.csv")
writeBinaryFile = open("US500_Pickle.dat", "wb")
pickle.dump(getLines, writeBinaryFile)
writeBinaryFile.close()    

print("=============================")
print("Reload GSPC US500.csv")
readBinaryFile = open("US500_Pickle.dat", "rb")
getData = pickle.load(readBinaryFile)
print(type(getData))

count = 0;
for eachLine in getData:
    print(count, ": ", eachLine)
    count += 1
    
readBinaryFile.close()