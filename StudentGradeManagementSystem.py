class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.grade = self.calculate_grade()
        self.status = self.get_status()

    def calculate_grade(self):
        avg = sum(self.scores) / len(self.scores)
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def get_status(self):
        return "Pass" if self.grade != 'F' else "Fail"

students = []

def add_student():
    name = input("Enter student name: ")
    scores = list(map(int, input("Enter scores separated by spaces: ").split()))
    student = Student(name, scores)
    students.append(student)

def display_students():
    print("\nStudent Records:")
    for s in students:
        print(f"Name: {s.name}, Grade: {s.grade}, Status: {s.status}")

while True:
    print("\n1. Add Student\n2. Show Records\n3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        display_students()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Try again.")
