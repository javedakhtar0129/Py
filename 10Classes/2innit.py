'''
1. _init_ class is basically a constructor of a class
'''
class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram= ram


    def configuration(self):
        print("Configuration is: ",self.cpu,self.ram)


comp1=Computer("i5","8 GB")
comp2=Computer("Apple M1","8 GB")

comp1.configuration()
comp2.configuration()