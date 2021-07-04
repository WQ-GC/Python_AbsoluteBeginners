#Test Global Variables

myGlobalVar = 123

def myFunc_ModifyGlobal():
    """Modify a global variable"""
    #Access global variable
    global myGlobalVar
    myGlobalVar = 999
    print("  myGlobalVar: ", myGlobalVar)

def myFunc_FailModifyGlobal():
    #Access global variable
    myGlobalVar = 999
    print("  myGlobalVar: ", myGlobalVar)


myFunc_FailModifyGlobal()
print("***Fail to modify global variable")
print("myGlobalVar: ", myGlobalVar)

    
print("======================")
myFunc_ModifyGlobal()
print("myGlobalVar: ", myGlobalVar)


