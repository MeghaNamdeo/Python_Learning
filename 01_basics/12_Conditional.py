'''
if - elif - else (SYNTAX)

if(condition):
    Statement1
elif(condition):
    Statement2
else :
    StatementN

    
age = 12
if(age >= 18):
    print("vote")
elif(age<18):
    print("Not Vote ")
else:
    print("wait For Sometimes")

light = input (" Enter color : ")
if(light == "red"):
    print("stop")
elif (light == "green"):
    print("go")
elif(light == "yellow" ):
    print("look")
elif(light == "white" or light =="blue"):
    print("Light is broken")
else:
    print("Invalid Color")
    '''

''' Single Line if / ternary operator 
<var> = <val1> if<condition> else <val2>

food = input("food : ")
eat = " yes "if food == "cake" else "no"
print(eat)

#<stt1> if <condition> else <stt2>

food = input(" food : ")
print("sweet")if food == "cake" or food=="jalebi"else print("not sweet")

'''
# clever if / Ternary Operator
#<var> = (false_val, true_val)[<condition>]
age = int(input("age: "))
vote = ("no", "yes")[age < 18]

salary = float(input("salary: "))
tax_rates = {True: 0.1, False: 0.2}
tax = salary * tax_rates[salary <= 50000]

print("Vote:", vote)
print("Tax:", tax)
