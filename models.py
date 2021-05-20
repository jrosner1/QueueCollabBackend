import api

class UserModel():
    def __init__(self, username, password, email):
        if not isinstance(username, str) or not isinstance(password, str) or not isinstance(email, str):
            raise TypeError("Both username and password must be strings")
        
        self.username = username
        self.password = password

    def save_to_db(self):
        

    
