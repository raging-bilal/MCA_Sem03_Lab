# Write a program to find product of two user supplied integers and if the productis equal to or lower than 5000 then return sum of the two numbers.


num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))

product= num1 * num2

print(product)

if product <=5000:
    print(num1 + num2)

else:
    print(product)
