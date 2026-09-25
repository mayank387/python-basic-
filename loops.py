# while loops 

count  = 1
while count <= 5 :
    print("hello", count)
    count += 1
    
print(count)#6 

i = 1
# while count <= 10:
while i <= 100:
    print("Mayank is great", i)
    i += 1
    
#print number from 1 to 10
a = 1
while a <= 10 :
    print(a)
    a += 1

#this is how we print numbers in reverse order
a = 10
while a >= 1 :
    print(a)
    a -= 1
#break keyword       

i = 0 
while i < 50:
    if (i == 48):
         break
    print(i)
    i += 1
    
print("end of loop")

#continue

i = 0
while i <= 5:
    if (i == 3):
        i +=1
        continue  #use for skip item                
    print(i)
    i += 1   
    
#for odd number

i = 0
while i <= 50:
    if (i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1
     
                     
