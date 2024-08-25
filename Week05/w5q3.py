# 3. Write a program to generate a random Password which meets the following conditions

# a. Password length must be 10 characters long.
# b. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.

import random
import string
import secrets

def generate_password():
    
    upper_case = ''.join(secrets.choice(string.ascii_uppercase) for _ in range(2))
    digits = secrets.choice(string.digits)
    special_symbol = secrets.choice(string.punctuation)
    
    
    remaining_length = 10 - len(upper_case + digits + special_symbol)
    other_chars = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))
    
   
    password_list = list(upper_case + digits + special_symbol + other_chars)
    random.shuffle(password_list)
    
    return ''.join(password_list)

password = generate_password()
print("Generated Password:", password)

