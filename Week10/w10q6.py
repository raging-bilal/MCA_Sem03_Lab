# 6# Consider two files that contain information about Employees and Departments in the following parameters: Employee 
# (Name, EId, Salary, DID), Department (DID, DName, DLocation).  
# Write a Python program to merge the content of both the file in following format.: Emp_Dep(Ename, Eid, Esalary, EDID, DName,Dlocation)  
# (Note: Merging should follow the condition-DID of Employee file should be equal to Department ID of department file) 




def read_edata(e_file):
    emp = {}
    with open(e_file, 'r') as f:
        for line in f:
            name, eid, salary, did = line.strip().split(',')
            emp[did] = (name, eid, salary)
    return emp

def read_ddata(d_file):
    dept = {}
    with open(d_file, 'r') as f:
        for line in f:
            did, dname, dlocation = line.strip().split(',')
            dept[did] = (dname, dlocation)
    return dept

def merge_e_d(e_file, d_file, output_file):
    emp = read_edata(e_file)
    dept= read_ddata(d_file)
    
    with open(output_file, 'w') as f:
        for did, emp_data in emp.items():
            if did in dept:
                name, eid, salary = emp_data
                dname, dlocation = dept[did]
        
                f.write(f"{name},{eid},{salary},{did},{dname},{dlocation}\n")
                print(f"Merged: {name}, {eid}, {salary}, {did}, {dname}, {dlocation}")
            else:
                print(f"No department found for Employee {eid} (DID: {did})")

merge_e_d('employees.txt', 'departments.txt', 'Output.txt')