'''
Static Methods  are the methods that donot use the self paramenter (work at class level)

'''

'''
decorator : decorator allows us to wrap another  function in order to 
extend the behavior of the wrapped function, without permanenetly modifying it.
'''
class Student :
    #this convert a funcion into staic function 
    @staticmethod #decorator
    def college():
        print("Global College")
Student.college()

