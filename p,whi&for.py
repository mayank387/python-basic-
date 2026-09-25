# find the sum of first n natural number. (using while)

n = int(input("enter you number : "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("total sum = ", sum)

# (using for)

n = 10
sum = 0

n = int(input("enter your number : "))
sum = 0
for i in range(1, n + 1):
    sum += i
    print("sum of total", sum)  # (print statment inside the loop)


n = 10
total = 0

for i in range(1, n + 1):
    total += i
    # https://chatgpt.com/c/6a482d14-cc94-83ee-9ec7-0fbca183237b

print("sum of number is : ", total)


# find factorial of any natural number

n = 10
fact = 1  # (1 because factorial of four is 1*2*3*4 = 24 thats why we ignore zero here)

for i in range(1, n + 1):
    fact *= i
    print("factorial is equal : ", fact)  # (print statment inside the loop)


n = 10
fact = 1

for i in range(1, n + 1):
    fact *= i
print("factorial is equal : ", fact)  # (print statment outside the loop)
