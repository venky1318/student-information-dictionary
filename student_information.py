
# Student Information Dictionary


def display_student(student_id, student):
    """Display one student's information."""
    print("\n" + "-" * 40)
    print(f"Student ID : {student_id}")
    print(f"Name       : {student['name']}")
    print(f"Age        : {student['age']}")
    print(f"Course     : {student['course']}")
    print(f"Marks      : {student['marks']}")
    print("-" * 40)


def search_student(students, student_id):
    """Search for a student using their unique ID."""
    student_id = student_id.strip()

    if student_id in students:
        display_student(student_id, students[student_id])
        return True

    print(f"No student found with ID '{student_id}'.")
    return False


def add_student(students, student_id, name, age, course, marks):
    """Add a new student after validating the details."""
    student_id = student_id.strip()
    name = name.strip()
    course = course.strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return False

    if student_id in students:
        print("This student ID already exists.")
        return False

    if not name or not course:
        print("Name and course cannot be empty.")
        return False

    if isinstance(age, bool) or not isinstance(age, int) or age <= 0:
        print("Age must be a positive integer.")
        return False

    if (
        isinstance(marks, bool)
        or not isinstance(marks, (int, float))
        or not 0 <= marks <= 100
    ):
        print("Marks must be a number between 0 and 100.")
        return False

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    print(f"Student '{name}' added successfully.")
    return True


def update_student(students, student_id):
    """Update the details of an existing student."""
    student_id = student_id.strip()

    if student_id not in students:
        print(f"No student found with ID '{student_id}'.")
        return False

    student = students[student_id]
    print("Press Enter to keep the current value.")

    name = input(f"Name [{student['name']}]: ").strip()
    age_text = input(f"Age [{student['age']}]: ").strip()
    course = input(f"Course [{student['course']}]: ").strip()
    marks_text = input(f"Marks [{student['marks']}]: ").strip()

    new_name = name if name else student["name"]
    new_course = course if course else student["course"]

    try:
        new_age = int(age_text) if age_text else student["age"]
        new_marks = float(marks_text) if marks_text else student["marks"]
    except ValueError:
        print("Age must be an integer and marks must be numeric.")
        return False

    if new_age <= 0:
        print("Age must be a positive integer.")
        return False

    if not 0 <= new_marks <= 100:
        print("Marks must be between 0 and 100.")
        return False

    students[student_id] = {
        "name": new_name,
        "age": new_age,
        "course": new_course,
        "marks": new_marks
    }

    print("Student information updated successfully.")
    return True


def display_all_students(students):
    """Display all student records."""
    if not students:
        print("No student records available.")
        return

    print("\n========== ALL STUDENTS ==========")

    for student_id, student in students.items():
        display_student(student_id, student)


def main():
    # Manually created sample dataset
    students = {
        "S101": {
            "name": "Arun",
            "age": 20,
            "course": "Python",
            "marks": 85
        },
        "S102": {
            "name": "Priya",
            "age": 21,
            "course": "Data Science",
            "marks": 91
        },
        "S103": {
            "name": "Rahul",
            "age": 19,
            "course": "Artificial Intelligence",
            "marks": 78
        }
    }

    while True:
        print("\n" + "=" * 40)
        print("    STUDENT INFORMATION SYSTEM")
        print("=" * 40)
        print("1. Search student")
        print("2. Add student")
        print("3. Update student")
        print("4. Display all students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            student_id = input("Enter student ID: ")
            search_student(students, student_id)

        elif choice == "2":
            student_id = input("Enter new student ID: ")
            name = input("Enter name: ")
            course = input("Enter course: ")

            try:
                age = int(input("Enter age: "))
                marks = float(input("Enter marks (0-100): "))

                add_student(
                    students, student_id, name, age, course, marks
                )
            except ValueError:
                print("Age must be an integer and marks must be numeric.")

        elif choice == "3":
            student_id = input("Enter student ID to update: ")
            update_student(students, student_id)

        elif choice == "4":
            display_all_students(students)

        elif choice == "5":
            print("Thank you for using Student Information System.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
