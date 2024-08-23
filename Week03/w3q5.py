# 5. Write a program to remove characters from a string starting from n to last and return a new string. Example: remove_char ("aligarh", 3) so output must be al



def remove_characters(string, n):
    return string[:n]  

result = remove_characters("aligarh", 2)
print(result)  

