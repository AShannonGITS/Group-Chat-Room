class chat_room:
    
    def __init__(self, username, info, group_list, name_list, server_ip, server_port):
        self._username = username
        self._info = info
        self._group_list = group_list
        self._name_list = name_list
        self._server_ip = server_ip
        self._server_port = server_port
    
    #Gets server IP address
    @property
    def server_ip(self):
        return self._server_ip
    
    #Sets server IP address
    @server_ip.setter
    def server_ip(self, new_ip):
        if len(new_ip) > 0 and len(new_ip) < 15:
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
        if len(new_port) > 0 and len(new_port) < 6:
            self._server_port = new_port
    
    #Gets usernames
    @property
    def username(self):
        return self._username
    
    #Sets usernames
    @username.setter
    def username(self, new_username):
        if len(new_username) > 0:
            self._username = new_username
        else:
            print("Invalid username, please try again. ")
    
    #Gets user info
    @property
    def info(self):
        return self._info
    
    #sets user info
    @info.setter
    def info(self, new_info):
        if isinstance(new_info, str) and len(new_info) > 0:
            self._info = new_info
        else:
            print("Invalid input, please try again. ")
     
    #Gets user group       
    @property
    def group_list(self):
        return self._group_list
    
    #Sets user group
    @group_list.setter
    def group_list(self, new_group_list):
        print("WIP")
        #WIP!!