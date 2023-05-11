import string
from random import choice

def get_new_password(password_length:int):
    characters = string.ascii_letters + string.punctuation  + string.digits
    return "".join(choice(characters) for x in range(0,password_length))

