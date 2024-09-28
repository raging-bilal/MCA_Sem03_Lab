# 2. Write a Python program to create a Python dictionary (the dictionary type). Add three names and their phone numbers in the dictionary. The names should act as a keys and phones as their values. Then ask the user a name and print its corresponding phone number.


def create_phone_book():
    phone_book = {}
  
    for _ in range(3):
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        phone_book[name] = phone_number



    
    
    lookup_name = input("Enter name to look up: ")
    if lookup_name in phone_book:
        print(f"The phone number for {lookup_name} is {phone_book[lookup_name]}")
    else:
        print(f"{lookup_name} is not in the phone book.")

create_phone_book()
