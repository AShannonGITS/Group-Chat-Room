##############################################################################################################
#   Python Socket Programming Tutorial made by "Tech With Tim" https://www.youtube.com/watch?v=3QiPPX-KeSc   #
#   Python Sockets Simply Explained made by "NeuralNine" https://www.youtube.com/watch?v=YwWfKitB8aA         #
##############################################################################################################

from mainclass import chat_room

import time
import socket

Valid = True

def main_client():
    while Valid == True:
        user_ip_input = input("What IP Address would you like to connect to? ")
        user_port_input = input("What port number would you like to connect to? ")
        
        