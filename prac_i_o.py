#create a new file "practic.txt" using python. Add the following data in it.

#Hi everyone 
#we are learning file I/O
#using java.
#i like programming in java.

with open("practice.txt","w") as f:
    f.write("Hi everyone \nwe are learning file I/O\n")
    f.write("using java\nI like programming in java")

#write a funtion to replace occurences of "java" with "python" in above file 

with open("practice.txt","r") as f:
    
    data = f.read()

new_data = data.replace("java","python")
print(new_data)

# with open("practice.txt","w") as f:
#     data = f.write()  

#waf to find "learning" is present or not 

def check_word ():
    word = "learning"
    with open ("practice.txt", "r") as f:
        data = f.read()
    if word in data:
        print("found")
    else:
        print("not found")

check_word()

#use of readline

with open ('mayank.txt','w') as f:
    
 data1 = f.write("Their are two types of thermometer one is digital and second is normal thermometer")
 data2 = f.write("\nDigital thermometer cost more expensive thenthe normal one")
 data3 = f.write("\nthermometer is a device which is use to measure temperature of human body")

with open('mayank.txt','r') as f:
    print(f.readlines())        
    