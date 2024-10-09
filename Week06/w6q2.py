# 2. Write a Python program to create a Python dictionary (the dictionary type). Add three names and their phone numbers in the dictionary. The names should act as a keys and phones as their values. Then ask the user a name and print its corresponding phone number.

d1={}



for i in range(3):
    name=input(f"Enter name {i+1}: ")
    pn=int(input("Enter phone number: "))
    d1[name]=pn


print(d1)

f1=input('Enter name to find phone number: ')
if f1 in d1:
    print(f"The phone number of {f1} is {d1[f1]}")

else:
    print("INVALID INPUT")
































