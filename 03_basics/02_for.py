'''
for loop are used for sequential traversal . for traversing list , string , tuples etc .

for loops

for el in list:
    #some work

for loop with else 

for el in list:
    #some work
else:
    #work when loop ends

'''
#practice question : print the elemnts of the following list using a loop
li = [1,4,16,25,36,49,64,81,100]

for el in li:
    print(el)

for el in li:
    print(el)
else:
    print("End")

# practice question : search for a number x in this tuple using loop
x = int(input("Enter value of x here : "))
for el in li:
    if(el == x):
        print(el)
    else:
        print("Not found ")

        
