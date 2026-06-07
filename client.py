##############################################################################################################
#   Python Socket Programming Tutorial made by "Tech With Tim" https://www.youtube.com/watch?v=3QiPPX-KeSc   #
#   Python Sockets Simply Explained made by "NeuralNine" https://www.youtube.com/watch?v=YwWfKitB8aA         #
#   Threading tutorial made by "NeuralNine" https://www.youtube.com/watch?v=A_Z1lgZLSNc                      #
##############################################################################################################

import socket
import threading

username = ""

"""
Receives the message from the server
"""
def receive_messages(client):
    global username

    Valid = True
    while Valid == True:
        try:
            message = client.recv(1024).decode()

            if message == "USERNAME":
                client.send(username.encode())
            else:
                print(message)
        except:
            print("Disconnected from server.")
            client.close()
            
            Valid = False

"""
Sends the messages to the server
"""
def send_messages(client):
    global username

    Valid = True
    while Valid == True:
        try:
            message = input()
            if message.strip() == "":
                continue

            full_message = f"{username}: {message}"
            client.send(full_message.encode())
        except:
            client.close()
            
            Valid = False

"""
Starts and runs the main client connection to the server
"""
def main_client():
    global username

    ip = input("Server IP: ")
    port = int(input("Server Port: "))
    username = input("Your Username: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((ip, port))
    except ValueError:
        print("Unable to connect to server.")
        
        return

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    send_thread = threading.Thread(target=send_messages, args=(client,))

    receive_thread.start()
    send_thread.start()