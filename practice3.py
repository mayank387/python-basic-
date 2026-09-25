#WAP to check if a number entered by user is odd or even

num = int(input("Enter your number : "))

if(num%2 == 0):
    print("Number entered by you is even")
else:
    print("Number entered by you is odd")
    
    
#WAP to check if a number is multple of 7 or not

num1 = int(input("Enter your number : "))

if(num1 % 7 == 0):
    print("Number entered  by you is multiple of 7 ")
else:
    print("Number entered by you is not the multiple of 7")
    

#WAP to find the greatest of 3 number entered by the user 

a = int(input("Enter your first number : "))
b = int(input("Enter your second nmuber : "))
c = int(input("Enter your third number : "))

if(a > b and a > c):
    print("A is the greatest number")
elif(b > c):
    print("B is the greatest number")
else: 
    print("C is the greatest number")


