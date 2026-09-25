                                  
                                  #string function

#endswith return true if string ends with substr
str7 = "I live in delhi form past two years"
print(str7.endswith("years"))
print(str7.endswith("not years"))

#str.capitalize() capitalize 1st char
str8 = "currently i am pursuing btech from lloyd institude of engineering and technology"
print(str8.capitalize())
print(str8)

    #or 
    
str9 = "currently i am pursuing btech from lloyd institude of engineering and technology"
# str = str9.capitalize()
# print(str)
print(str9.capitalize)

#str.replace(old,new) , replace all occurences of old value
str10 = "i am studying python from apna college"
print(str10.replace("i" , "u"))
print(str10.replace("python" , "javascript"))

#str.find(word) returns 1sr index of the 1st occurrens 

str11 = "Hello my name is Hello . Hello how are you Hello"
print(str11.find("is"))
print(str11.find("s"))


#str.count("am") counts the occurence of the substring
str12 = "Hello my name is Hello . Hello how are you Hello"
# print(str12.count("Hello"))
print(str12.count("Hello"))



