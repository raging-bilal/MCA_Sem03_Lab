import csv
from collections import defaultdict

employees = []
with open("employees.txt", "r") as e_file:
    reader = csv.DictReader(e_file)
    for i in reader:
        i['Salary'] = float(i['Salary'])
        employees.append(i)

departments = {}
with open("departments.txt", "r") as d_file:
    reader = csv.DictReader(d_file)
    for i in reader:
        departments[i['DID']] = i['DName']

d_data = defaultdict(lambda: {'total_salary': 0, 'count': 0})
for e in employees:
    dept_id = e['DID']        
    salary = e['Salary']    
    d_data[dept_id]['total_salary'] += salary
    d_data[dept_id]['count'] += 1


print("The average salary of different department are as follows:")
for dept_id, data in d_data.items():
    
    avg_salary = data['total_salary'] / data['count']
    dept_name = departments[dept_id]
    print(f"{dept_name}: {avg_salary:.2f}")



