import re
import string


def password_validator():
    while True:
        password = input("Please enter a password: ")
        special_characters = set(string.punctuation)
        if len(password) < 8:
            print("Password should contain at least one special character.")
        elif not re.search(r'[a-z]', password):
            print("Password should contain at least one lowercase letter.")
        elif not re.search(r'[A-Z]', password):
            print("Password should contain at least one uppercase letter.")
        elif not re.search(r'[0-9]', password):
            print("Password should contain at least one number.")
        elif not any(char in special_characters for char in password):
            print("Password should contain at least one special character.")
        else:
            print("Password is valid.")
            return password

valid_password = password_validator()
print("Valid password:", valid_password)