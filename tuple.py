#tuple

Number = (45,56,34,54,76,3,44,45)
print(type(Number))
print(Number[0])
# Number[2] = 34 not possible beacause tuple is immutable
 
  #slicing in tuple
 
tup = (45,56,34,54,76,3,44,45)
print(tup[0:4])
print(tup[1:4])

print(tup.index(54))

position = tup.index(54) #this the returns at what position 54 occurs first
print(position)

print(tup.count(45))
print(tup.count(44))