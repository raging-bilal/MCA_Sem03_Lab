# 5. Write a program to create a numpy array and return array of odd rows and even columns from the numpy array.



import numpy as np

my_array=np.array([
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
])

new_array=my_array[1::2, ::2]
print(new_array)
