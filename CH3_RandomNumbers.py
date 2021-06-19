#Random Numbers

import random

#Generate 10 numbers
print("[", end = "")
for i in range(10):
    #Random between 1 to 10
    print(random.randint(1,10), end=" ")
print("]")


print("[", end = "")
#Generate 10 numbers
for i in range(10):
    #Random number between 0 to 9
    print(random.randrange(10), end=" ")
print("]")


#######################################################
import matplotlib.pyplot as plt
import numpy as np
MAX_SIMULATIONS = 100000
MAX_BINS = 1000

print("================================")
getList_Uniform = list()
x_axis = range(1, (MAX_SIMULATIONS + 1),1)
for i in range(MAX_SIMULATIONS):
    #random UNIFORM distribution 0 to 1
    getList_Uniform.append(random.uniform(0,1))

getList_Uniform.sort()

#######################################################
print("================================")
getList_Normal = list()
x_axis = range(1, (MAX_SIMULATIONS + 1),1)
for i in range(MAX_SIMULATIONS):
    #random NORMAL distribution 0 to 1
    getList_Normal.append(random.gauss(0,1))
    #print(getVar)

getList_Normal.sort()

#plt.hist([getList_Uniform, getList_Normal], MAX_BINS)
plt.plot(getList_Uniform, MAX_SIMULATIONS)
#plt.hist(getList_Normal, bins = MAX_BINS)
plt.show()
