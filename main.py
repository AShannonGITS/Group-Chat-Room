from mainfunctions import main_instructions, program_instructions, options_menu
from client import main_client
from server import main_server

from mainclass import chat_room

import time

exit()

def main():
    Valid = True
    
    main_instructions()
    
    while Valid == True:
        UserMenuInput = input("Please pick an option from the menu: ").lower()
        
        if UserMenuInput == "start" or UserMenuInput == "s":
            user_input = input("Would you like to start the client or server? ")
            
            if user_input == "client" or user_input == "c":
                main_client()
            elif user_input == "server" or user_input == "s":
                main_server()
            else:
                print("Invalid input please try again. ")
            Valid = False
        elif UserMenuInput == "instructions" or UserMenuInput == "i":
            print()
            program_instructions()
        elif UserMenuInput == "options" or UserMenuInput == "o":
            print()
            options_menu()
            
            OptionsMenuInput = input("")
            
            if OptionsMenuInput == "username" or OptionsMenuInput == "u":
                print("")
            elif OptionsMenuInput == "server" or OptionsMenuInput == "server settings" or OptionsMenuInput == "s":
                
                chat_room.server_ip = input("Input the new IP Addres you would like the server to be hosted on (Local only): ")
                chat_room.server_port = (input("Input the new port number for the server: "))
                
            elif OptionsMenuInput == "client" or OptionsMenuInput == "client settings" or OptionsMenuInput == "c":
                client_input = input("")
                print("")
            else:
                print("Invalid input, please try again: ")
            Valid = False
        elif UserMenuInput == "exit" or UserMenuInput == "e":
            exit()
        else:
            print("Invalid input, please try again: ")
            Valid = True
            
    
    

if __name__ == '__main__':
    main()