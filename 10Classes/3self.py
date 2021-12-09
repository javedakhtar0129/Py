'''
1. id on object will give new value every time computer executes program
2. size of the object in memory depends on no. of variables & size of each
   variable
3. Who allocates size of object? Constructor
'''
class Computer:
    def __init__(self):
        self.name="Javed"
        self.age=20

    def update(self):
        self.age=30

    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


# creating heap memories for both objects
comp1 = Computer()
comp2 = Computer()

print("Printing address of both objects: ")
print(id(comp1))  # Id gives the reference address of object comp1
print(id(comp2))


if comp1.age == comp2.age:
    print("\nAge is Same!")



# Or we can use a user defined method to compare it
if comp1.compare(comp2):
    print("Comparing with def,Same!")
else:
    print("Comparing with def,Not Same!")


comp1.name = "BANANA"  # changing value for this object

print(comp1.name)
print(comp2.name)