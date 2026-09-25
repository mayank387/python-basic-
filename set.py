#set is mutable but element of the set is immuteable

Number = {1,3,4,5,6,"hello",65.4,"hello"} 
print(type(Number))
print(Number)

#duplicate values will not print it doesn't show any kind of error it just ignore the duplicate values
print(len(Number))

Number1 = set() #this is how we create empty set because in empty dict we use curly brackets

#operation 

#set.add(elemt) add an element
Number1.add("mayank")
Number1.add(45)
Number1.add(67)

Number1.remove(45)
print(Number1)

#we can store tuple and string in set but we cannot store list in set

Number1.add("karn")
Number1.add((2,4,5,4))
print(Number1)
# Number1.set([3,4,4,2,4,34,3])

#set.clear it remove all the element from the set

# Number1.clear()
# print(Number1)

#set.pop it pop the random element from the set

print(Number1.pop()) 

#set.union combine both set values and return a new set

room = {34,45,65,66,76,87,97}
room1 = {65,54,54,97,34,66}

print(room.union(room1))

#set.intersection combine common values and returns new

print(room.intersection(room1))


