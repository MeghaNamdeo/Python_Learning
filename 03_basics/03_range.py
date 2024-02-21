
'''
Range functions returns a sequence of numbers, starting from 0
 by default , and increment by 1 (by default), and scope before
  a specified number .\

range (start?,stop,step?)

'''
for el in range(5):#end
    print(el)
for el in range(1,5):#start,end
    print(el)
for el in range(1,5,2):#start,end,increment
    print(el)

# Practice question: WAP to find the sum of the first n numbers using while

i = 1
n = int(input("Enter the value of n: "))
Sum = 0

while i < n:
    Sum = Sum + i
    i = i + 1

print("Sum of the first", n, "numbers:", Sum)

#practice question : print number from 1 to 100

for i in range(1,101,1):
    print(i)
    #practice question : print number from 100 to 1

for i in range(100,0, -1):
    print(i)
    
#practice question : print multiplication table of a number n 
n = int (input("Enter value of n here : "))
for i in range(1,11):
    print(n,'*',i,"=",n*i)