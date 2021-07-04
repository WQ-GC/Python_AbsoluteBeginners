#Read a textfile
print("Read whole text")
textFile = open("TextFile.txt", "r")
print(textFile.read())
textFile.close()

print("=============================")
print("Read entire file lines")
textFile = open("TextFile.txt", "r")
getLines = textFile.readlines()
for eachLine in getLines:
    print(eachLine, end="")
textFile.close()

print()
print("=============================")
print("Read first 10 lines")
textFile = open("TextFile.txt", "r")
#First line starts from 1
for i in range(10):
    print(i, ": ", textFile.readline(), end ="")
textFile.close()


print("=============================")
print("Read first 26 char")
textFile = open("TextFile.txt", "r")
print(textFile.read(26))
textFile.close()