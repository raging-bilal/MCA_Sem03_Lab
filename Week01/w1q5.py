# Write a program to calculate the cube of all numbers from 1 to a given number.

num=int(input("Enter a number till we want to calculate the cube: "))

for i in range(num):
    print(f"The cube of {i+1} is: ",(i+1)**3)
    
