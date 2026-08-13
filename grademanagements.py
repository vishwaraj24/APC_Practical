students = []
grades = []

def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))

    students.append(name)
    grades.append(grade)

    print("Student added successfully!")

def update_grade():
    name = input("Enter student name: ")

    if name in students:
        index = students.index(name)
        new_grade = float(input("Enter new grade: "))
        grades[index] = new_grade
        print("Grade updated successfully!")
    else:
        print("Student not found!")

def remove_student():
    name = input("Enter student name: ")

    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
        print("Student removed successfully!")
    else:
        print("Student not found!")

def calculate_average():
    if len(grades) == 0:
        print("No students available!")
    else:
        average = sum(grades) / len(grades)
        print("Average grade:", average)

def display_extreme():
    if len(grades) == 0:
        print("No students available!")
    else:
        print("Highest grade:", max(grades))
        print("Lowest grade:", min(grades))

while True:
    print("\n----- Student Grade Management System -----")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average")
    print("5. Display Highest and Lowest Grade")
    print("6. Display All Students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        update_grade()

    elif choice == 3:
        remove_student()

    elif choice == 4:
        calculate_average()

    elif choice == 5:
        display_extreme()

    elif choice == 6:
        for i in range(len(students)):
            print(students[i], ":", grades[i])

    elif choice == 7:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")