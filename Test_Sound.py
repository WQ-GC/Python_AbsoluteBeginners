import os
import time
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 300  # Set Duration To 1000 ms == 1 second
#winsound.Beep(frequency, duration)


while 1:
    time.sleep(0.05)
    winsound.Beep(frequency, duration)
    

##for i in range(2000,20000,100):
##    print(i)
##    frequency = i
    
