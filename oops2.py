# inheritance                    
class car:
    show_room = "Najafgarh"
    @staticmethod
    def car_start():
        print("car started...")
    
    @staticmethod
    def car_stop():
        print("car stopped...")
    
class toyota_car(car):
    def  __init__(self,name,colour):
        self.name = name
        self.colour = colour
    
car1 = toyota_car("innova","grey")
print(car1.name)
print(car1.car_start())
car1.car_stop()
print(car1.show_room)


# # Three types of inheritance 
# 1. single level inheritance "One child class inherits from one parent class.
# 2. multi-level inheritance "A class inherits from a class that itself inherits from another class."
# 3. multiple inheritance "Multiple child classes inherit from the same parent class."

# multi level inheritance 
class car:
    @staticmethod
    def car_start():
        print("car starting...")

    @staticmethod
    def car_stopped():
        print("car stopped...")

class toyota_car(car):
    def __init__(self,toyota_car):
     self.toyota_car = toyota_car
        
class car_colour(toyota_car):
    def __init__(self,car_colour):
        self.car_colour = car_colour
        
car1 = car_colour("black")
car1.car_start()
print(car1.car_colour)

#multi level inheritance
class start:
    @staticmethod
    def car_started():
        print("car starting...")
class car(start): 
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
        # print("car model is ",self.Model)
               
         
car1 = model("Maruti","brezza","black","top") 
print(car1.Brand)
car1.Model
print("car model is ",car1.Model)
car1.car_started()

 #super method **`super()`** lets a child class reuse code from its parent class automatically.
 
 
class start:
    @staticmethod
    def car_started():
        print("car starting...")
        
class car(start): 
    def __init__(self,Brand): 
        self.Brand = Brand  
           
class brand_name(car): 
    def __init__(self,Brand,name,colour): 
       super().__init__(Brand)
       self.name = name 
       self.colour = colour
 
class model(brand_name): 
    def __init__(self,Brand,name,colour,Model): 
        super().__init__(Brand,name,colour)
        self.Model = Model
        # print("car model is ",self.Model)
               
         
car1 = model("Maruti","brezza","black","top") 
print(car1.Brand)
car1.Model
print("car model is ",car1.Model)
car1.car_started()

# class method decorator
class person:
    name = "anonymous"

    @classmethod
    def changename(cls,name):
     cls.name = name

print(person.name)
p1 = person()
p1.changename("mohan")
print(p1.name)

# property decoratorThe **`@property` decorator** lets you access a class method like an instance attribute, allowing you to compute values dynamically or add getter/setter validation without changing your class interface.

class student:
    def __init__(self,phy,chemis,maths):
        self.phy = phy
        self.chemis = chemis
        self.maths = maths
        # percentage
        # self.percentage = str((self.phy + self.chemis + self.maths) / 3) + "%" 
    
    @property 
    def cal_percentage(self):
        return str((self.phy+self.chemis+self.maths) / 3) + "%"

        

stu1 = student(98,80,97)
print(stu1.cal_percentage)
stu1.phy = 87
print(stu1.phy)
print(stu1.cal_percentage)  

# polymorphism when the same operator is allowed to have different meaning according to context.

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(num1,num2): 
        newreal = num1.real + num2.real
        newimg = num1.img + num2.img
        return Complex(newreal,newimg)
    
         
num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()
    
 
        