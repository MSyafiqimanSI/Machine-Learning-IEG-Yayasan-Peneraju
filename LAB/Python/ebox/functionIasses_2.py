def multiVarFunc():
    department_name = input("Enter department name:\n")
    total_students = int(input("Enter the number of total students:\n"))
    total_faculty = int(input("Enter the number of total faculties:\n"))
    
    return department_name, total_students, total_faculty

dept, students, faculty = multiVarFunc()

print("Details:")
print(f"Department: {dept}")
print(f"Total students: {students}")
print(f"Total faculties: {faculty}")
