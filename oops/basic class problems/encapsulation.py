# Question:

# Imagine you are designing a system to model a university. Create a class called Student that encapsulates the information about a student. The 
# Student class should have private attributes for the student's name, ID, and GPA. Provide methods to get and set each of these attributes in a 
# controlled manner. Additionally, include a method called display_info() that prints the student's information.

# Demonstrate the usage of the Student class by creating an instance of it, setting its attributes using the provided methods, and displaying 
# the student's information.

class student:
    def __init__(self,name,id,gpa):
        self.__name = name
        self.__id = id
        self.__gpa = gpa
    
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def get_gpa(self):
        return self.__gpa
    
    def set_name(self,name):
        self.__name = name

    def set_id(self,id):
        self.__id = id

    def set_gpa(self,gpa):
        self.__gpa = gpa

    def dispaly_info(self):
        print(f"Student information: Name : {self.__name} ID : {self.__id} GPA : {self.__gpa}")

students = student('Aryan',21,8.1)

students.dispaly_info()

students.set_name('rishi')
students.set_id(12)
students.set_gpa(8)

students.dispaly_info()

