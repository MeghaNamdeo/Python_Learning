# WAF that replace all occurrences of "java " with "python"in above file.
with open("practice.txt","w") as f:
    f.write("Hi everyone\n we are learning I/O\n")
    f.write("using Java.\nI like programming in Java.")

data.replace('Java',"Python")
print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

    #Search "learning" exite or not in file 

def check_for_word():
    word = "xlearning"
    with open("practice.txt","r") as f:
      data=f.read()
      if(data.find(word)1=-1):
        print("Found")
      else:
        print("not found")

check_for_word()
