# Write a program to Iterate the supplied list of 20 numbers by the user and print only those numbers which are divisible by 5.


n=int(input("Enter the length of list: "))
lst=[0]*n

for i in range(n):
    lst[i]=int(input(f"Enter the {i+1} elements of the list: "))

print("The final list: ",lst)




new_lst=[]
for i in lst:
    if i%5==0:
        new_lst.append(i)
        
print("Print only those numbers which are divisible by 5")
print(new_lst)




