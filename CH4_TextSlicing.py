#Text Slicing
import random

getText = "Singapore GDP Data"
#0123456789
#Singapore GDP Data

#-1 -2 -3 -4
# a  t  a D


#for i in range(len(getText)):
#    print(getText[i], end="")
    
"""
print("")
j = -1    
for i in range(len(getText)):
    print(getText[j], end="")
    j-=1
"""
######################################################3    
getText = -1    
while(getText != 0):
    getText = input("\nGet Text: ")    
    if getText == "0":
        break
    
    lowIdx = random.randrange(-(len(getText)), len(getText))
    highIdx = random.randrange(-(len(getText)), len(getText))    
    if(lowIdx > highIdx):
        temp = lowIdx
        lowIdx = highIdx
        highIdx = temp
        
    print(str(lowIdx) + "   " + str(highIdx))    
    print("[", end="")
    #[startIdx:endIdx]
    print(getText[lowIdx: highIdx], end="")
    print("]", end="")
        
    