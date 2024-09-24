# 2. Write a program to pick a random character from a given String supplied by the user.

import random as ran

def random_char(my_string):
    if not my_string:
        return None
    else:
        return ran.choice(my_string)

my_string=input("Enter the String: ")

result=random_char(my_string)
print("The randomly generated character: ",result)
