class LoginUser:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def checkUserDetails(self):
        if(self.username == "san" and self.password =='123'):
            return True
        return False


