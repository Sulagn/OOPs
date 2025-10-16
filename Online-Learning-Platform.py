from abc import ABC, abstractmethod

# ------------------------------
# 1. Abstraction & Inheritance
# ------------------------------
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def show_profile(self):
        print(f"Name: {self.name}, Email: {self.email}")


class Student(User):
    total_students = 0  # Class variable

    def __init__(self, name, email):
        super().__init__(name, email)
        self.__password = None  # Encapsulation
        self.courses = []  # Aggregation
        Student.increment_student_count()

    def enroll_course(self, course):
        self.courses.append(course)
        course.add_student(self)

    def set_password(self, pwd):
        self.__password = pwd

    def get_password(self):
        return "Access Denied!"

    @classmethod
    def increment_student_count(cls):
        cls.total_students += 1

    @staticmethod
    def validate_email(email):
        return "@" in email

    def show_profile(self):  # Polymorphism
        print(f"Student Name: {self.name}, Courses Enrolled: {len(self.courses)}")


class Instructor(User):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.__salary = salary  # Encapsulation
        self.courses_created = []

    def create_course(self, title):
        course = Course(title, self)
        self.courses_created.append(course)
        return course

    def get_salary(self):
        return "Access Denied!"

    def show_profile(self):  # Polymorphism
        print(f"Instructor Name: {self.name}, Courses Created: {len(self.courses_created)}")


# ------------------------------
# 2. Abstraction for Course Content
# ------------------------------
class CourseContent(ABC):
    @abstractmethod
    def display_content(self):
        pass


class Video(CourseContent):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def display_content(self):
        print(f"Playing Video: {self.title}, Duration: {self.duration} mins")


class Quiz(CourseContent):
    def __init__(self, title, num_questions):
        self.title = title
        self.num_questions = num_questions

    def display_content(self):
        print(f"Starting Quiz: {self.title}, Questions: {self.num_questions}")


# ------------------------------
# 3. Composition & Operator Overloading
# ------------------------------
class Course:
    def __init__(self, title, instructor):
        self.title = title
        self.instructor = instructor
        self.contents = []  # Composition: list of CourseContent
        self.students = []  # Aggregation

    def add_content(self, content):
        self.contents.append(content)

    def add_student(self, student):
        self.students.append(student)

    def __len__(self):  # Operator overloading
        return len(self.students)

    def __add__(self, other):  # Combine courses into a bundle
        return CourseBundle([self, other])

    def show_course_details(self):
        print(f"Course: {self.title}, Instructor: {self.instructor.name}")
        print(f"Students Enrolled: {len(self.students)}")
        for content in self.contents:
            content.display_content()


class CourseBundle:
    def __init__(self, courses):
        self.courses = courses

    def show_bundle(self):
        print("Course Bundle Includes:")
        for course in self.courses:
            print(f"- {course.title}")


# ------------------------------
# 4. Platform (Aggregation)
# ------------------------------
class Platform:
    def __init__(self, name):
        self.name = name
        self.students = []  # Aggregation
        self.instructors = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_instructor(self, instructor):
        self.instructors.append(instructor)

    def add_course(self, course):
        self.courses.append(course)

    def show_all_courses(self):
        print(f"Platform: {self.name} Courses:")
        for course in self.courses:
            course.show_course_details()


# ------------------------------
# 5. Testing the Starter Skeleton
# ------------------------------
if __name__ == "__main__":
    # Instructors
    instr = Instructor("John Doe", "john@example.com", 5000)
    course1 = instr.create_course("Python OOP")
    course2 = instr.create_course("Data Science Basics")

    # Course contents
    course1.add_content(Video("OOP Concepts", 30))
    course1.add_content(Quiz("OOP Quiz", 10))

    # Students
    stud1 = Student("Sulagna", "sulagna@example.com")
    stud1.enroll_course(course1)

    stud2 = Student("Ravi", "ravi@example.com")
    stud2.enroll_course(course2)

    # Platform
    platform = Platform("EduPlatform")
    platform.add_student(stud1)
    platform.add_student(stud2)
    platform.add_instructor(instr)
    platform.add_course(course1)
    platform.add_course(course2)

    # Display
    platform.show_all_courses()
    print(f"Total Students: {Student.total_students}")

    # Operator Overloading Example
    bundle = course1 + course2
    bundle.show_bundle()
