#---DICTIONARY---


#1. create dictionary using{}:                                  #Output: {1: 'python', 2: 'java', 3: 'c++'}

dict1={1: "python", 2: "java", 3: "c++"}
print(dict1)


#2. create dictionary using dict() constructor:                 #Output: {'a': 'python', 'b': 'java', 'c': 'c++'}

dict2=dict(a= "python", b= "java", c= "c++")
print(dict2)


#3. accessing dictionary items:                                 

dict1={"name": "arun",
       1: "python",
       (1,2): [1,2,4]}
#using key:                                                     #Output: arun
print(dict1["name"])

#using get():                                                   #Output: arun
print(dict1.get("name"))


#4. adding dictionary items:                                    #Output: {'name': 'arun', 'course': 'java', 'roll no': 1001, 'age': 25}

dict1={"name": "arun",
       "course": "java",
       "roll no": 1001}
dict1["age"]=25
print(dict1)


#5. updating an existing value:                                 #Output: {'name': 'arun', 'course': 'python', 'roll no': 1001}

dict1={"name": "arun",
       "course": "java",
       "roll no": 1001}
dict1["course"]="python"
print(dict1)


#6. removing dictionary items:                                  
# using del to remove an item                                   #Output: {'name': 'arun', 'course': 'java', 'roll no': 1001}

dict1={"name": "arun",
       "course": "java",
       "roll no": 1001,
       "age": 25}
del dict1["age"]
print(dict1)

#using pop():                                                   #Output: arun
dict1={"name": "arun",
       "course": "java",
       "roll no": 1001,
       "age": 25}
dict2=dict1.pop("name")
print(dict2)

#clear all items from dictionary:                               #Output: {}
dict1={"name": "arun", 
       "course": "java",
       "roll no": 1001,
       "age": 25}
dict1.clear()
print(dict1)


#7. to print all keys:                                          #Output: dict_keys(['name', 'course', 'roll no', 'age'])
#using keys()

dict1={"name": "arun",
       "course": "java",
       "roll no": 1001,
       "age": 25}
print(dict1.keys())


#8. to print all values:                                         #Output: dict_values(['arun', 'java', 1001, 25])
#using values()
 
dict1={"name": "arun",
       "course": "java",
       "roll no": 1001,
       "age": 25}
print(dict1.values())


#9. to print keys&values :                                       #Output: dict_items([('name', 'arun'), ('course', 'java'), ('roll no', 1001), ('age', 25)])                      
#using items()

dict1={"name": "arun",
       "course": "java",
       "roll no": 1001,
       "age": 25}
print(dict1.items())


#10. print all keys&values using loop:                           #Output: name
                                                                 #        arun
dict1={"name": "arun",                                           #        course
       "course": "java",                                         #        java
       "roll no": 1001,                                          #        roll no
       "age": 25}                                                #        1001
for x in dict1:                                                  #        age
    print(x)                                                     #        25
    print(dict1[x])

#print keys&values:                                              #Output: name arun
                                                                 #        course java
dict1={"name": "arun",                                           #        roll no 1001
       "course": "java",                                         #        age 25
       "roll no": 1001,     
       "age": 25}            
for x,y in dict1.items():
    print(x,y)


#11. print only values using loop:                               #Output: arun
                                                                 #        java
dict1={"name": "arun",                                           #        1001
       "course": "java",                                         #        25
       "roll no": 1001,
       "age": 25}
for x in dict1.values():
       print(x)


#12. print only keys using loop:                                 #Output: name
                                                                 #        course
dict1={"name": "arun",                                           #        roll no
       "course": "java",                                         #        age
       "roll no": 1001,
       "age": 25}
for x in dict1.keys():
       print(x)