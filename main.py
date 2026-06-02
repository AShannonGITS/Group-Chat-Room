from mainfunctions import main_instructions, program_instructions, options_menu
from client import main_client
from server import main_server

from mainclass import chat_room

import time

def main():
    Valid = True
    
    main_instructions()
    
    while Valid == True:
        main_instructions()
        
        user_menu_input = input("Select an option from the menu")
        
        if user_menu_input == "start" or user_menu_input == "s":
            print("start main program")
            
            main_program_input = input("")
            
            if main_program_input == "" or main_program_input == "":
                main_server()
            elif main_program_input == "" or main_program_input == "":
                main_client()
            else:
                print("Invalid input, please try again. ")
                
        elif user_menu_input == "options" or user_menu_input == "o":
            options_menu()
            print("options menu")
        elif user_menu_input == "instructions" or user_menu_input == "i":
            program_instructions()
        elif user_menu_input == "exit" or user_menu_input == "e":
            exit()
        else:
            print("Invalid Input, please try again. ")
            
    
    

if __name__ == '__main__':
    main()