#wap to print the length of a list (list is the parameter)
cities = ["delhi","gurgoan","noida","pune","haryana"]

def print_len (list):
    print(len(list))

print_len(cities)

#wap to print the element of a list in a single line(list is the parameter)
subject = ["maths", "science","english","hindi","sanskrit"]

def element_list (list):
    for item in list:
        print(item,end=" ")
    print()
    

element_list (subject)
element_list(cities)

#wap to find the factorial of n (n is the parameter)
def factorial (n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
    return 0 
    
factorial(10)
factorial(7)

#waf to convert usd into inr
def usd_to_inr (usd_val):
    inr = usd_val * 95.35
    print(usd_val, "usd = ",inr ,"inr")
    
usd_to_inr(10)

#function to check whether the given number is even or odd
def check_even_odd (n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")

check_even_odd (10)

        

           