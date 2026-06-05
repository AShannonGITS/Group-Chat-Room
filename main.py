from mainfunctions import main_instructions, program_instructions, server_instructions, client_instructions, options_menu

from client import main_client
from server import main_server

from mainclass import chatroom


import time

def main():
    Valid = False
    
    while Valid == False:
        main_instructions()
        
        user_menu_input = input("Select an option from the menu: ").lower()
        
        if user_menu_input == "start" or user_menu_input == "s":
            print("Pick either 'server' or 'client':")
            
            main_program_input = input("").lower()
            
            if main_program_input == "server" or main_program_input == "s":
                server_instructions()
                main_server()
                
                Valid = True
            elif main_program_input == "client" or main_program_input == "c":
                client_instructions()
                main_client()
                
                Valid = True
            else:
                print("Invalid input, please try again. ")
                Valid = False
        elif user_menu_input == "options" or user_menu_input == "o":
            options_menu()
            
            options_menu_input = input("Type either 'ip' or 'port': ").lower()
            
            if options_menu_input == "ip" or options_menu_input == "i":
                print(f"\nCurrent IP: {chatroom.server_ip}")

                new_ip = input("New IP Address: ")
                chatroom.server_ip = new_ip

                print("IP updated.")
            elif options_menu_input == "port" or options_menu_input == "p":
                print(f"\nCurrent Port: {chatroom.server_port}")

                try:
                    new_port = int(input("New Port: "))

                    chatroom.server_port = new_port

                    print("Port updated.")
                except ValueError:
                    print("Invalid port number. Please try again. ")
            else:
                print("Invalid selection. Please try again. ")
            
        elif user_menu_input == "instructions" or user_menu_input == "i":
            program_instructions()
            time.sleep(0.5)
        elif user_menu_input == "exit" or user_menu_input == "e":
            exit()
        else:
            print("Invalid Input, please try again. ")
            
    
    

if __name__ == '__main__':
    main()