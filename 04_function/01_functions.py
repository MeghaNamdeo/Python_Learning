'''Functions in python 
Block of statement that perform a specific task]

def func_name(param1,param2):
    #some work
    return va
func_name(agr1,arg2..)#function call
'''

def Sum(a,b):
    Summision = a+b
    return Summision
print(Sum(2,4))

def Print_Hello():
    print("Hello")
Print_Hello()

#Calculate Average 
def Avg(a,b,c):
    ans = (a+b+c)/3
    return ans
print(Avg(100,89,700))

'''Type of function 
1. Bulid in function
print()
len()
type()
range()

2. User defined

Agar multiple value ko same line me print krna chahte hai to 
'''
print("Megha Namdeo",end=" " )
print("Computer Science student ")

'''output
Megha Namdeo Computer Science student
'''

''' Default Parameter : Assigning a default value to paramter , 
which is used when no argument is passed '''

# def cal_prod(a,b):
#     print(a*b)
# cal_prod(1,2) #output 1

def cal_prod(a=1,b=1):
    print(a*b)
cal_prod() #output : 1

# def cal_prod(a=1,b):
#     print(a*b)
# cal_prod(1,2) #error

# def cal_prod(a=1,b):
#     print(a*b)
# cal_prod(2) #error

# def cal_prod(a,b=2):
#     print(a*b)
# cal_prod(2) #output : 4

# def cal_prod(a=1,b):
#     print(a*b)
# cal_prod() #error

''' practice Question '''

#WAP to print the length of a list(list is the parameter )

cities = ["jabalpur","pune","Dindori","Bhopal","indore"]
movies = ["ABCD", "Spideman","KGF","Dabang"]

def print_len(list):
    print(len(list))


    
print_len(cities)
print_len(movies)

#WAP to print the in single line (list is the parameter )

def Single_line(list):
    for items in list:
        print(items, end = " ")

Single_line(cities)
Single_line(movies)

#WAF to find the factorial of n (n is the parameter )

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    fac = 1
    for i in range(1, n + 1):
        fac *= i
    return fac
result =factorial(5)
print(result)

#USD to INR 
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD= ",inr_val,"INR")
    
converter(89)

# write even / odd function

def Even_odd(n):
    if(n%2==0):
        print("Even")
    else:
        print("ODD")
        
Even_odd(4)



