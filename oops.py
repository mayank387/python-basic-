# class and object in python
# class is a blueprint for creating objects

class student:
    name = "Mayank"

s1 = student()
print(s1.name)

class car:
    colour = "Black"
    Company = "Maruti suzuki"

car1 = car()
print(car1.colour)
print(car1.Company)


# __init__ function 
# constructor 
class student:
    college_name = "Apna college"  #class atribute
    def __init__(self,Name,address,course,age,marks):
        self.Name = Name  #(object atributes)
        self.address = address 
        self.course = course
        self.age = age
        self.marks = marks
    
    def get_marks(self):   #this is the part of "method" below this topic
        return self.marks
    
obj1 = student("karan","Delhi","B.com",16,98)
print(obj1.Name,obj1.address)
print(obj1.address)
print(obj1.course)
print(obj1.age)
print(obj1.get_marks())
print(obj1.college_name)

obj2 = student("sahil","uttarpradesh","B.tech",45,87)
print(obj2.Name)
print(obj2.address)
print(obj2.course)
print(obj2.age)

# methods (those funtion which is created in class is known as methods)
class employee:  
   def __init__(self,compnany,location,):
    self.company = compnany
    self.location = location

   def welcome(self):
    print("welcome students,", self.company)
    
obj = employee("tcs","gurgoan")
obj.welcome()

#static methods
  # works at class level
  #methods that dont use the self parameter

class employee:  
   def __init__(self,compnany,location,):
    self.company = compnany
    self.location = location
   
   @staticmethod     #this is a decorator in python 
   def hello():
       print("hello")
   
   def welcome(self):
    print("welcome students,", self.company)
    
obj1 = employee("tcs","gurgoan")
obj1.welcome()
obj1.hello()

#abstraction
  #hiding the implementation details of a class and only showing the essential features to the user

class car():
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brk = False
    
    def start(self):
        self.clutch = True
        self.acc = True
        print("car is starts...")

car1 = car()
car1.start()

# encapsulation 
#   wrapping data and funtion into a single unit (object)


# oops part 2 

# delete keyword (it can delete the whole and attributes of the objects)  
class student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

stu1 = student("esha",3434)
print(stu1.name)
del stu1.name

# print(stu1.name)
print(stu1.rollno)

# private attributes and methods 
# A private attribute is an attribute that is intended to be 
# accessed only inside the class.In Python, we indicate it using double 
# underscore "__".

class account:
    def __init__(self,acc_number,password):
        self.acc_number = acc_number
        self.__password = password
    
    def get_password(self):
        return self.get_password

acc_holder1 = account(40594930340,9654)
print("user here is your account number = ",acc_holder1.acc_number)
# print(acc_holder1.__password) #it throwss error because password is now the private attribute

print(acc_holder1.get_password())



