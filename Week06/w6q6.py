# 6. Write a program to accept a string and display the following:
# a. Number of uppercase characters
# b. Numbers of lowercase characters
# c. Total number of alphabets
# d. Number of digit


def analyze_string(input_string):
    uppercase_count = sum(1 for char in input_string if char.isupper())
    lowercase_count = sum(1 for char in input_string if char.islower())
    alphabet_count = sum(1 for char in input_string if char.isalpha())
    digit_count = sum(1 for char in input_string if char.isdigit())

    print(f"Number of uppercase characters: {uppercase_count}")
    print(f"Number of lowercase characters: {lowercase_count}")
    print(f"Total number of alphabets: {alphabet_count}")
    print(f"Number of digits: {digit_count}")


input_string = input("Enter a string: ")
analyze_string(input_string)
