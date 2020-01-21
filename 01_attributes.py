# Class attributes: attributes that are common to all instances of the class
# Data is common to all instances of the class

class Employee:
    # Class attribute    
    numberOfWorkingHours = 40

employeeOne = Employee()
employeeTwo = Employee()
print(employeeOne.numberOfWorkingHours)
print(employeeTwo.numberOfWorkingHours)

# Changing class attribute
Employee.numberOfWorkingHours = 45

print(employeeOne.numberOfWorkingHours)
print(employeeTwo.numberOfWorkingHours)


# Instance attribute: specific to the instances of the class

employeeOne.name = 'John'
# Prints 'John'
print(employeeOne.name)

# Attribute does not exist
try:
    print(employeeTwo.name)
except AttributeError:
    print("Attribute does not exist")

# Create instance attribute numberOfWorkingHours
employeeOne.numberOfWorkingHours = 40
# Python first checks instance attributes: prints 40
print(employeeOne.numberOfWorkingHours)

# When there is no instance attribute, python checks class attribute.
# "Instance Attribute" => "Class Attribute"
# Prints 45
print(employeeTwo.numberOfWorkingHours)

