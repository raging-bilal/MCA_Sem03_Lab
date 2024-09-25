# 4. Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.



n1=int(input("Enter l1 length: "))
l1=[0]*n1
for i in range(n1):
    l1[i]=int(input(">> "))
print(l1)

n2=int(input("Enter l2 length: "))
l2=[0]*2
for i in range(n2):
    l2[i]=int(input(">> "))
print(l2)


l3=[]
for i in l1:
    if i%2!=0:
        l3.append(i)
for i in l2:
    if i%2==0:
        l3.append(i)
print("The final list: ")
print(l3)
