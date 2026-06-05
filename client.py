##############################################################################################################
#   Python Socket Programming Tutorial made by "Tech With Tim" https://www.youtube.com/watch?v=3QiPPX-KeSc   #
#   Python Sockets Simply Explained made by "NeuralNine" https://www.youtube.com/watch?v=YwWfKitB8aA         #
#   Threading tutorial made by (PLACE LINK HERE!)   #
##############################################################################################################

import socket
import threading

username = ""

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


def main_client():
    global username

    ip = input("Server IP: ")
    port = int(input("Server Port: "))
    username = input("Your Username: ")

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((ip, port))
    except:
        print("Unable to connect to server.")
        
        return

    receive_thread = threading.Thread(target=receive_messages, args=(client,))

    send_thread = threading.Thread(target=send_messages, args=(client,))

    receive_thread.start()
    send_thread.start()