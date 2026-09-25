#for loop (it is use for sequential traversal)
 
list = [1,2,3,4,5]      

for val in list:
    print(val)

tup = (1,2,3,4,5)      

for val in tup:
    print(val)

veggies = ("potatos","tomatos","cucumber","onion")

for val in veggies:
    print(val)
    
str = "Hello my name is mayank"

for char in str:
    print(char)
else:
    print("End")
    
#use of for loops using else (it is completly optional)
 
str = "Hello my name is mayank"

for char in str:
    if(char == "n"):
        print(" found ")
        break
    print(char)
else:
    print("end")
    
