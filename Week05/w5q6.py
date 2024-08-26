# 6. Write a program create a numpy array and sort as per below cases:

# a. Case 1: Sort array by the second row.

import numpy as np

# def sort_by_second_row(arr):
#     return arr[:, arr[1, :].argsort()]

# arr = np.array([[34, 12, 25, 45],
#                 [14, 10, 9, 21],
#                 [40, 32, 31, 20]])

# sorted_by_second_row = sort_by_second_row(arr)
# print("Array sorted by second row:\n", sorted_by_second_row)






# b. Case 2: Sort the array by the second column


def sort_by_second_column(arr):
    return arr[arr[:, 1].argsort()]

arr = np.array([[34, 12, 25, 45],
                [14, 10, 9, 21],
                [40, 32, 31, 20]])

sorted_by_second_column = sort_by_second_column(arr)
print("Array sorted by second column:\n", sorted_by_second_column)
