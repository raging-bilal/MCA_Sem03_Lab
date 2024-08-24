# 1. Write a program to create function cal_sum_sub() such that it can accept two variables and calculate addition and subtraction.Also, it must return both addition and subtraction in a single return call.


def cal_sum_sub(a, b):
    addition = a + b
    subtraction = a - b
    return addition, subtraction


result = cal_sum_sub(10, 5)
print("Addition:", result[0])
print("Subtraction:", result[1])










