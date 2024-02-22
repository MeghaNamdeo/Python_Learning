'''
Types of method :

1. class methods(cls as a argument hota h 
2.static method  (jo cls yaa instance dono me se kissi ke bhi atrribute ko access nahi krte )
3. normal methods or instance method (self as a argument hhota hai )

class methods

A class method is bound to the class & receive the class as an implicit first argument.
Note - static method canot access or modify class state and generally for utility.

'''
class Student:
    @classmethod#decorator
    def college(cls):
        pass
    
class Person:
    name="megha"
    def changename(self,name):
        self.name=name 
p1=Person()
p1.changename("megha namdeo")
print(p1.name)#output :megha namdeo
print(Person.name)#output :megha  
'''yha new object create hora h uska name megha namdeo hai same class me changes nahi hore h 
'''

class Person:
    name="Sahil"
    def changeName(self,name):
        self.__class__.name="Aahaan"
        # __class__ se hum ye class me change kr sakte hai 
p1=Person()
p1.changeName("Raja")
print(p1.name)#output : Aahaan
print(Person.name)#output : Aahaan

#**************************Another way *******************

class Person:
    name="Ramila"
    @classmethod
    def changeName(cls,name):#directly class me change hua 
        cls.name=name
         
p1=Person()
p1.changeName("Raja")  
print(p1.name)#output : Raja
print(Person.name)#output : Raja




     #property decorator : we use @property decorator on any method in the class to use the methhod as a property



class Student:
    def __init__(self, phy, chem, math):
        self._phy = phy
        self._chem = chem
        self._math = math

    @property
    def percentage(self):
        return str((self._phy + self._chem + self._math) / 3) + "%"

s1 = Student(90, 89, 70)
print(s1.percentage)

s1._phy = 86
print(s1.percentage)

