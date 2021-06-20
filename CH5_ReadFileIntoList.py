#Read csv from file
import random

def OpenReadCsv():
    f = open("GSPC US500.csv", "r")
    print(f.fileno())

    for i in range(10):
        getLine = f.readline() 
        print(str(i) + ": " + getLine)
    
    
    g = open("GSPC US500.csv", "r")
    print(g.fileno())
    for i in range(10):
        getLine = g.readline() 
        print(str(i) + ": " + getLine)

#############################################################
def OpenReadCsv_1(getList):
    f = open("GSPC US500.csv", "r")
    print(type(getList))
    
    #first 5 entries    
    for i in range(5):
        getList.append(f.readline())

    print("initial size: {0}" .format(len(getList)))
    getList.pop(0) #remove from [0] index

    print("removed size: %i" % len(getList))            #method 1

    print("removed size: {0}" .format(len(getList)))    #method 2

    print("removed size:", format(len(getList)))        #method 3

    getStr = "removed size: " + str(len(getList))       #method 4
    print(getStr)

#############################################################
def AccessListItems_1(getList):
    #Access each element in the list
    count = 0
    print("===============================================================")
    print(type(getList))
    for eachLine in getList:
        print(str(count) + ": " + eachLine)
        count += 1

#############################################################
def AccessListItems_2(getList):
    #Access each idx in the list
    print("===============================================================")
    for i in range(len(getList)):
        print(str(i) + ": " + getList[i])

#############################################################
def CreateSubList(getList):
    startIdx = random.randint(0, len(getList) - 1)
    endIdx   = random.randint(0, len(getList) - 1)
    if(startIdx > endIdx):
        temp = startIdx
        startIdx = endIdx
        endIdx = temp
    print("sublist: [", startIdx, ":", endIdx, "]")

    subList = getList[startIdx: endIdx+1]
    #Access each idx in the list
    AccessListItems_2(subList)

#############################################################
SnP500List = list()
OpenReadCsv_1(SnP500List)
#AccessListItems_1(SnP500List)
AccessListItems_2(SnP500List)
CreateSubList(SnP500List)

