#del keyword 
''' used to delete properties or object itself .
del s1.name
del s1
'''

class Student:
    def __init__(self,name):
        self.name=name
        
s1 = Student("Megha")
print(s1.name)
del s1.name
print(s1.name) #error : name was not define in student 

'''Private (like ) attributes and methods 
Conceptual Implementations in Python 
Private attribute and methods are meant to be used only 
within this class and are not 
accessible from outside the class

kisi bhi element ko private krne ke liy um uske aage 2 underscore lga dete hai 
'''
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass=acc_pass
acc1=Account("12345","abcde")
print(acc1.acc_no)
print(acc1.__acc_pass) # error : Account object has no attribute '__acc_pass'

# agr hum attribute yaa meth ke samne 2 times underscore __ lga de to bo private ho jati h 
# class Person:
#     __name="megha"

#     def __hello():
#         print("Hello person!")
# p1=Person()
# print(p1.__name)#error
# print(p1.__hello())#error
# p1.__hello()#error

class Person:
    __name = "Megha"

    def __hello(self):
        print("Hello person!")

    def welcome(self):
        self.__hello()

p1 = Person()
p1.welcome()  # This will call the welcome method which internally calls the __hello method
'''ye humko error ni dega hello function 
call ho jayaga kyu b hum __ lgakr private banate h class ke ander ke function access kr
skte hai but outside class access nahi kr sakte '''