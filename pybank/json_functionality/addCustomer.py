import json
import os

def createNewTestCustomer():
    data = { 'username': 'Scott', 'password': 'welcome123', 'flags': {'savings': 'true', 'checking': 'false'}}
    addNewCustomer(data)

#Create a working user directory for new customer
def createCustomerDirectory(newCustomerData):
    #Path of customer directory
    path = "../customer_data/" + newCustomerData["username"]

    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of directory %s failed" % newCustomerData["username"])
    else:
        print ("Creation of directory %s successful" % newCustomerData["username"])
        #If successful, add path to customer json
        newCustomerData['flags']['path'] = path

    return newCustomerData

#Add a new customer to json
def addNewCustomer(newCustomerData):

    createCustomerDirectory(newCustomerData)

    #Open file to extract json
    with open('../customer_data/overview.json') as customer_data:
        data = json.load(customer_data)

    data['customers'].append(newCustomerData)

    #Write back to json. Current functionality overwrites data in file with new "data"
    with open('../customer_data/overview.json', 'w') as customer_data:
        json.dump(data, customer_data)

createNewTestCustomer()
