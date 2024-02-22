'''
Polymorphism : Operator Overloading 

when the same operator is allowed to have different meaning according to the context.

Operator & Dunder Functions
a+b #addition                   a.__add__(b)
a-b #subtraction                a.__sub__(b)
a*b #multiplication             a.__mul__(b)
a/b #division                   a.__truediv____(b                   
a#b #modulos                    a.__mod____(b)                

'''     
#implicit overloading jo python ne already kr chuki hai 
print(1+2)#addition
print("megha"+" namdeo")#concatenate
print([1,2,3]+[9,8,7])#merge

'''in all three '+' meaning is difference this is a example of operator overloading '''
'''
Complex Number 
 1i + 3j
+2i + 5j
----------
 3i + 8j

 '''
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNum(self):
        print(self.real, "i + ", self.img, "j")

    def __add__(self, n2):
        newReal = self.real + n2.real
        newImg = self.img + n2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNum()

num2 = Complex(4, 6)
num2.showNum()

result = num1 + num2
result.showNum()


# result = num1.add(num2)
# result.showNum()

''''
output : 
1i + 3j
4i + 6j
5i + 9j

'''