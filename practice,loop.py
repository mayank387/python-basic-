# print number from 1 to 100 

i = 1 
while i < 101:
    print(i)
    i += 1
print("loop is end")

#print number from 100 to 1

a = 100
while a >= 1:
    print(a)
    a -= 1
    
#print the multiplication of a number n 

n = int(input("enter your number : "))
i = 1
while i <= 10 :
    print(i*n)
    i += 1
#print the element of the following list using a loop
# [1,4,9,16,25,36,49,64,81,100]

i = 1
while i <= 10:
    print(i**2)
    i += 1 
    
list = [1,4,9,16,25,36,49,64,81,100]
print(len(list))

i = 0
while i < len(list):
    print(list[i])
    i += 1

heros = ["ironman","thor","superman", "batman"]
 
 #visiting every element called traverse
  
i = 0
# or we can write i < len(hero``)        
while i < len(heros)-1: # len(heros)-1 = 2 
    print(heros[i])
    i += 1
    
#search for a number x inn this tuple using loop

tuple = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter no. for search "))

i = 0 
while i < len(tuple):
    if(tuple[i] == x): # tuple which is present on the i'st index is == value of x or not
        print("x is found", i )
        break
    else:
        print("x is finding")
    i += 1
       







