# 1. Write a program to generate 6 digit random secure OTP.

import secrets

def generate_otp():
    otp = secrets.randbelow(10**6)
    return f'{otp:06}'  

otp = generate_otp()
print("Generated OTP:", otp)

















