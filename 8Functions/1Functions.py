# Always use meaningful names for your function
# Put two blank after defining a function as per PEP guidlines
# There is not concept of void and int,float fuctions here
def greet_user():
    print("Hi There")
    print("How ij u")


def greet_person(first,last):
    print(f"\nHello {first} {last}!")
    print(f"Hope your doing good {first} {last}")


print("Start")
greet_user()
greet_person("JAVED","Akhtar")
# Now lets see Keyboard Arguments,they are used to increase redeadbility
greet_person(last="Apple",first="Juice") # here order of argument doest matter
#Dont use positional and keyword arguments at the same time
print("Finish")

