"""
Inner class is a class inside a class

We make object of Inner class using name of Outer class like in JAVA
"""


class Student:  # outer class

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop()

    def show(self):
        print(f"Name: {self.name} || Roll no: {self.roll_no}")
        self.lap.show_laptop()  # Printing innerclass's method here

    class Laptop:  # inner class
        def __init__(self):
            self.brand = "APPLE"
            self.cpu = "M1"
            self.ram = "8GB"

        def show_laptop(self):
            print(f"Brand: {self.brand} cpu: {self.cpu} ram: {self.ram} ")


s1 = Student("JAVED AKHAR", 21)
s2 = Student("Navin", 33)

s1.show()
s2.show()

print()
lap1 = Student.Laptop()
lap2 = Student.Laptop()

lap1.show_laptop()
lap1.ram = "RAM ka value changed"
lap1.show_laptop()
