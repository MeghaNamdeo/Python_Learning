'''
class is a collection of 2 things : 1 data(attributes) 2.methods 
Methods are functions that belong to objects.
types : 
1. Non Static  2.Static 

'''
class Student:
    def __init__(self, fullname ):
        self.name=fullname
    def hello(self):#self ko har method me likhana ecessary h chahe 
                    #hum usko use kr rahe ho yaa nahi use kr rahe ho agar nahi likhenege to error aayga 
        print("Hello",self.name)

#creating object
s1=Student("Megha")
s1.hello()