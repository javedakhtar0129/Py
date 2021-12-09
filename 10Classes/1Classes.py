'''
Class contains two things, attributes(variables) and behaviour(functions)
1. Actually when we call methods from objects it is actually Class.method(object))
2. Self is the object itself and is always passed
3.
'''
class Computer:
    def config(self):
        print("This a M1 mac 2020 edition")

a = '8' #Charachter belongs to str class
b = 8
print(f"a= {type(a)}   b= {type(b)}") #This is printing the type of class these variabes are


comp1 = Computer()
print(type(comp1))

Computer.config(comp1) #This is also a method
comp1.config() # Here we are using objects to call methods