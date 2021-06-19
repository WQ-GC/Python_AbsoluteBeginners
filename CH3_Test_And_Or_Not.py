#Test and, or, not for  Logical variables
import random
#############################################################
#Test and
print("and")
getStates = (False, True)
#print(str(getStates[0]), str(getStates[1]))
getBothStates = getStates[0] and getStates[0] 
print(str(getStates[0]) + " and " + str(getStates[0]) + "\t\t: " + str(getBothStates))

getBothStates = getStates[0] and getStates[1] 
print(str(getStates[0]) + " and " + str(getStates[1]) + "\t\t: " + str(getBothStates))

getBothStates = getStates[1] and getStates[0] 
print(str(getStates[1]) + " and " + str(getStates[0]) + "\t\t: " + str(getBothStates))

getBothStates = getStates[1] and getStates[1] 
print(str(getStates[1]) + " and " + str(getStates[1]) + "\t\t: " + str(getBothStates))
print("")


#############################################################
#Test Or
print("or")
getStates = (False, True)
#print(str(getStates[0]), str(getStates[1]))
getBothStates = getStates[0] or getStates[0] 
print(str(getStates[0]) + " or " + str(getStates[0]) + "\t\t: " + str(getBothStates))

getBothStates = getStates[0] or getStates[1] 
print(str(getStates[0]) + " or " + str(getStates[1]) + "\t\t: " + str(getBothStates))

getBothStates = getStates[1] or getStates[0] 
print(str(getStates[1]) + " or " + str(getStates[0]) + "\t\t: " + str(getBothStates))

getBothStates = getStates[1] or getStates[1] 
print(str(getStates[1]) + " or " + str(getStates[1]) + "\t\t: " + str(getBothStates))
print("")


#############################################################
#Test Not
print("not")

getStatus = False
i = 0
while i < 10:
  #toggle status
  getStatus = not getStatus
  print("status: " + str(getStatus) + "\t\tnot status: " + str(not getStatus))
  i += 1
