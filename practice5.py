#wap to store following word meanings in python dictionary

dict = {
    "table" : ["a piece of furniture","list of fact and figures"],
    
    "cat" : "a small animal"
}

#you are give a list of subjects for students. Assume one classroom is required for one subject. how many classroom are needed by all studetns 

classroom = {"python", "java" , "c++", "python","javascript","java","c++","c"} 
print(len(classroom))

#wap to enter marks of 3 subjects from the user and store them in dictionary. start with an empty dictionary and add one by one . use subject name as key and marks as value

marks = {}

subject = int(input("enter your first subject marks : "))
marks.update({"maths" : subject})


subject2 = int(input("enter your second subject marks : "))
marks.update({"science" : subject2})

subject3 = int(input("enter your third subject matks : "))
marks.update({"Hindi" : subject3})

print(marks)

#figure out a way to store 9 and 9.0 as seprate values in the set (you can take help of built-in data types)

box = {
    ("float",9),
    ("int",9.0),
}

print(box)

#second solution
box = {9 , "9.0"}
print(box)



