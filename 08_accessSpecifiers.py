# Public => memberName
# Protected => _memberName
# Private => __memberName


class Car:
    numberOfWheels = 4
    # Protected attribute is also accessible outside of classes
    # Only a naming convention
    _color = "Black"
    #Private attribute
    __yearOfManufacture = 2017  # Stored as _Car__yearOfManufacture


class Bmw(Car):
    def __init__(self):
        print("Protected attribute color: ", self._color)


car = Car()
print("Public attribute numberOfWheels: ", car.numberOfWheels)
bmw = Bmw()

print("Private attribute yearOfManufacture: ", car._Car__yearOfManufacture)
# Private attribute not accessible outside of class
print("Private attribute yearOfManufacture: ", car.__yearOfManufacture)
