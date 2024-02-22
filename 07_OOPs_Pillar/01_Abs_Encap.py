'''
1.Abstraction : Hiding the implementation details of a class and only 
showing the essential features to the user .

2.Encapsulation : Wrapping data and function into a single unit (object).

3.Polymorphism
4.Inheritance




'''
#Abstraction
class Car:
    def __init__(self):
        self.acc= False
        self.brek= False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("Car Started ...")
car1=Car()
car1.start()

#