#dictionaries are used to store data values in key:value pairs
'''
keys ko repeat nii krte 
dictionaries mutable hoti hai 

They are unordered , mutable (changeable)& dont allow duplicate keys
'''
dic={
    "name":"Megha",
    "cgpa":9.21,
    "marks":[98,97,95],
}
print(dic)
print(dic["name"])
print(dic["cgpa"])
print(dic["marks"])
dic["name"]="Megha Namdeo"#changeable
dic["surname"]="Namdeo"#add new key value
print(dic)
#key me list ko nahi le akte , hum integer , float, tuple, string , boolean ho sakta 
info={
    "key":"value",#string
    "subject":["maths","physics","chemistry"],#list
    "interest":("badminton","bolyball","ludo"),#tuple
    "name":"global college",
    "learning":"coding",
    "age":25,# integer
    "is_adult":True,#boolean
    "cgpa":9.21,#float
}
print(info)
print(info["subject"])
print(info["cgpa"])
print(info["interest"])

#empty dictionaries
null_dic={}

print(null_dic)
null_dic["name"]="global"
print(null_dic)

#nested dictionaries
student={
    "name":"megha namdeo",
    "subjects":{
        "phy":90,
        "math":100,
        "che":99,
        
    }
}
print(student)