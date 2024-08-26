# 3. Write a Python program having a void function that receives a 4-digit number and calculates the sum of squares of first 2 digits’ number and last two digits’ number, e.g. if 1233 is passed as argument then function should calculate 122 + 332.



def sum_of_squares_of_digits(number):
    if len(str(number)) != 4:
        print("Please enter a 4-digit number.")
        return
    
    first_two_digits = int(str(number)[:2])
    last_two_digits = int(str(number)[-2:])
    
    result = first_two_digits**2 + last_two_digits**2
    print(f"The sum of squares is: {result}")


sum_of_squares_of_digits(1234)
