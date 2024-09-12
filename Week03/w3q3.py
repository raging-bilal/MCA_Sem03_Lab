# 3. Write a program to print characters from a string which are present at an even index numbers.

s="Khushnood"
l=len(s)
print("The length of the string is: ", l)



print("Print characters from a string which are present at an even index numbers:")

for i in range(0,l,2):
    print(s[i],end=" ")

