
#Conditional Statments
#if , elif , else 

age = int(input("Enter your Age :"))

if ( age >= 18):
    print("Your are applicable of voting")
else:
   print("You are not applicable for voting")
   
light = input("Enter Traffic light colour :")

if(light == "Red"):   #we use if multiple time whenever we wanted to go through or (check) all the conditions 
    print("Stop")   
elif(light == "Green"):
    print("you can go")
else:
    print("Light is broken")


marks = int(input("Enter your marks :"))

# a = marks
if(marks >= 90):
    print("you have passed with 'A' grade ")
elif(marks < 90 and marks >= 80 ):
     print("you have passed with 'B' grade")   
elif(marks < 80 and marks >= 70 ):
    print("you have passed with 'D' grade")
else:
    print("Your marks is below then 70 :")


 #Nesting 
 #whenever we use if statment in if statement then it is called nesting 
 
age = int(input("Enter your age :"))

if (age > 17):
    if(age > 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("you cannot drive")     


     
