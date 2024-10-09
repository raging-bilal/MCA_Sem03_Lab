# 1. Write a Python program that inputs two tuples and creates a third that contains all elements of the first followed by all elements of the second. (You may use other data types such as lists etc. to make your program work)


l1=[]
print('Enter the elements of l1 and press ENTER to quit:')
while True:
    tmp=input(">> ")
    if tmp=="":
        break
    l1.append(tmp)
print("Tuple 1: ",tuple(l1))

l2=[]
print('Enter the elements of l2 and press ENTER to quit:')
while True:
    tmp=input(">> ")
    if tmp=="":
        break
    l2.append(tmp)
print("Tuple 2: ",tuple(l2))

l3=l1+l2
print("The final tuple l3 are as follows:")
print("Tuple 3: ",tuple(l3))



