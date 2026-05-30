class chat_room:
    
    def __init__(self, username, info, group_list, name_list):
        self._username = username
        self._info = info
        self._group_list = group_list
        self._name_list = name_list
        
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if len(new_username) > 0:
            self._username = new_username
        else:
            print("Invalid username, please try again. ")
    
    @property
    def info(self):
        return self._info
    
    @info.setter
    def info(self, new_info):
        if isinstance(new_info, str) and len(new_info) > 0:
            self._info = new_info
        else:
            print("Invalid input, please try again. ")
            
    @property
    def group_list(self):
        return self._group_list
    
    @group_list.setter
    def group_list(self, new_group_list):
        print("WIP")
        #WIP!!