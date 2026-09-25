seq = range(5)
 
for i in seq:
    print(i)
    
#another way 
for i in range(10): #range(stop)
    print(i)
    
for i in range(2,10): #range(start,stop)
    print(i) 
    
for i in range(10): #range(start,stop,step size)
    print(i)
    
for i in range(2,101,2): #print even no. using range 
    print(i)
    
    
#using rane and for print no. from 1 to 100

for i in range(0,101,1):
    print(i)
    
#print number from 100 to 1 

for i in range(101,0,-1):
    print(i)

#print multiplication table of number n 

n = int(input("enter your number: "))

for i in range(1, 11):
    print(n * i)
    

for i in range(1,100):
    print(i * i)
    
    
    
#pass statement 

for i in range(9):
    pass                                
print("print some value")
    
    
    
n = 5 

sum = 0 
for i in range (1,n+1): #(range does not includes the last digit)
    sum += i #https://chatgpt.com/c/6a482d14-cc94-83ee-9ec7-0fbca183237b
    print(i)

    