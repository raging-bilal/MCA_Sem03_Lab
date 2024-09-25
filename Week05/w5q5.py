# 5. Write a program to create a numpy array and return array of odd rows and even columns from the numpy array.




import numpy as np

rl=int(input("Enter the number of rows: "))
cl=int(input("Enter the number of columns: "))

my_array=np.random.randint(1,100,(rl,cl))


print(my_array)

rows=my_array[::2,:]
cols=my_array[:,1::2]

print("rows: " ,rows)
print("cols: " ,cols)
