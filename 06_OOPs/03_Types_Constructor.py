'''
1.Default 
2. Parameterized 
'''

class Student:

    # Default constructor
    def __init__(self):
        pass

    # Parameterized constructor
    def __init__(self, name, RollNo):
        self.name = name
        self.RollNo = RollNo
        print("Adding new student to the database...")

# Creating object
s1 = Student("Megha", 97)
print(s1.name, s1.RollNo)

