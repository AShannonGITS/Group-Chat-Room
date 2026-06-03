################################################################################################################
#   "Python Socket Programming Tutorial" made by "Tech With Tim" https://www.youtube.com/watch?v=3QiPPX-KeSc   #
#   "Python Sockets Simply Explained" made by "NeuralNine" https://www.youtube.com/watch?v=YwWfKitB8aA         #
################################################################################################################

from mainclass import chat_room

from mainfuntions import write_chat_log

import time
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((chat_room.server_ip, chat_room.server_port))


server.listen()

def main_server():
    chat_room.start_server()
    
    host_name = input("Enter the name of the owner of the server: ")
    hosting_user = chat_room(host_name, "N/A", "N/A")
    
    chat_room.save_user_info(hosting_user)
    
    receive_thread = threading.Thread(target = receive_connections, daemon = True)
    receive_thread.start()
    
    print("Server started!")
    server_chat(host_name)
    
def client_handling(client):
    Valid = True
    
    while Valid == True:
        try:
            message = client.recv(1024).decode()
            print(message)
            
            username = "Unknown username"
            
            for user in chat_room.users:
                if user.client_socket == client:
                    username = user.username
                    
            chat_room.broadcast(message)
        except:
            exit()
            
def receive_connections():
    Valid = True
    
    while Valid == True:
        client, address = chat_room.server.accept()
        
        print(f"Client '{address}' has connected.")
        client.send("username".encode())
        
        username = client.recv(1024).decode()
        user = chat_room(username)
        
        chat_room.add_user(user)
        chat_room.save_user_info(user)
        
        chat_room.broadcast(f"{username} has joined the chat!")
        
        thread = threading.Thread(target = client_handling, args = (client,))
        thread.start()
        
def server_chat(host_name):
    Valid = True
    
    while Valid == True:
        message = input()
            
        chat_log_message = (f"{host_name}: {message}")
        print(chat_log_message)
        
        write_chat_log(message, host_name)
        
        chat_room.broadcast(chat_log_message)
        
