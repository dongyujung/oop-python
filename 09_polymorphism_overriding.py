# Polymorphism
# "+" operator adds two numbers but also concatenates strings
# same operator but operates differently for different types of objects

# Polymorphic properties of overriding

# Derived class can change how the method works by redifining in the derived class


class Employee:
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 40
        
    def displayNumberOfWorkingHours(self):
        print(self.numberOfWorkingHours)


class Trainee(Employee):
    def setNumberOfWorkingHours(self):
        self.numberOfWorkingHours = 45
        
    # If you want to call the base class method: use super()
    def resetNumberOfWorkingHours(self):
        super().setNumberOfWorkingHours()


employee = Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours of employee: ", end = ' ')  # space instead of line change
employee.displayNumberOfWorkingHours()
trainee = Trainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of trainee: ", end = ' ') 
trainee.displayNumberOfWorkingHours()
# Call the base class method
trainee.resetNumberOfWorkingHours()
print("Number of working hours of trainee: ", end = ' ') 
trainee.displayNumberOfWorkingHours()





