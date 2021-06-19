#Compute Tip amount based on Bill 15% and 20% 

getBill = float(input("Input bill amount: $"))

print("15% tip: ${0:.2f}" .format(getBill * 0.15))
print("20% tip: ${0:.2f}" .format(getBill * 0.20)) 
