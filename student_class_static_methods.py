# ---------- Class and Static Methods Demonstration ----------
# Concept: @classmethod and @staticmethod
# Purpose: To show the difference between instance methods, class methods, and static methods


class Student:
    # Class variable (shared by all objects of this class)
    next_id = 1

    # Constructor (instance method) - initializes individual student data
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.id = Student.next_id  # Assign the current value of next_id as ID
        Student.next_id += 1       # Increment the class variable for the next student

    # Instance method - works on individual objects
    def __str__(self):
        return f"Student: {self.name} (ID: {self.id})"

    # Class method - works on the class as a whole (not a single object)
    @classmethod
    def total_students(cls):
        return f"Total students created: {cls.next_id - 1}"

    # Static method - independent of both object and class, just a helper function
    @staticmethod
    def validate_email(email):
        return "@" in email and email.endswith(".com")


# ---------- Testing Section ----------
# Creating student objects
s1 = Student("Sulagna", "sulagna@example.com")
s2 = Student("Ariana", "ariana@example.com")

# Printing each student's data
print(s1)
print(s2)

# Calling class method using the class name
print(Student.total_students())

# Using static method for validation
print("Is 'hello@gmail.com' valid?", Student.validate_email("hello@gmail.com"))
print("Is 'notanemail' valid?", Student.validate_email("notanemail"))
