class chat_room:
    
    def __init__(self, server_ip, server_port, username):

        self._server_ip = server_ip
        self._server_port = server_port
        self._username = username
    
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