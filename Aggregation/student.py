# ---------- Student Class Definition ----------

class Student:
    def __init__(self, name, student_id):
        # Initialize name and ID
        self.name = name
        self.student_id = student_id

    def __str__(self):
        # String representation for printing
        return f"{self.name} (ID: {self.student_id})"
