#dictionary in python
# "key" : "value"
info = {
    
    "name" : "mayank",
    "age" : "22",
    "room" : "34", 
    "learning" : "coding",
    "marks" : [98,45,54,65,45,44,76], 
    
 } 

print(type(info))
print(info["name"]) 
 
info["name"] = "Esha" # this is how which change value of key in dictonary
print(info)

info["contact"] = 9405049444
info["batch"] = "2021-2023" #this is how which add elements in dictionary
print(info)

null_dict = {}
null_dict["name"] = "esha and mayank"
print(null_dict)

#nested dictionary

student = {
    "name" : "mayank", 
    "subject" : {
        "maths" : "67", 
        "science" : "98",
        "social science" : "67",
        "English" : "80"
    }
}

#creating a dictionarty in a dictionnary called nesting

print(student["subject"]["maths"])

student1 = { 
            "name" : "Mayank karn", 
            "course" : "btech",
            "branch" : "ai-ml",
            "section" : "D",
            }

#some operations we can perform in dictionary

#keys it returns all the key present in dict
print(student1.keys())

#values it will return all the values stores in keys
print(type(list(student1.values())))
print("student1", student1)
print(len(student1))

#items() return all (key, value) pair as tuples
print(list(student1.items()))

pairs = list(student1.items())
print(pairs[0])
print(pairs[2])

#get return the key according to value

print(student1.get("name"))
print(student1.get("branch")) #if the key is not present in the dict it will give none instead of error
print(student1.get("Home"))
#update insert the specified item to the dictionary

# print(student1.update({"Home" : "Delhi",}))
student1.update({"home" : "delhi"})
print(student1)

student1.update({"contact" : "8440485434" , "percentage" : "97%"})
print(student1)