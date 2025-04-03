# Dictionary to store student grades
student_grades = {}

while True:
    print("\nOptions:")
    print("1. Add a new student")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        student_grades[name] = grade
        print(f"Student {name} added with grade {grade}.")
        
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in student_grades:
            new_grade = input("Enter new grade: ")
            student_grades[name] = new_grade
            print(f"Grade updated for {name}.")
        else:
            print("Student not found!")

    elif choice == "3":
        print("\nStudent Grades:")
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")

    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please select a valid option.")
