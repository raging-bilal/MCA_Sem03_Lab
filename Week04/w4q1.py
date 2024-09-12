# 1. Write a program to create function cal_sum_sub() such that it can accept two variables and calculate addition and subtraction.Also, it must return both addition and subtraction in a single return call.


def cal_sum_sub_mul_div(a,b):
    
    sum=a+b
    sub=a-b
    mul=a*b
    div=a//b

    return sum,sub,mul,div

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
sum,sub,mul,div= cal_sum_sub_mul_div(a,b)

print("The addition of {0} and {1} is {2}.".format(a,b,sum))
print("The difference of {0} and {1} is {2}.".format(a,b,sub))
print("The product of {0} and {1} is {2}.".format(a,b,mul))
print("The quotient of {0} and {1} is {2}.".format(a,b,div))










