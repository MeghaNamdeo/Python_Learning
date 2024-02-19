"""types of Operators 

An Operator is a symbol that performs a certain operation between  operands.

1.Arithmetic Operators(+,-,*,/,%,**)
2.Relational / Comparison Operators(==, !=, >, < ,>=,<=)
3.Assignment Operators(=, += , -=, *= , /=, %= , **=)
4.logical operators (not , and , or )
5.Membership Operator (in , not in)
6.Identity Operator (is , is not )
7.Bitwise Operator (&, | , ^)

Operator precedence 
not > and > or 
"""

a = 10
b = 5

print ( a+b)
print ( a-b)
print ( a/b)# integer value aani chahiy lekin floating value aati hai 
print ( a*b)
print ( a**b)# power
print ( a%b) #remainder

#relational operator 
a = 50 
b = 209 
print (a==b) #output : false

print(a!=b) #output: true
print(a>=b)#output : false

#assignment operator 
num = 10 
num  = num + 10
#or
num += 10
print (" num : ", num)

#logical operator 
print (not False) # output : True
print(not(a>b))#output : True

val1 =True 
val2=True
print("And operator : ", val1 and val2) # True
print("And operator : ", val1 or val2)#True