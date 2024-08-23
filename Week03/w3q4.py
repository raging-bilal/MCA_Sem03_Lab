# 4. Write a program to accept a string from the user and display characters that are present at an even index number.


str = input("Enter a string: ")

for i in range(0, len(str), 2):
    print(str[i])
