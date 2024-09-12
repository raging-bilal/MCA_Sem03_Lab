# 4. Given a two Python list. Write a program to iterate both lists simultaneously and display items from list 1 in original order and items from list 2 in reverse order.

a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]


b_rev = b[::-1]


for item_a, item_b in zip(a, b_rev):
    print(item_a, item_b)
