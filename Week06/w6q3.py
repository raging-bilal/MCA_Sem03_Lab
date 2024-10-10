# 3. Write a Python program having a void function that receives a 4-digit number and calculates the sum of squares of first 2 digits’ number and last two digits’ number, e.g. if 1233 is passed as argument then function should calculate 122 + 332.



def sqnum(num):
    if len(str(num))!=4:
        return "INVALID INPUT, Enter 4 digit number only!"

    else:
        s1=int(str(num)[:2])
        s2=int(str(num)[-2:])
        res=s1**2 + s2**2
        return res


num=int(input('Enter 4 digit number: '))
print(sqnum(num))
