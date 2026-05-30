##############################################################################################################
#   Python Socket Programming Tutorial made by "Tech With Tim" https://www.youtube.com/watch?v=3QiPPX-KeSc   #
#   Python Sockets Simply Explained made by "NeuralNine" https://www.youtube.com/watch?v=YwWfKitB8aA         #
##############################################################################################################

from mainclass import chat_room

import time
import socket

HOST = "127.0.0.1"
PORT = 2468

Valid = True

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

def main_server():
    while Valid == True:
        communication_socket, address = server.accept()
        print(f"Connected to {address}")
        message = communication_socket.recv(1024).decode("utf-8")
        print(f"Message from client: {message}")
        
        communication_socket.send(f"Message recived").encode("utf-8")