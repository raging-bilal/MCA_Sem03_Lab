from collections import defaultdict

program_courses = defaultdict(int)

with open("program_courses.txt", "r") as file:
    for line in file:
        program, course = line.strip().split(',')
        
        program_courses[program] += 1

print("The number of courses for each program")

for program, count in program_courses.items():
    print(f"{program}: {count}")
