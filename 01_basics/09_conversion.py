"""1. Type Conversion : automatically ho jata 
2. Type Casting : manually krna parta hai 
"""
a = 2 
b = 9.89
sum = a + b 
print(a+b)#float me automatically ho jayga 
# a = "2"
# b = 9.89

a = float("2") 
b = 9.89


print(a+b)#yaha conversion ni hora . error dega 
#isliy isko manually casting ke through convert krna hoga 

# a = float("MEGHA") # yha ni ho payga conversion error milegi
# b = 9.89

sum = a + b 
print(sum)

a = 3.14
a = str(a)# type change krne ke liy 
print(type(a))
