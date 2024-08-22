# Write a Program to extract each digit from an integer in the reverse order.


def reverse_digits(num):
    while num > 0:
        digit = num % 10  
        print(digit, end=' ')  
        num = num // 10  



num = int(input("Enter an integer: "))
reverse_digits(num)
