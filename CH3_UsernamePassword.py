#Simple Password Application
#Test Strings Username & Password

username_pw_database = {
  "Guest1": "111",
  "Guest2": "222",
  "Guest3": "333",
  }
print(username_pw_database.keys())
print(username_pw_database.values())

getName = ""

#getName = input("Input name: ")
searchStatus = False
while(not searchStatus): 
  getName = input("Input name: ")
  
  if(getName in username_pw_database.keys()):
    searchStatus = True

  else:
    print("Username invalid - Retry...")
  


getPW = ""
searchStatus = False
#print(database[getName])
while(not searchStatus):
  getPW = str(input("Input Password: "))

  if(getPW == username_pw_database[getName]):
    searchStatus = True

  else:    
    print("Password invalid - Retry...")

    
print("Login: Success")
