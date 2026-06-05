################################################################################################################
#   "Python Socket Programming Tutorial" made by "Tech With Tim" https://www.youtube.com/watch?v=3QiPPX-KeSc   #
#   "Python Sockets Simply Explained" made by "NeuralNine" https://www.youtube.com/watch?v=YwWfKitB8aA         #
################################################################################################################

import threading

from mainclass import chatroom, User
from mainfunctions import write_chat_log

#Recives messages from the clients and logs them
def handle_client(client):
    Valid = True
    
    while Valid == True:
        try:
            message = client.recv(1024).decode()
            print(message)

            write_chat_log(message)
            chatroom.broadcast(message)
        except:
            Valid = False

    user = chatroom.remove_user(client)

    if user:
        print(f"{user.username} disconnected.")
        chatroom.broadcast(f"{user.username} left the chat.")

    client.close()

#Receives the connections from the client
def receive_connections():
    Valid = True
    
    while Valid == True:
        client, address = chatroom.server.accept()

        print(f"A client has connect from {address}")

        client.send("USERNAME".encode())
        username = client.recv(1024).decode()
        user = User(username, client)

        chatroom.add_user(user)
        chatroom.broadcast(f"{username} joined the chat.")

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

#Allow the server to send messages
def server_chat(server_name):
    Valid = True
    
    while Valid == True:
        message = input()

        if message.strip() == "":
            continue

        full_message = f"{server_name}: {message}"
        print(full_message)

        write_chat_log(message)
        chatroom.broadcast(full_message)

#Runs the main server
def main_server():
    chatroom.start_server()

    server_name = input("Your username name: ")

    receive_thread = threading.Thread(target=receive_connections, daemon = True)
    receive_thread.start()

    print("\nServer chat enabled.")
    print("Clients can now connect.\n")

    server_chat(server_name)