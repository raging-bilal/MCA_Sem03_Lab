# 2. Write a program to pick a random character from a given String supplied by the user.

import random



def pick_random_char(user_string):
    if not user_string:
        return None  
    return random.choice(user_string)

user_string = input("Enter a string: ")
random_char = pick_random_char(user_string)
print("Randomly selected character:", random_char)
