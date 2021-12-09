'''
We will look at getters and setters over here
1. To access class variables we need class definition
2. We pass cls in class methods like we used to pass self in instance methods

There are also static methods we use them when we have nothing to do with
class variables or instance variables
'''


class Student:
    school = "AKHTAR"  # This is a class variable

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3) / 3

    def get_m1(self):  # getter
        return self.m1

    def set_m1(self, value):  # setters or Mutators
        self.m1 = value

    # Below is a class method
    @classmethod  # This is called a decorator
    def get_schoolName(cls):
        return cls.school + " (CLASS METHOD)"

    @staticmethod
    def info():
        print("(STATIC METHOD)This is school Class")




s1 = Student(14, 345, 56)
s2 = Student(32, 234, 64)

# Below are instance methods
print(s1.average())
print(s2.average())
# Below are class methods
print(s1.get_schoolName())
# Below are static methods
Student.info()

