#recursive function
def show(n):
    if (n==0):
        return
    print (n)
    show (n-1)

n = int(input("enter your nunber : "))
show(n)

#factorial using recusion (in recursion we always use base case which is represented by (if) )
def factorial (n):
    if (n == 0 or n == 1):
        return 1
    else:
        return factorial(n-1) * n #(https://chatgpt.com/c/6a4fe0bb-ba5c-83ee-816d-2afad8d83e9a)
    
print("factorial of number is : ",factorial(5))


# practice 

# write a recursive function to calculate the sum of first n natural number

def calculate_sum(n):
    if(n == 0):
        return 0
    return calculate_sum(n-1) + n

print("sum",calculate_sum(3))
    
#write a function to print a list 

def print_list(list,idx =0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx +1)
    
state = ('delhi',"uttarpradesh","assam","bihar")

# idx = int(input("Enter starting index: "))

print_list(state[2])
