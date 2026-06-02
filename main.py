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
        
        user_menu_input = input("Select an option from the menu").lower()
        
        if user_menu_input == "start" or user_menu_input == "s":
            print("start main program")
            
            main_program_input = input("").lower()
            
            if main_program_input == "server" or main_program_input == "s":
                main_server()
            elif main_program_input == "client" or main_program_input == "c":
                main_client()
            else:
                print("Invalid input, please try again. ")
        elif user_menu_input == "options" or user_menu_input == "o":
            options_menu()
            
            options_menu_input = input("Select an option from the menu: ").lower()
            
            if options_menu_input == "ip" or options_menu_input == "ip address" or options_menu_input == "i":
                
                print("Please input the new IP address for the server to broadcast from")
                print()
                print("For testing purposes you can use '127.0.0.1' to have the program work with only 1 computer")
                print("If you want to test it with multiple computers, type the IP address of the computer that is going to host the server")
                print()
                print("To find you IP address, open command prompt, then type 'ipconfig' ")
                print("Next, find the address that reads 'IPv4 Address' under the type of connection your are using. (Wifi or Ethernet)")
                print()
                print("Default IP Addres: 127.0.0.1")
                
                new_ip_input = input()
                chat_room.server_ip = new_ip_input
            elif options_menu_input == "port" or options_menu_input == "port number" or options_menu_input == "p":
                print("Please input the port number you want the program to broadcast to")
                print("Make sure the the port number is not one that is used already")
                print()
                print("If you do not know what a port number is, then leave it default")
                print()
                print("Default port number: 2468")
            else:
                print("Invalid input, please try again. ")
            
        elif user_menu_input == "instructions" or user_menu_input == "i":
            program_instructions()
        elif user_menu_input == "exit" or user_menu_input == "e":
            exit()
        else:
            print("Invalid Input, please try again. ")
            
    
    

if __name__ == '__main__':
    main()