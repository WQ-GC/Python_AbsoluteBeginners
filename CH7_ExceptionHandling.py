#Python Exceptions
import sys

def ExitProgram():
    print("sys.exit() - Exiting Program...")
    sys.exit()

def MyFunc(inputVar):
    return "Hello World"
    

def ExceptionInput():
    try:
        num = float("Hello World")

    except ValueError:
        print("cannot convert to float")
    

def ExceptionDivision():    
    num = 1000
    print("ExceptionDivision")

    for i in range(-3, 3, 1):
        print("divide by:", i, end="   ")

        try:
            num = 1000 / i
            print(num)

        except ZeroDivisionError:
            print("***Exception: Division by 0")
            continue


def TestExceptions():
    filename = "nosuchfile.txt"
    try:
        getFile = open(filename, "r")
    except IOError:
        print("Exception: IOError ", filename, " - Not found")

    ###########################################################
    print()
    myList = list()
    for i in range(10):
        myList.append(i)
        #print(i, ":", myList[i])

    try:
        myList[100] = 123

    except IndexError:
        print("Exception: IndexError - myList has no index at 100")

    ###########################################################
    print()
    myDict = {"abc": 123,
              "def": 456}
              
    try:
        getData = myDict["xyz"] 
    except KeyError:
        print("Exception: KeyError - myDict has no key ", '"xyz"')

    ###########################################################
    print()
    #myResult = myValue / 3
    try:
        myResult = myValue / 3
    except NameError:
        print("Exception: NameError - myValue does not exist")
    
    try:
        MyNoSuchFunction()
    except NameError:
        print("Exception: NameError - MyNoSuchFunction() does not exist")

    ###########################################################
    #print()
    #
    #try:
    #
    #except SyntaxError:
    #    print("Exception: Syntax error")
    
    
    ###########################################################
    print()
    
    #getFile = open(123, 123)
    try:
        getFile = open(123, 123)
    except TypeError:
        print("Exception: TypeError - open inputs type wrong")
    
    ###########################################################
    print()
    try:
        getData = MyFunc(123)
        print(int(getData))
    except ValueError:
        print("Exception: ValueError - MyFunc returns string, not integer")
        
    ###########################################################
    print()
    try:
        getData = 1000 / 0
    except ZeroDivisionError:
        print("Exception: ZeroDivisionError - Divide by zero")

def ExceptionCode():
    myVar = 1000 / 0                        #ZeroDivisionError
    getFile = open("NoSuchFile.txt", "r")   #FileNotFoundError
    getFile = open(123, "r")                #OSError
    getFile = int(MyFunc(123))              #ValueError
    getFile = MyFunc()                      #TypeError
       
    
def MultipleExceptions():
    myExceptionTuple = (ZeroDivisionError, OSError, FileNotFoundError, IOError, ValueError, TypeError)
    
    try:
        ExceptionCode()

    except myExceptionTuple:
        print("Check for exceptions... ")
        for eachItem in myExceptionTuple:
            print("  Exception: ", eachItem)

def ReceiveException():
    myExceptionTuple = (ZeroDivisionError, OSError, FileNotFoundError, IOError, ValueError, TypeError)
    try:
        print("Try...")
        ExceptionCode()
    except myExceptionTuple as e:
        print("...CAUGHT Exception as: ", end="")
        print(e)

    try:
        ExceptionCode()
    except myExceptionTuple:
        print("Within myExceptionTuple")
        ExitProgram() 
    


        
#############################################
ExceptionDivision()
print()
print("=====================================")
TestExceptions()
print()
print("=====================================")
MultipleExceptions()
print()
print("=====================================")
ReceiveException()
