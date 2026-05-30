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

def main_client():
    while Valid == True:
        print()