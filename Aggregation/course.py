# ---------- Course Class Definition (Aggregation Example) ----------

from student import Student

class Course:
    def __init__(self, course_name):
        # Initialize course name and empty student list
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        # Add an existing Student object (aggregation)
        self.students.append(student)
        print(f"{student.name} has been enrolled in {self.course_name}.")

    def remove_student(self, student):
        # Remove student if they exist in the list
        if student in self.students:
            self.students.remove(student)
            print(f"{student.name} has been removed from {self.course_name}.")
        else:
            print(f"{student.name} is not enrolled in this course.")

    def list_students(self):
        # Print all enrolled students
        print(f"\nStudents enrolled in {self.course_name}:")
        for student in self.students:
            print(f" - {student}")
