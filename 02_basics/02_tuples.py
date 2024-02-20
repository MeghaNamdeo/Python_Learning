''' 
Tuples in Python : A built-in data tyype that lets us create immutable sequence of values.
'''
tup =(87,64,33,95,76)#tup[0],tup[1]
#  tup =(87,64,33,95,76, )this syntax is also valid
print(type(tup))

print(tup[0])
# tup[0]=44 #not allowed becaue tuole is immutable like string 
tup1=()
print(type(tup1)) #output :<class 'tuple'>
print(tup1)  #output: ()

tup2=(1,) #comma lagana necesary hai ager hum chahte h ye tuple ki tarah hi treat ho 
print(type(tup2)) #output :<class 'tuple'>
print(tup2)#output : (1,)

tup3=(1)# integer treat krta hai 
print(type(tup3)) #output :<class 'int'>
print(tup3)#output : 1

tup4=('hello')
print(type(tup4)) #output :<class 'str'>
print(tup4)#output : hello

tup5=(09.78)
print(type(tup5)) #output :<class 'float'>
print(tup5)#output : 9.78

tup6=(1,2,3)
print(type(tup6)) #output :<class 'tuple'>
print(tup6)#output : (1,2,3)



''' Slicing in Tuple : is same as list   '''

''' Tuple Methods '''
tup7 = ( 2,1,3,4 , 1, 3 ,1 ,5)
print(tup7.index(3)) #  output : 2, return index of first occurence of 3
print(tup7.count(1)) # output : 3,counts total occurence  of 1 
print(tup7)
 