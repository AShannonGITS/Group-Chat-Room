################################################################################################################
#   "Python Socket Programming Tutorial" made by "Tech With Tim" https://www.youtube.com/watch?v=3QiPPX-KeSc   #
#   "Python Sockets Simply Explained" made by "NeuralNine" https://www.youtube.com/watch?v=YwWfKitB8aA         #
################################################################################################################

import threading

from mainclass import room, User
from mainfunctions import write_chat_log


def handle_client(client):
    Valid = True
    
    while Valid == True:
        try:
            message = client.recv(1024).decode()

            if not message:
                break

            print(message)

            username = "Unknown"

            for user in room.users:
                if user.client_socket == client:
                    username = user.username
                    break

            write_chat_log(message, username)

            room.broadcast(message)
        except:
            Valid = False

    user = room.remove_user(client)

    if user:
        print(f"{user.username} disconnected.")
        room.broadcast(f"{user.username} left the chat.")

    client.close()


def receive_connections():
    Valid = True
    
    while Valid == True:
        client, address = room.server.accept()

        print(f"Connected to {address}")

        client.send("USERNAME".encode())
        username = client.recv(1024).decode()
        user = User(username, client)

        room.add_user(user)
        room.broadcast(f"{username} joined the chat.")

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


def server_chat(server_name):
    Valid = True
    
    while Valid == True:
        message = input()

        if message.strip() == "":
            continue

        full_message = f"{server_name}: {message}"
        print(full_message)

        write_chat_log(message, server_name)
        room.broadcast(full_message)


def main_server():
    room.start_server()

    server_name = input("Server name: ")

    receive_thread = threading.Thread(target=receive_connections, daemon=True)
    receive_thread.start()

    print("\nServer chat enabled.")
    print("Clients may now connect.\n")

    server_chat(server_name)