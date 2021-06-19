#Flip a coin 100 times
import random

trials = 10000

for i in range(trials):
    coinState = random.randint(0,1)
    if(coinState == 0):
        print(str(i) + ":\t Tails")
    else:
        print(str(i) + ": Heads")
