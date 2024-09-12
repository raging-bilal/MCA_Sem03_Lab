# 3. Given a list of numbers. Write a program to turn every item of a list into its square.

a=[1,2,3,4,5]
l=len(a)

print(a)


print("The list of square are as follows: ")
for i in range(0,l):
    sq=a[i] * a[i]

    print(sq , end="  ")
