from common.firebase_util import create_user
import datetime as dt

class UserModel:
    def __init__(self, name, email, display_name, password, phone_number, email_verified):
        self.name = name
        self.created_at = dt.datetime.now()
        self.email_verified = email_verified
        self.email = email
        self.display_name = display_name
        self.password = password
        self.email_verified = False
        self.phone_number = phone_number


    def save_to_db(self):
        create_user(self.email, self.display_name, self.password, self.phone_number)