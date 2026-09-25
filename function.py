#funtion defination
def calc_sum(a,b):
    return (a+b)#4,7 are called parameters
    
sum = calc_sum(4,7)#funtion call , arguments
print(sum)

def calc_sum(a,b):
    sum = (a+b)
    print(sum)
    return sum

calc_sum(43,45)
    
calc_sum(34,76)
 
calc_sum(34,65)

def print_hello():
    print("hello")
    
print_hello()
print_hello()
print_hello()
print_hello()
print_hello()


#calculater the average of 3 values

def calc_average (a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(avg)
    return avg #A function's output is None when it doesn't return a value

mark_avg = calc_average (3,6,9)
print(mark_avg)

#types of function
#Built_in function
  # type1 = print,range,len,type
  # type2 = user defined funtion
  
 
