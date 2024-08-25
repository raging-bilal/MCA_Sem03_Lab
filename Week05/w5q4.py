# 4. Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.


def create_custom_list(list1, list2):
    odd_from_list1 = [num for num in list1 if num % 2 != 0]
    even_from_list2 = [num for num in list2 if num % 2 == 0]
    return odd_from_list1 + even_from_list2

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
new_list = create_custom_list(list1, list2)
print("New List:", new_list)
