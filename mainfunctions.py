####################################################################################################
#   Tutorial for datetime made by w3schools https://www.w3schools.com/python/python_datetime.asp   #
####################################################################################################

import time
from datetime import datetime


"""
This displays the main menu instructions.
"""
def main_instructions():
    print("-----------------")
    print("|     Start     |")
    print("|    Options    |")
    print("|  Instructions |")
    print("|      Exit     |")
    print("-----------------")
    print()


"""
This displays the program instrustions.
"""
def program_instructions():
    print("This progam is a group chat that is run on the local network.")
    print("One computer runs the server, and other computers on the same network can connect to them using that computer's IP address.")
    print()
    time.sleep(0.5)
    print("If you testing this program with only one computer leave the default options. Otherwise change the IP address, and the port number in the options.")
    print("To find your computer IP address, first open Command Prompt, then type 'ipconfig'.")
    print("Find where it says 'IPv4 Address' under where it says your type of newtork connection (Wifi or Ethernet).")
    print("Using that IP address input that into the options menu.")
    time.sleep(0.5)
    print()
    print("For the port number, either leave it as default if you have not used that port number. Or change it if that port number is already used.")

"""
This displays the server instructions.
""" 
def server_instructions():
    time.sleep(0.5)
    print()
    print("When you start the server it will say 'Server started on 'your IP Address': 'your Port Number' '")
    print("These are the number you need to remember when you are using the client to connect to the server.")
    print("Pick the username you would like to use when chatting.")

"""
This displays the client instructions.
"""     
def client_instructions():
    time.sleep(0.5)
    print()
    print("First, type the IP address of server. If unchanged it will be '127.0.0.1' this means that the client and the server must be run on the same computer.")
    print("Then type the port number of the server. If unchanged it will be '2468'.")
    print("Next, type your username that will be used it the chat.")
    print()

"""
This displays the options menu.
"""     
def options_menu():
    print()
    time.sleep(0.25)
    print("First type the IP address of the computer that is running this program. When you run the 'server' this is the IP address that will be used by the clients to connect from.")
    print("For testing purposes leave it as the default IP address, so you can test it on one computer.")
    print("Default IP: 127.0.0.1")
    time.sleep(0.5)
    print()
    print("Type the port number you would like the program to use. When you run the 'server' this is the port number that the clients will use to connect to this computer.")
    print("For testing purposes leave it as the default port number, so you can test it on one computer.")
    print("Default Port Number: 2468")
    print()

"""
This writes the chat history into a txt file.
"""     
def write_chat_log(message):
    #From w3schools
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("chat_log.txt", "a") as chat_log:
        chat_log.write(f"[{time_stamp}] {message}\n")