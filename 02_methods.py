class Employee():
    
    # Class method
    # Input "self" by convention
    def employeeDetails(self):
        self.name = "Ben"
    
    # Static Method: does not take self as argument
    # Ignore binding to object
    @staticmethod
    def welcomeMessage():
        print("Welcome to our organization!")
        
        
employee = Employee()
employee.employeeDetails()
print("employee.name: ", employee.name)

# This will not work without @staticmethod
# since employee.welcomeMessage() is interpreted as Employee.welcomeMessage(employee)
# and welcomeMessage() does not take any arguments.
# myobject.method(arg1, arg2) as MyClass.method(myobject, arg1, arg2)
employee.welcomeMessage()