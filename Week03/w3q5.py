# 5. Write a program to remove characters from a string starting from n to last and return a new string. Example: remove_char ("aligarh", 3) so output must be al



def remove_char(s,n):
    return s[0:n-1]

s="aligarh"
n=3

r=remove_char(s,n)

print(r)
