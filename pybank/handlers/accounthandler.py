#File for reading and handling of account CSVs

def createChecking(userPath):
    filepath = userPath + '/checking.csv'
    open(filepath,"w+")

def createSavings(userPath):
    filepath = userPath + '/savings.csv'
    open(filepath,"w+")

def addTransaction(path, transaction):
    with open(path, "a") as accountData:
        accountData.write(",test")
