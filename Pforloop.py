# print the element of the following list using a loop

list = [1,4,9,16,35,54,65,6,7,66]

for el in list: #we can also use (val) instead of el
    print(el)
    
#search for a number (x) in this tuple using loop

tup = (1,4,9,16,25,36,49,64,81,100,49)

x = 49

idx = 0
for el in tup:
    if (el == x):
        print("you have found your number", idx)
        break    
    idx += 1
    