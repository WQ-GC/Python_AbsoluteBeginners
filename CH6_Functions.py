#Python Functions


def MyFunc_PrintInfo():
    """Display Info"""
    print("=====================")
    print("Test MyPythonFunction")
    

def MyFunc_GetInput(number):
    print("=====================")
    print("input is : ", number)


def MyFunc_ReturnOutput():
    print("=====================")
    print("output is: ", end="")
    return 999

def MyFunc_Return_3Values():
    a,b,c = 111,222,333
    return a,b,c


MyFunc_PrintInfo()
MyFunc_GetInput(111)
print(MyFunc_ReturnOutput())

#getData = MyFunc_Return_3Values()
#print(type(getData))
#print(getData)
#for eachItem in getData:
#    print(eachItem)
    
print("=======================")
print("Return 3 values and store into 3 variables")
getData1, getData2, getData3 = MyFunc_Return_3Values()
print(type(getData1), ": " , getData1)
print(type(getData2), ": " , getData2)
print(type(getData3), ": " , getData3)
