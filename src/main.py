import os
import helper
#import appointmentManager

def mainMenuFunctionality():
    helper.printMainMenu()
    op = helper.getUserInputForMainMenu()
    print(op)
    
def main():
    os.system("clear")
    helper.printHeader()
    helper.printFooter()
    mainMenuFunctionality()
    
main()    


