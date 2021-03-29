def printHeader():
    print("\n**************************")
    print("****Appointment System****")
    print("**************************")

def printFooter():
    print("\n***************************")
    print("~~~~ Created by Navdeep ~~~")
    print("***************************")

def printMainMenu():
    print("\n~~~ Main Menu ~~~")
    print("1: Show all appointments")
    print("2: Add an appointment")
    print("3: Remove an appointment")
    print("4: Change an appointment")
    print("5: Exit")

def getUserInputForMainMenu():
    op = input("\nPlease enter your choice: ")
    if(op == "1" or op == "2" or op == "3" or op == "4" or op == "5"):
        return op
    print ("Your option is not valid. Please try again.")
    return getUserInputForMainMenu()

