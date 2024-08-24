# 2. Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.


def is_first_last_same(lst):
    if len(lst) < 1:
        return False  
    return lst[0] == lst[-1]


print(is_first_last_same([10, 20, 30, 40, 10]))  
print(is_first_last_same([10, 20, 30, 40, 50]))  
