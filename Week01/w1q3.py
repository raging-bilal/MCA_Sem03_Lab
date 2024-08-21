# Write a program to Iterate the supplied list of 20 numbers by the user and print only those numbers which are divisible by 5.

limit=5
lst=[]
i=1
while i<=limit:
    num=int(input("Enter 5 values in the list: "))
    lst.append(num)
    i+=1

print(lst)

for num in lst:
    if num % 5==0:
        print(num)
    








