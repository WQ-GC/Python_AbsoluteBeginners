#shelve module
#to allow random access to list
import pickle, shelve

readFilename = "XAU_USD Historical Data.csv"
readPickleFilename = "Pickle_XAU_USD Historical Data.dat"

def ReadFileFunc():
    readFile = open(readFilename, "r")
    print("Reading: ", readFilename)
    getLines = readFile.readlines()
    readFile.close()

    writeBinaryFile = open(readPickleFilename, "wb")
    print("Writing pickle data to binary file: ", readPickleFilename)
    pickle.dump(getLines, writeBinaryFile)    
    writeBinaryFile.close()    
    
    readBinaryFile = open(readPickleFilename, "rb")
    print("Reading pickle data to binary file: ", readPickleFilename)
    getLines = pickle.load(readBinaryFile)
#    for eachLine in getLines:
#        print(eachLine)    
    readBinaryFile.close()    


def TestShelve():
    print("TestShelve")
    #shelve code Not Working
    ###s = shelve.open(readPickleFilename)





##############################
ReadFileFunc()
TestShelve()