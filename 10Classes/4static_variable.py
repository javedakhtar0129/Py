'''
1. Instance variables are those defined inside a constructor
2. Class or static variables are those defined inside class
there are two namespaces instance and class
'''


class Car:
    wheels = 4

    def __init__(self):
        self.mileage = 10
        self.brand = "BMW"


c1 = Car()
c2 = Car()
c1.mileage = 8
print("Wheels: ", Car.wheels)
Car.wheels = 3  # changing class variables

# We can use class name to call wheel because it's static/class variable
print(c1.brand, c1.mileage, Car.wheels)
print(c2.brand, c2.mileage, c2.wheels)
