# 4. Write a program to accept a string from the user and display characters that are present at an even index number.


s=input("Enter the String: ")
l=len(s)
print("The length of the string is: ", l)



print("Print characters from a string which are present at an even index numbers:")

for i in range(0,l,2):
    print(s[i],end=" ")

