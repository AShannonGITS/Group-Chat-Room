##############################################################################################################
#   Python Socket Programming Tutorial made by "Tech With Tim" https://www.youtube.com/watch?v=3QiPPX-KeSc   #
#   Python Sockets Simply Explained made by "NeuralNine" https://www.youtube.com/watch?v=YwWfKitB8aA         #
#   Threading tutorial made by (PLACE LINK HERE!)   #
##############################################################################################################

import time
import socket
import threading

Valid = True

def main_client():
    while Valid == True:
        global username
        
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((connecting_ip, connecting_port))
        
        connecting_ip = input("Please enter the IP Address of the server you would like to connect to: ")
        time.sleep(0.25)
        connecting_port = int(input("Please enter the port number of the server you would like to connect to: "))
        time.sleep(0.25)
        
        username = input("Please enter your username: ")
        
        #Threading tutorial made by (PLACE LINK HERE!)
        receive_thread = threading.Thread(target = recive_message, args = (client,))
        receive_thread.start()
        
        send_thread = threading.Thread(target = send_message, args = (client,))
        send_thread.start()
        
def recive_message(client):
    Valid = True
    
    while Valid == True:
        try:
            message = client.recv(1024).decode()
            
            if message == "username":
                client.send(username.encode())
            else:
                print("Invalid input please try again.")
        except:
            print("Disconnected")
            client.close
            
            exit()
            
def send_message(client):
    Valid = True
    
    while Valid == True:
        message = input()
        
        chat_log_message = (f"{username}: {message}")
        client.send(chat_log_message.encode())