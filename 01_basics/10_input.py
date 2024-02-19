"""
input() statement is used to accept values (using keyboard) from user

input() # result for input() is always a string
int(input()) #int
float(input()) #float

"""
# name =input("Enter your name ")
# print("Welcome ",name)

# val = input("enter some values: ")
# print(type(val),val)

# ager hum input me koi bhi value dete hai 
#to humko str type hi mila hai 
# input jo function hota hai bo har value ko
# string me hi convert kr deta hai 

#ager humko integer value me type cast krna hai 

value = int(input("Enter an integer: "))
print("You entered:", value)
print(type(value))

#ager humko integer value me type cast krna hai 

value2 = float(input("Enter an float: "))
print("You entered:", value2)
print(type(value2))

name = input("Enter name : ")
age = int(input("Enter age : "))
price = float(input("Enter price : "))

print("Name : ", name)
print("Age : ", age)
print("price : ", price)
