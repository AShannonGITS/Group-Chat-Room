#########################################################################################################################################
#   Tutorial for json files made by GeeksforGeeks  https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/   #
#########################################################################################################################################

from mainclass import chat_room

import socket
import time
import json

def main_instructions():
    print("This program is a chat room that multiple clients can connect to.")
    print('First, either type "server" to run a chat room server or type "client" to connect to a server run on your local network')

def program_instructions():
    print("Test 2")
    
def options_menu():
    print("Options Test 1")
    
def client_chat(message):
    chatting = True
    
    while chatting == True:
        print()
        #WIP

def write_chat_log(message, author):
    with open("chat_log.txt", "a") as log:
        log.write(f"    By:{author} \n")
        log.write(f"{message} \n")
        
def chat_log_search(server_input):
    server_input = input("Which message would you like to find? ").lower()
    
    with open("chat_log.txt", "r") as log_search:
        log_search.read(server_input)
        #WIP!!!
        
def write_user_info(user_info_input):
    print("")
    # Use JSON
        
def read_user_info(user):
    print("")
    # Use JSON
        
def write_group_info(user_group_input):
    print("")
    # Use JSON
        
def read_group_info(group):
    print("")
    # Use JSON
        
def server_console(console_input_valid):
    while console_input_valid == True:
            server_input = input("").lower()
            
            if server_input == "chat log search" or server_input == "log search":
                print("log search")
            elif server_input == "edit user info" or server_input == "edit info":
                print("edit user info")
            elif server_input == "stop chat" or server_input == "stop":
                print("stop chat")
            elif server_input == "" or server_input == "":
                print("4")
            elif server_input == "stop server" or server_input == "server stop":
                print("stop server")
            else:
                print("Invalid input please try again. ")