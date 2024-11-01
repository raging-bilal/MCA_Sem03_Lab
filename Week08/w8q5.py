# 5. Write a python program that reads a string which contains English alphabets and numbers. The program should create two lists L1 and L2, where L1 includes all the numbers present in the string while L2 includes all the alphabets of the string.


def separate(s):
    l1=[]
    l2=[]

    for i in s:
        if i.isdigit():
            l1.append(int(i))

        elif i.isalpha:
            l2.append(i)


    return l1,l2

s=input("Enter the string: ")
l1,l2=separate(s)

print("List of digits: ",l1)
print("List of alphabets: ",l2)


