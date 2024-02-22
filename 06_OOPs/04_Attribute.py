'''
Class & intance attributes
 class attributes are class variables that are inherited by every object of a class.
  The value of class attributes remain the same for every new object.

  instance attributes, which are defined in the __init__() function, are class variables
   that allow us to define different values for each object of a class.

1.Class attritbute (Class.attr)
2.object attribute (obj.attr)
'''
class Student:
    college_name = "Global College"
    name = "anonymous"  # class attribute

    def __init__(self, name, marks):
        self.name = name  # object attribute, overrides class attribute
        self.marks = marks
        print("Adding new student to the database...")

s1 = Student("Megha", 97)
print(s1.name)
