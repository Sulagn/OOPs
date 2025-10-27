# ---------- Employee Management System: Inheritance Demonstration ----------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: ₹{self.salary}")

    def get_role(self):
        return "Employee"


# Child class 1: Manager
class Manager(Employee):
    def __init__(self, name, salary, department):
        # Inherit from Employee
        super().__init__(name, salary) #Calls parent class methods
        self.department = department

    def show_details(self):
        print(f"Manager: {self.name}, Salary: ₹{self.salary}, Department: {self.department}") #Overriding (Child changes parent method)

    def get_role(self): #Polymorphism (Same method behaves differently)
        return "Manager"


# Child class 2: Developer
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def show_details(self):
        print(f"Developer: {self.name}, Salary: ₹{self.salary}, Language: {self.programming_language}")

    def get_role(self):
        return "Developer"


# ---------- Try It Out Section ----------

# Create objects
emp1 = Employee("Yashashee", 40000)
mgr1 = Manager("Akankshya", 70000, "HR")
dev1 = Developer("Sulagna", 60000, "Python")

# Show details
emp1.show_details()
mgr1.show_details()
dev1.show_details()

# Check polymorphism
print("\nRoles:")
for emp in [emp1, mgr1, dev1]:
    print(f"{emp.name} is a {emp.get_role()}")
