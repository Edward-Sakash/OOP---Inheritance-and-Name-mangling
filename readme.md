#Exercise(OOP - Inheritance and Name mangling):
Create a parent class called Person with the following attributes:
A private attribute called __name
A private attribute called __age
The class should have the following methods:
A method called set_name that takes a parameter name
and sets the value of the private attribute __name to name.
A method called set_age that takes a parameter age
and sets the value of the private attribute __age to age.
A method called get_name that returns the value of the private attribute __name.
A method called get_age that returns the value of the private attribute __age.
Create a child class called Employee that inherits from the Person class.
The Employee class should have an additional private attribute called __salary.
The Employee class should have the following methods:
A method called set_salary that takes a parameter salary and sets
the value of the private attribute __salary to salary.
A method called get_salary that returns the value of the private attribute __salary.
A method called print_name that prints the value of the private attribute __name.

class Person:
......


class Employee(.....):
......


# Create an instance of the Employee class
employee = Employee()

# Set the name, age, and salary using the appropriate methods
employee.set_name("John Doe")
employee.set_age(30)
employee.set_salary(5000)

# Get the name, age, and salary using the appropriate methods
print("Employee Name:", employee.get_name()) #---> John Doe
print("Employee Age:", employee.get_age())  #---> 30
print("Employee Salary:", employee.get_salary())  #---> 5000
employee.print_name() #--> John Doe