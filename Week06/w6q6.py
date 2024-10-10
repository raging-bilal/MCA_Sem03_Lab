# 6. Write a program to accept a string and display the following:
# a. Number of uppercase characters
# b. Numbers of lowercase characters
# c. Total number of alphabets
# d. Number of digit

s=input("Enter the string: ")

n_u=0
n_l=0
n_a=0
n_d=0

for i in s:
    if i.isupper():
        n_u+=1
    if i.islower():
        n_l+=1
    if i.isalpha():
        n_a+=1
    if i.isdigit():
        n_d+=1

print("Upper case: ",n_u)
print("Lowercase: ", n_l)
print("Alphabet: ",n_a)
print("Digit: ",n_d)



