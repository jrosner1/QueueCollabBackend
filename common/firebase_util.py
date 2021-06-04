from firebase_admin import auth, exceptions

def get_user_object_from_email(email):
    user = auth.get_user_by_email(email)
    return user.toJSON()

def create_user(email_input, display_name_input, password_input, phone_number_input):
    try:
        user = auth.create_user(
            email = email_input,
            email_verified = False,
            display_name = display_name_input,
            password = password_input,
            phone_number = phone_number_input,
            disabled = False
        )
        return user
    
    except exceptions.FireBaseError as ex:
        print(f'failed to create new user: {ex}')







