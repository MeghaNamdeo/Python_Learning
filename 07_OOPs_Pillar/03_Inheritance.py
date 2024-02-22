#inheritance 
'''
When one class(child / derived )derives thr properties and methods of another (parent/base )class.

class Car:
    ...
class ToyotoCar(Car):
    ....

'''

#types : 
'''
1. Single inheritance 
2. Multiple inheritance 
3. Multi-level inheritance 

'''

#Single inheritance 
class Car:
    color = "black"

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")

car1.start()
print(car1.name)
car1.stop()
print(car1.color)

''' output 
Car started...
Fortuner
Car stopped.
black
'''


#multi-level inheritance 
class Car:
    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped.")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type
car1=Fortuner("deisel")
car1.start()


#mutiple inheritance 

class A:
    varA="welcom to class A"
class B:
    varB="welcom to class B"
class C(A,B):
    varC="welcom to class C"
c1=C()

print(c1.varA)
print(c1.varB)
print(c1.varC)