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

def run():
    print(mainMenu())

if __name__ == "__main__":
    run()