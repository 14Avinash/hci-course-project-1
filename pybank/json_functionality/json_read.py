import json

#Read json into a variable
def parseJson():
    with open('customer_data/overview.json') as customer_data:
        data = json.load(customer_data)
    return data

#Find user dictionary based upon username. NOTE: Does not return username. Returns user dictionary
def findUser(username, data=None):
    if data is None:
        with open('customer_data/overview.json') as customer_data:
            data = json.load(customer_data)
    for user in data['customers']:
        if user['username'] == username:
            return user
    #Temporary error until UI functionality built
    print("Unable to find user")
    return None

#Find user's flags
# Data = full data set/dictionary.
# Requires username to find the correct user
def findUserFlags(username, data=None):
    if data is not None:
        #Find user's flags in dictionary
        if "username" not in data:
            data = findUser(username, data)
    else:
        #Find user's flags in JSON
        data = findUser(username)
    #If user is not found
    if data is None:
        return None
    #if user is found
    return data['flags']
# Data = Data pertaining to a specific user. This function can only be used when user data has already been separated out
def findFlags(data):
    return data['flags']

#Find path to user directory
# Data = full data set/dictionary.
# Requires username to find the correct user
def findUserDir(username, data=None):
    if data is not None:
        if "flags" not in data:
            data = findUserFlags(username, data)
    else:
        data = findUserFlags(username)
    #If user is not found
    if data is None:
        return None
    #if user is found
    return data.get("path", "")
# Data = Data pertaining to a specific user. This function can only be used when user data has already been separated out
def findDir(data):
    data = findFlags(data)
    return data.get("path", "")

#Find if user has a savings account
# Data = full data set/dictionary.
# Requires username to find the correct user
def findUserSavings(username, data=None):
    if data is not None:
        if "flags" not in data:
            data = findUserFlags(username, data)
    else:
        data = findUserFlags(username)
    #If user is not found
    if data is None:
        return None
    #if user is found
    return data.get("savings", "")
# Data = Data pertaining to a specific user. This function can only be used when user data has already been separated out
def findSavings(data):
    data = findFlags(data)
    return data.get("savings", "")

#Find if user has a checking account
def findUserChecking(username, data=None):
    if data is not None:
        if "flags" not in data:
            data = findUserFlags(username, data)
    else:
        data = findUserFlags(username)
    #If user is not found
    if data is None:
        return None
    #if user is found
    return data.get("checking", "")
# Data = Data pertaining to a specific user. This function can only be used when user data has already been separated out
def findChecking(data):
    data = findFlags(data)
    return data.get("checking", "")

#Find user password
# Data = full data set/dictionary.
# Requires username to find the correct user
def findUserPassword(username, data=None):
    if data is not None:
        #Find user in dictionary
        if "password" not in data:
            data = findUser(username, data)
    else:
        #Find user in JSON
        data = findUser(username)
    #If user is not found
    if data is None:
        return None
    #if user is found
    return data.get("password", "")
# Data = Data pertaining to a specific user. This function can only be used when user data has already been separated out
def findPassword(data):
    return data.get("password", "")

#Test function for gathering usernames
# def printAllCxUsernames():
#     with open('../customer_data/overview.json') as customer_data:
#         data = json.load(customer_data)
#         for c in data['customers']:
#             print('username: ' + c['username'])
