'''
Create student class that takes name and marks of 3 subjects as arguments in constructor.
Then create a method to print the average 
'''
#these are all non static method 
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks

    def get_avg(self):
        sum= 0 
        for val in self.marks:
            sum+=val
        print("hello ",self.name,"your avg score is : ",sum/3)

s1=Student("Megha",[90,99,98])
s1.get_avg()
print(s1.name,s1.marks)

s1.name = "Vijay Namdeo"
print(s1.name,s1.marks)

