# 5. Write a program to get roll numbers, names and marks of the students of a class (get from user) and store these details in a file called “Marks.data”


def store_student_data():


    num_students = int(input("Enter number of students: "))
    with open("Marks.data", "w") as file:

        for _ in range(num_students):
            roll_number = input("Enter roll number: ")
            name = input("Enter name: ")
            marks = input("Enter marks: ")
            file.write(f"{roll_number},{name},{marks}\n")
            
    print("Student data has been saved to 'Marks.data'.")

store_student_data()
