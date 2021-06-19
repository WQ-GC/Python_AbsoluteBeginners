#Message/String Analyser


#Checks for Lower Case Letters
def CountLowerLetters():
  print("=================================")
  getMessage = input("Input message: ")
  getAlphabets = "abcdefghijklmnopqrstuvwxyz"
  print("Message length: " + str(len(getMessage)))
  for getChar in getAlphabets:
    print("Number of " + getChar + ": " + str(getMessage.count(getChar)))


#Checks for Upper Case Letters
def CountUpperLetters():
  print("=================================")
  getMessage = input("Input message: ")
  getAlphabets = "abcdefghijklmnopqrstuvwxyz"
  print("Message length: " + str(len(getMessage)))
  for getChar in getAlphabets.upper():
    print("Number of " + getChar + ": " + str(getMessage.count(getChar)))


#Checks for Specific Word
def CheckWord():
  print("=================================")
  getMessage = input("Input message: ")
  print("Message length: " + str(len(getMessage)))

  #Words to Check
  matchWords = ["Hello", "World"]

  for eachWord in matchWords:
    print("Number of " + eachWord + ": " + str(getMessage.count(eachWord)))


def EachWord():
    getWord = input("Input word: ")
    for i in range(len(getWord)):
        #Array access
        #print("[" + str(i) + "]: " + getWord[i])
        print(getWord[i], end="")

    print("")
    #first 10 letters
    for i in range(10):
        print(getWord[i], end="")

    print("")
    #Last 10 letters    
    for i in range(len(getWord)-10, len(getWord)):
        print(getWord[i], end="")
        
        
def ReverseText():
    getMsg = "Hello World"
    j = -1
    for i in range(len(getMsg)):
        print(getMsg[j], end="")
        j -=1

def ImmutableStrings():
    #Strings are IMMUTABLE in Python
    getText = "Hello World"
    print(getText)

    #new string created (old string destroyed)
    getText = "New String Hello World"
    print(getText)

    #new string created (old string destroyed)
    getText += " World"
    print(getText)

    #Immutable (Runtime error)
    #Immutable (Runtime error)
    #Immutable (Runtime error)
    getText[0] = "W"

############################################################
############################################################
ImmutableStrings()
#ReverseText()
#CheckWord()
#EachWord()

