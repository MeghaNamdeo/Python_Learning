# __init__ Function
# Constructor
# All classes have a function called __init__(), which is always executed when the object is being initiated

# creating class
class Student:
       def __init__(self, fullname):
        print("Adding new student to the database...")
        self.name = fullname
        #attribute
# creating object
s1 = Student("Megha")
print(s1.name)

# creating object
s2 = Student("Pratibha")
print(s2.name)
       
'''The self parameter is a reference to the current instance of the class,
and is used to access variables that belong to the class.
'''

class Student:
       def __init__(self, fullname, RollNo):
        self.name = fullname
        self.RollNo=RollNo
        print("Adding new student to the database...")
        
        #attribute
# creating object
s1 = Student("Megha",97)
print(s1.name,s1.RollNo)

# creating object
s2 = Student("Pratibha",98)
print(s2.name,s2.RollNo)
       
