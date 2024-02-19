'''
Lists in Python: A build in data type that store set of values
It can store elements of difference types (integer, float , string etc.)

list are mutable 
string is immutable 
'''
marks =[90,89,78,67,56,45]
print(marks[0])
print(marks[4])
marks[3]=900
print(marks)# list is mutable hum change kr sakte hai 
print("length : ",len(marks))
print(marks[1:6])#slicing : last elemnet noyt included
print('\n')
li=[90,"megha",78.67,0]
print(li[0])
print(li[3])
print("length : ",len(li))
print(li[-3:-1])#negative slicing

# method in list 
mylist = [2,1,3]
mylist.append(4)#add one element at the end
print(mylist)
mylist.sort()#sort in ascending order
print(mylist)
mylist.sort(reverse=True)#sort in descending order
print(mylist)
mylist.reverse()#reverse the list
print(mylist)
mylist.insert(6,900)# list.insert(index, elemnt insert an element at index)
print(mylist)