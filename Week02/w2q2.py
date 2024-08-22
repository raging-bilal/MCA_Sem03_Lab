# Write a program to count the total number of digits in a number using a while loop.




def count_digits(num):
    count = 0
    while num > 0:
        num = num // 10  
        count += 1  
    return count



num = int(input("Enter an integer: "))
total_digits = count_digits(num)
print("The total number of digits are: ", total_digits)



