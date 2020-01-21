# Noun: class
# Adjective: attributes
# Verb: method

# Attribute: property that further defines a class
# Method: function within a class which can access all the attributes of a class
# and perform a specific task

class Employee:

    numberOfWorkingHours = 40
    # Attributes
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6

    # Method
    def hasAchievedTarget(self):
        if self.salesMadeThisWeek >= 5:
            print("Target has been achieved")

        else:
            print("Target has not been achieved")

# Create object for class: object instantiation
employeeOne = Employee()
print(employeeOne.name)
employeeOne.hasAchievedTarget()

employeeTwo = Employee()
print(employeeTwo.name)
