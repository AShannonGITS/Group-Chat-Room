from mainfunctions import main_instructions, main_program, program_instructions, options_menu
from client import main_client
from server import main_server

import time

exit()

def main():
    Valid = True
    
    main_instructions()
    
    while Valid == True:
        UserMenuInput = input("Please pick an option from the menu: ").lower()
        
        if UserMenuInput == "start" or UserMenuInput == "s":
            Valid = False
            Chatting = True
            print()
            
            
            
        elif UserMenuInput == "instructions" or UserMenuInput == "i":
            print()
            program_instructions()
        elif UserMenuInput == "options" or UserMenuInput == "o":
            print()
            options_menu()
            
            OptionsMenuInput = input("")
            
            if OptionsMenuInput == "" or OptionsMenuInput == "":
                print("")
                Valid = False
        elif UserMenuInput == "exit" or UserMenuInput == "e":
            exit()
        else:
            print("Invalid input, please try again: ")
            Valid = True
            
    
    

if __name__ == '__main__':
    main()