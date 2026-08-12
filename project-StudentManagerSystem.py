class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks

    def display(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print()


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID")
            return

        for student in self.students:
            if student.student_id == student_id:
                print("Student ID already exists")
                return

        name = input("Enter Name: ").strip()
        if not name:
            print("Name cannot be empty")
            return

        try:
            marks = int(input("Enter Marks: "))
        except ValueError:
            print("Invalid marks")
            return

        if not (0 <= marks <= 100):
            print("Marks should be between 0 and 100")
            return

        student = Student(student_id, name, marks)
        self.students.append(student)
        print("Student added successfully")

    def display_students(self):
        if not self.students:
            print("No students available")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID")
            return

        for student in self.students:
            if student.student_id == student_id:
                print("Student Found")
                student.display()
                return

        print("Student not found")

    def update_marks(self):
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID")
            return

        for student in self.students:
            if student.student_id == student_id:
                try:
                    new_marks = int(input("Enter New Marks: "))
                except ValueError:
                    print("Invalid marks")
                    return

                if not (0 <= new_marks <= 100):
                    print("Marks should be between 0 and 100")
                    return

                student.marks = new_marks
                print("Marks updated successfully")
                return

        print("Student not found")

    def delete_student(self):
        try:
            student_id = int(input("Enter Student ID: "))
        except ValueError:
            print("Invalid ID")
            return

        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Student deleted successfully")
                return

        print("Student not found")

    def find_topper(self):
        if not self.students:
            print("No students available")
            return

        topper = self.students[0]
        for student in self.students:
            if student.marks > topper.marks:
                topper = student

        print("Topper Details")
        topper.display()


def main():
    manager = StudentManager()

    while True:
        print("\nStudent Menu")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Update Marks")
        print("5. Delete Student")
        print("6. Find Topper")
        print("7. Exit")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input")
            continue

        match choice:
            case 1:
                manager.add_student()
            case 2:
                manager.display_students()
            case 3:
                manager.search_student()
            case 4:
                manager.update_marks()
            case 5:
                manager.delete_student()
            case 6:
                manager.find_topper()
            case 7:
                print("Program exited")
                break
            case _:
                print("Invalid choice")


if __name__ == "__main__":
    main()