#Default Function Values

def MyFunc(data1 = "123", data2 = "345"):
    print("data1: ", data1)
    print("data2: ", data2)
    
    

print("Default Values")    
MyFunc() 

print("========================")
print("Default Values - data2")    
MyFunc(data2 = 999)

print("========================")
print("Default Values - data1")    
MyFunc(data1 = "111")


print("========================")
print("Default Values (Keyword Arguments)")    
MyFunc(data1 = "111", data2 = "222")

print("========================")
print("Default Values (reverse Keyword Arguments)")    
MyFunc(data2 = "222", data1 = "111")

print("========================")
MyFunc("aaa","bbb")
