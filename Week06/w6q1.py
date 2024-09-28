# 1. Write a Python program that inputs two tuples and creates a third that contains all elements of the first followed by all elements of the second. (You may use other data types such as lists etc. to make your program work)



def concatenate_tuples(tuple1, tuple2):
    
    concatenated_tuple = tuple(list(tuple1) + list(tuple2))
    return concatenated_tuple




tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = concatenate_tuples(tuple1, tuple2)
print("Concatenated Tuple:", result)











