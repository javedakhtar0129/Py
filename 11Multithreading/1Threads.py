'''
By default we have only one thread
Multithreading is basically running processes multiply
1.To make Threads we pass Threads in 'class Name(Thread):'
2.Thread class has an inbuilt method call run and it will only work objects call start method
3.To make threads synchronous we use sleep() method
4.Join method is telling main to let the thread complete itself and join
'''
from threading import *
from time import sleep


class Hello(Thread):
#T is capital because conventionally we use capitals when dealing with class
    def run(self):
        for i in range(5):
            print("Hello!!")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi!!")
            sleep(1)


t1 = Hello()
t2 = Hi()

# t1.run()
# t2.run()
print("\n")
# Threads can only be initiated with start method
t1.start()
t2.start()

t1.join() # Telling main to complete itself
t2.join()

print("\nBye!")