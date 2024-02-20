'''
Set is the collection of the unordered items.
Each elemnt in the set must be unique and immutable
we can store boolean , int , float, str, tuple  in set  because it is immutable
we cannot store list and dictornies in set because it is mutable 

sets --> mutable
set-->element-->immutable
'''

num={1,2,3,4,5}
print(num)
set2={1,2,2,2,2}
#repeated element stored only once, so it resolved to {1,2}
print(set2)

collection = {} # this is a syntax of empty dictornies that why for empty set we write null_Set=set()

null_Set=set()#empty set syntax
print(null_Set)

''' output 
{1, 2, 3, 4, 5}
{1, 2}
set()
'''

#Set Methods
'''
1.set.add(Element )#adds an Element
2.set.remove(element )#removes the Element
3.set.clear()#empties the set
4.set.pop()#removes a random value 
5.set.union(Set2)#combines both set values and returns new
6.set.intersection(Set2)#combine common values and returns new 

'''
collection=set()
collection.add(1)#adds an element 
collection.add(2)
collection.add(3)
collection.add(2)

print(collection)
collection.remove(1)# remove element 
print(collection) 
collection.pop()#removes a random value
print(collection) 
collection.clear()#empties the set
print(collection) #output : empty set 

set1 = { 1, 2, 3 ,4 ,5 }
set2={1,0,6,8,3,2}
print(set1.union(set2))
print(set1.intersection(set2))

#unhashable means jiski value change ho jay jese lists, set 

#practice question 
'''
You are given a list of subjects for students. Assume one classroom is required
for subject. How many classrooms are needed by all students 
'''
classroom={"python","cpp","python","js","C","java","python","java"}
print(classroom)
print(len(classroom))