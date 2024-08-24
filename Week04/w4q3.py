# 3. Given a list of numbers. Write a program to turn every item of a list into its square.

def square_list(lst):
    return [x ** 2 for x in lst]


numbers = [1, 2, 3, 4, 5]
squared_numbers = square_list(numbers)
print(squared_numbers)  

