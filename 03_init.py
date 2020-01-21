"""
class Employee:
    def enterEmployeeDetails(self):
        self.name = "Mark"
        
    def displayEmployeeDetails(self):
        print(self.name)


employee = Employee()
employee.displayEmployeeDetails()
# 'Employee' object has no attribute 'name'
# name not set when object created
# hence use "init" method


class Employee:
    # Initializing when object is created
    # First method to be called at the time of object creation
    # Special methods in python start and end with __
    def __init__(self):
        self.name = "Mark"
        
    def displayEmployeeDetails(self):
        print(self.name)


employee = Employee()
employee.displayEmployeeDetails()
employeeTwo = Employee()
employeeTwo.displayEmployeeDetails()
#>> Mark
"""


class Employee:
    # Initializing when object is created
    # First method to be called at the time of object creation
    # Special methods in python start and end with __
    def __init__(self, name):
        self.name = name
        
    def displayEmployeeDetails(self):
        print(self.name)

employee = Employee("Mark")
employee.displayEmployeeDetails()
employeeTwo = Employee("Matthew")
employeeTwo.displayEmployeeDetails()

