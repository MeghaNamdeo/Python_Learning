''' break : used to terminate the loop when encountered.

'''
li = [1,4,16,25,36,49,64,81,100]
x = 4
for el in li:
    if(el == x):
        print(el)
        break
    else:
        print("Not found ")