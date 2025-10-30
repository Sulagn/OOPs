from student import Student
from course import Course

# Create independent students
s1 = Student("Sulagna", 101)
s2 = Student("Aarav", 102)
s3 = Student("Meera", 103)

# Create a course
python_course = Course("Object-Oriented Programming")

# Add existing students to the course
python_course.add_student(s1)
python_course.add_student(s2)

# List enrolled students
python_course.list_students()

# Remove a student
python_course.remove_student(s2)

# Show final enrollment
python_course.list_students()
