from mainclass import chat_room

import socket
import time

def main_instructions():
    print("Test 1")

def main_program():
    print("Main test 1")

def program_instructions():
    print("Test 2")
    
def options_menu():
    print("Options Test 1")
    
def chat_log(message, author):
    with open("chat_log.txt", "a") as log:
        log.write(f"    By:{author} \n")
        log.write(f"{message} \n")
        
def chat_log_search():
    moderator_input = input("Which message would you like to find? ")
    
    with open("chat_log.txt", "r") as log_search:
        log_search.read(moderator_input)
        #WIP!!!
        
def write_user_info(user_info_input):
    with open("user_info.txt", "a") as w_user_info:
        w_user_info.write(f"{user_info_input} \n")
        #WIP!!!
        
def read_user_info(user):
    with open("user_info.txt", "r") as r_user_info:
        r_user_info.read(user)