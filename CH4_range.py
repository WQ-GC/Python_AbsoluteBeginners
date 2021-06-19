getRange = range(0,10)

#############################################
def PrintRange():
  print(getRange)
  print(type(getRange))

  for i in getRange:
    print(i)

#############################################
def PrintEachLetterOfWord():
  getWord = input("Input Word: ")

  #Print each char in word
  for eachChar in getWord:
    print(eachChar)

#############################################
def PrintEachDigitOfNumber():
  getVar = input("Get a number: ")

  #Convert to string for processing  
  for eachDigit in str(getVar):
    print(eachDigit)

#############################################
def CountFunction():
  startCount = 0
  endCount = 100
  gap = 5
  
  for i in range(startCount, endCount + 1, gap):
    print(i)


def CountReverse():
  startCount = 100
  endCount = 0
  gap = -10

  for i in range(startCount, endCount - 1, gap):
    print(i)

############################################################3###
############################################################3###
CountReverse()
    
