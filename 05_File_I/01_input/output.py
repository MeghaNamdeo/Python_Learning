'''
File I/O in Python
Python can be used to perform operations on a file .(read and write data)

Type of all files 
1.Text files : .txt,.docx,.log etc.
2.Binary Files:mp4,.mov,.png,.jpeg etc.

Open , read and close File

We have to open a file before reading or writing .
f = open ("file_name","mode")

sample.txt              w : write mode 
demo.docx               r : read mode 

data = f.read() # reads entire file
data = f.reading()#reads one line at a time

f.close()
                
'''

f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

'''
'r' --> open for reading(Defult)
'w' --> open for writing truncating the file first
'x' --> create a new file and open it for writing
'a' --> open for writing , appending to the end of the file if it exists
'b' --> binary mode
't' --> text mode (default)
'+' --> open a disk file for updating (reading and writing)

'''

'''
Writing to a file 
f=open("demo.txt","w")
f.write("this is a new line ")#overwrite the entire file

f= open("demo.txt","a")
f.write("this is a new line")#adds to the file
'''

'''
with syntax
with open("demo.txt","a")as f:
    data=f.read()
    '''

'''
    Deleting a File
    using the os module 
    Module (like a code library ) is a file written by another programmer that generally has 
    a function we can use.

    import os
    os.remove (filename)
'''
