
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
    