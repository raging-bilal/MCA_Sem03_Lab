import csv
file1 = 'employees.csv'
file2 = 'employees_with_HRA.csv'

with open(file1, 'r', newline='') as f1:
    reader = csv.DictReader(f1)
    fieldnames = reader.fieldnames + ['HRA']
    
    with open(file2, 'w', newline='') as f2:
        writer = csv.DictWriter(f2, fieldnames=fieldnames)
        
        writer.writeheader()
        for row in reader:
            salary = float(row['Salary'])
            hra = 0.18 * salary
            row['HRA'] = round(hra, 2)
            writer.writerow(row)

print(f"File with HRA column saved as '{file2}'.")
