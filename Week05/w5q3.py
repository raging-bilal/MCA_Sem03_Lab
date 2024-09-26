# 3. Write a program to generate a random Password which meets the following conditions

# a. Password length must be 10 characters long.
# b. It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.


import random as ran
import string as str

U=str.ascii_uppercase
L=str.ascii_lowercase
D=str.digits
S=str.punctuation

password=[]
password.extend(ran.choices(U,k=2))
password.append(ran.choice(D))
password.append(ran.choice(S))

rem_len=10-len(password)

all_char=U+L+D+S
password.extend(ran.choices(all_char,k=rem_len))

ran.shuffle(password)
password="".join(password)
print("The generated password: ")
print(password)
