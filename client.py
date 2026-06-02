##############################################################################################################
#   Python Socket Programming Tutorial made by "Tech With Tim" https://www.youtube.com/watch?v=3QiPPX-KeSc   #
#   Python Sockets Simply Explained made by "NeuralNine" https://www.youtube.com/watch?v=YwWfKitB8aA         #
##############################################################################################################

from mainclass import chat_room

import time
import socket

Valid = True

chatlog = "chat_log.txt"
userinfo = "user_info.json"

def main_client():
    while Valid == True:
        print("Temp")