# 4. Given a two Python list. Write a program to iterate both lists simultaneously and display items from list 1 in original order and items from list 2 in reverse order.

def iterate_lists(lst1, lst2):
    for x, y in zip(lst1, lst2[::-1]):
        print(f'List 1 item: {x}, List 2 item: {y}')


list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
iterate_lists(list1, list2)

