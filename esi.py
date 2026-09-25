list = [1,4,9,16,25,36,49,64]
x = 36

idx = 0
for el in list :
    if(el == x):
       print("x is found at the index", idx)
       break 
    idx += 1 
        
        
# Print the multiplication table of a number entered by the user.

n = int(input("enter your number : "))

for i in range(1,11):
   if (i == 5):
      continue
   if (i == 8) :
      break
   print(n * i)
   
# find the sum of number from 1 to n 

n = int(input("enter you n number : "))
total = 0

for i in range (1, n + 1):
   total += i 
  
print("Here is the sum of your given range",total) 

#function 
#calculate the sum of n number 


with open("hello.txt",'a') as f:
   data = f.write("Hello world")
   print(data)
   
   
   
word = "learning"
with open('practice.txt','r') as f:
   data = f.read()
   if data.find(word):
      print("found")
   else:
      print("Not found")
   
a = int("A", 26)
print(a)

a = int("2",56)
print(a)


#for oops concept
class car: 
    def __init__(self,Brand): 
        self.Brand = Brand     
class brand_name(car): 
    def __init__(self,Brand,name,colour): 
       car.__init__(self,Brand)
       self.name = name 
       self.colour = colour
 
class model(brand_name): 
    def __init__(self,Brand,name,colour,Model): 
        brand_name.__init__(self,Brand,name,colour)
        self.Model = Model
               
         
car1 = model("Maruti","brezza","black","top") 
print(car1.brand)

