################################################################################################################
#   "Python Socket Programming Tutorial" made by "Tech With Tim" https://www.youtube.com/watch?v=3QiPPX-KeSc   #
#   "Python Sockets Simply Explained" made by "NeuralNine" https://www.youtube.com/watch?v=YwWfKitB8aA         #
################################################################################################################

from mainclass import chat_room

import time
import socket

Valid = True

chatlog = "chat_log.txt"
userinfo = "user_info.json"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((chat_room.server_ip, chat_room.server_port))


server.listen()

def main_server():
    while Valid == True:
        print("Temp")