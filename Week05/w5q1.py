# 1. Write a program to generate 6 digit random secure OTP.




import secrets as sec

def generate_otp():
    otp=sec.randbelow(10**6)
    return f"{otp:06}"

result=generate_otp()
print("The 6 digits OTP: ",result)
















