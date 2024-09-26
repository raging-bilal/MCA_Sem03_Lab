# 6. Write a program create a numpy array and sort as per below cases:
import numpy as np

arr=np.array(np.random.randint(0,100,(4,5)))
print("Original array: ")
print(arr)

# a. Case 1: Sort array by the second row.
by_row=arr[:,arr[1,:].argsort()]


print("Sort by Second Row: ")
print(by_row)



# b. Case 2: Sort the array by the second column

by_col=arr[arr[:,1].argsort(),:]


print("Sort by Second Column: ")
print(by_col)






