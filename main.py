students = []

print("Welcome to Student Management System")

name = input("Enter Student Name: ")
student_id = input("Enter Student ID: ")
department = input("Enter Department: ")
gpa = float(input("Enter GPA: "))

student = {
    "Name": name,
    "ID": student_id,
    "Department": department,
    "GPA": gpa
}

students.append(student)
print("Student added successfully!")
print("\nStudent Information:")
print(student)
