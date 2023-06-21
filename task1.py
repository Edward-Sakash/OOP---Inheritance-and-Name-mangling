class Person:
    def __init__(self):
        self.__name = None
        self.__age = None

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age


class Employee(Person):
    def __init__(self):
        super().__init__()
        self.__salary = None

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def print_name(self):
        print("Employee Name:", self.get_name())

# Create an instance of the Employee class
employee = Employee()

# Set the name, age, and salary using the appropriate methods
employee.set_name("John Doe")
employee.set_age(30)
employee.set_salary(5000)

# Get the name, age, and salary using the appropriate methods
print("Employee Name:", employee.get_name())  # John Doe
print("Employee Age:", employee.get_age())  # 30
print("Employee Salary:", employee.get_salary())  # 5000

# Call the print_name method
employee.print_name()  # Employee Name: John Doe
