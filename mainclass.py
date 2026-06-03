##############################################################################################################
#   Python Socket Programming Tutorial made by "Tech With Tim" https://www.youtube.com/watch?v=3QiPPX-KeSc   #
#   Python Sockets Simply Explained made by "NeuralNine" https://www.youtube.com/watch?v=YwWfKitB8aA         #
##############################################################################################################

import socket
import json
import os

class chat_room:
    
    def __init__(self, server_ip, server_port, username, client_socket):

        self._server_ip = server_ip
        self._server_port = server_port
        self._username = username
        
        self.client_socket = client_socket
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.users = []
    
    #Gets server IP address
    @property
    def server_ip(self):
        return self._server_ip
    
    #Sets server IP address
    @server_ip.setter
    def server_ip(self, new_ip):
        if len(new_ip) > 0 and len(new_ip) <= 15:
            self._server_ip = new_ip
        else:
            print("Invalid IP Address, please try again")
    
    #Gets server port number 
    @property
    def server_port(self):
        return self._server_port
    
    #Sets server port number
    @server_port.setter
    def server_port(self, new_port):
        #Rework for verification WIP!!
        if len(new_port) > 0 and len(new_port) < 6:
            self._server_port = new_port
    
    #Start the server using the given IP address and port number
    def start_server(self):
        self.server.bind((self.server_ip, self.server_port))
        self.server.listen()
        
        print("The server is using the using IP address: {self.server_ip}")
        print("The server is using the port number: {self.server_port}")
    
    #Adds users to the "users" list
    def add_user(self, user):
        self.users.append(user)
    
    #Remove users from the "users" list
    def remove_user(self, client_socket):
        for user in self.users.remove(user):
            if user.client_socket == client_socket:
                self.users.remove(user)
                
                return user
        return user

    def broastcast(self, message):
        for user in self.users:
            try:
                user.client_socket.send(message.encode(1024))
            except:
                pass
   
    def save_user(self, user):
        #os files and json file tutorial by w3schools
        
        user_info_file = "user_info.json"
        
        if not os.path.exists(user_info_file):
            with open(user_info_file, "w") as info_file:
                json.dump({user: []}, info_file, indent = 4)
                
        with open(user_info_file, "r") as info_file:
            json_data = json.load(info_file)
            
        file_exist = False
        
        for user_existing in json_data["users"]:
            if user_existing["username"] == chat_room.username:
                exist = True
                
        if not file_exist:
            json_data["users"].append({"username": user.username})
            
        with open(user_info_file, "w") as info_file:
            json.dump(json_data, info_file, indent = 4)
            
    def get_usernames(self):
        return [user.username for user in self.users]