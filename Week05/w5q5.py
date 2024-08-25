# 5. Write a program to create a numpy array and return array of odd rows and even columns from the numpy array.


import numpy as np

def get_odd_rows_even_columns(arr):
    return arr[1::2, ::2]  

arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

result = get_odd_rows_even_columns(arr)
print("Array of odd rows and even columns:\n", result)
