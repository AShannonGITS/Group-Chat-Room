####################################################################################################
#   Tutorial for datetime made by w3schools https://www.w3schools.com/python/python_datetime.asp   #
####################################################################################################

from datetime import datetime

def main_instructions():
    print("This program is a chat room that multiple clients can connect to.")
    print('First, either type "server" to run a chat room server or type "client" to connect to a server run on your local network')
    print()

def program_instructions():
    print("Test 2")
    
def options_menu():
    print("Options Test 1")
    
def write_chat_log(message, author):
    #From w3schools
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("chat_log.txt", "a") as chat_log:
        chat_log.write(f"[{time_stamp}] {author} {message}")