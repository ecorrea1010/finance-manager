import numpy as np
import pandas as pd
import os
import re
from datetime import datetime

def mainMenu():
    print("Welcome to Finance Manager!!!")
    print("1 - Enter a record")
    print("2 - View records")
    return getOptions("Select an option, please: ")

def getOptions(prompt):
    defaultValue = 0
    try:
        value = int(input(prompt))
        if value == 0:
            return defaultValue
        return value
    except ValueError:
        return defaultValue
    
def validateOption(option):
    if option == 1:
        setRecord()
    else:
        print("The selected option is incorrect")

def setRecord():
    fileData = openFile()
    if fileData["status"]:
        data = fileData["data"]
        print(getDataNewRecord())
    else:
        print("Data empty")

def getDataNewRecord():
    dateformat = '%Y-%m-%d'
    while True:
        date = input("Transaction date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, dateformat)
            date = datetime.strptime(date, dateformat)
            date = date.strftime(dateformat)
            break
        except ValueError:
            print("Invalid date. Please enter the date in the format YYYY-MM-DD.")
    while True:
        amount = input("Transaction amount: ")
        if re.match(r'^-?\d+(\.\d+)?$', amount):
            break
        else:
            print("Invalid amount. Please enter a valid number (integer or decimal)")
    while True:
        type = input("Transaction type (Entry - Egress): ")
        if type == "Entry" or type == "Egress":
            break
        else:
            print("Invalid transaction type. Please enter (Entry or Egress)")
    method = input("Transaction method: ")
    category = input("Transaction category: ")
    description = input("Transaction description: ")
    print("For bank transfers")
    origin = input("Bank of origin: ")
    destination = input("Destination bank: ")
    return {
        'date': date,
        'amount': float(amount),
        'type': type,
        'method': method,
        'category': category,
        'description': description,
        'origin': origin,
        'destination': destination
    }

def openFile():
    filePath = 'data/transactions.csv'
    data = {"status": False, "data": []}
    if os.path.exists(filePath):
        data = {"status": True, "data": pd.read_csv(filePath)}
    return data

def run():
    option = mainMenu()
    validateOption(option)

if __name__ == "__main__":
    run()