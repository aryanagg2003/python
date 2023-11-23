# Question:

# Create a Python class called University to model a university. Inside the University class, define an inner class called Department. The Department
#  class should have attributes such as name and head_of_department.

# Additionally, implement a method in the University class called add_department that allows adding instances of the Department class to the 
# university.

# Demonstrate the usage of your classes by creating an instance of the University class, adding a few departments, and displaying information about 
# the university and its departments.

class University:
    def __init__(self,name):
        self.name = name
        self.departments = []

    def add_departments(self,name,department_name):
        department = self.Department(name,department_name)
        self.departments.append(department)

    class Department:
        def __init__(self,name,head_of_department):
            self.name = name
            self.head_of_department = head_of_department

university = University("Example University")

university.add_departments("Computer Science", "Dr. Smith")
university.add_departments("Physics", "Prof. Johnson")
university.add_departments("History", "Dr. Davis")

# Displaying information
print(f"University Name: {university.name}")

for department in university.departments:
    print(f"Department: {department.name}, Head: {department.head_of_department}")