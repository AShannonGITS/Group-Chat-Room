##############################################################################################################
#   Python Socket Programming Tutorial made by "Tech With Tim" https://www.youtube.com/watch?v=3QiPPX-KeSc   #
#   Python Sockets Simply Explained made by "NeuralNine" https://www.youtube.com/watch?v=YwWfKitB8aA         #
##############################################################################################################

import socket


class User:
    def __init__(self, username, client_socket):
        self.username = username
        self.client_socket = client_socket

class ChatRoom:
    def __init__(self, server_ip = "127.0.0.1", server_port = 2468):
        self._server_ip = server_ip
        self._server_port = server_port

        self.users = []

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #Gets the server IP address
    @property
    def server_ip(self):
        return self._server_ip

    #Set the IP Address
    @server_ip.setter
    def server_ip(self, new_ip):
        self._server_ip = new_ip

    #Gets the server port number
    @property
    def server_port(self):
        return self._server_port

    #sets the server port number
    @server_port.setter
    def server_port(self, new_port):
        if 1 <= new_port <= 65535:
            self._server_port = new_port
        else:
            print("Invalid port number. Please try again")

    #Binds the server IP and port number to the program, then starts the server.
    def start_server(self):
        self.server.bind((self.server_ip, self.server_port))
        self.server.listen()

        print(f"\nServer started on {self.server_ip}: {self.server_port}")

    #Adds a users to the 'users' list
    def add_user(self, user):
        self.users.append(user)

    #Removes a users from the 'users' list.
    def remove_user(self, client_socket):
        for user in self.users:
            if user.client_socket == client_socket:
                self.users.remove(user)
                return user

        return None

    #Send messages to all users
    def broadcast(self, message):
        for user in self.users:
            try:
                user.client_socket.send(message.encode())
            except:
                pass

    #Gets the usernames from the list
    def get_usernames(self):
        return [user.username for user in self.users]

chatroom = ChatRoom()