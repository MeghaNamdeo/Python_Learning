''' Slicing is accesing part of a string

str[starting_idx : ending_idx] ending idx is not included

'''

str  = "Megha Namdeo"


print(str[1:4]) # output : egh

#str[:4] is same as str[0:4]
print(str[:4])# output: Megh
#str[1:] is same as str[1:len(str)]
print(str[1:])#output : egha Namdeo


'''Negative Index
A  p  p  l  e 
-5 -4 -3 -2 -1 

str = "Apple"
str[-3:-1]is "pl"
'''

str = "Apple"
print(str[-3:-1])#output : pl, last bala include in hota 
