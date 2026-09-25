#calculate the average of three marks 
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def marks_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your average is ",sum/3)
            
        
stu1 = student("mayank",[98,89,90])
stu1.marks_avg()

stu1.name = "mayank karn"
stu1.marks_avg()

#create account class with 2 attributes - balance & account no.
#create methods for debit, credit and printing the balance

class account():
    def __init__(self,current_balance,acc_number):
        self.current_balance = current_balance
        self.acc_number = acc_number
    
    def debit(self,amount):
        self.current_balance -= amount
        print("Rs. ",amount," amount was debited")
        print("Rs. ",self.current_balance,"current balance")

    def credit(self,amount):
        self.current_balance += amount
        print("Rs. ",amount,"amount was credit")
        print("Rs. ",self.current_balance,"current balance")
        
    def get_balance(self):
        return self.balance
        
        
acc1 = account(10000,4953432)
acc1.debit(5000)
acc1.credit(101)


#define a circle class to create a circle with radius using the constructor 
class circle:
    def __init__(self,radius):
        self.radius = radius
    
    def area_circle(self):
        print("Area of circle is ", (3.14 * self.radius**2))
    
    def parameter_circle(self):
        print("Parameter of the cirle is ", (2 * 3.14 * self.radius))

c1 = circle(7)
c1.area_circle()
c1.parameter_circle()


#define an employee class with attributes role, departmemt and salary. this class also has a showdetails() method 
    
class employee:
    
    def __init__(self,Role,Department,Salary):
        self.Role = Role
        self.Department = Department
        self.Salary = Salary
    
    def showdetails(self):
        print("Role =", self.Role,
              "Department = ",self.Department,
              "Salary =",self.Salary,
              )
        
class engineer(employee):
    def __init__(self,name, age):
        super().__init__("Team leader,","Software development,","100K,")
        self.name = name
        self.age = age
        
E1 = employee("HR,","IT,","50,000")
E1.showdetails()

e2 = engineer("Mayank",21)
e2.showdetails()
        
        
#create a class called order which stores item ad its 
# price use dunderfuntion __gt__() to convey that:
# order1 > order2 if price of order1 > price of order2

class order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
    
    def __gt__(obj1,obj2):
        return obj1.price > obj2.price
            
        
obj1 = order("soft drink", 100)

obj2 = order("cold drink ", 40)
        
print(obj1 > obj2)
        


        
        




    
    

     

         
        
    