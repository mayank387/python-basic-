#WAP to ask the user to enter name of their 3 favourite movies and store them in a list

print("Enter your three favourite movie name")

# list.append(input("Enter your fouth ")) doubt

a = input("Enter your first movie name : ")
b = input("Enter your second movie name : ")
c = input("Enter your third movie name : ")

list = []

list.append(a)
list.append(b)
list.append(c)
print(list)

#WAP to check if a list contains a palindrome of element .(hint.use copy(method))
[1,2,3,2,1]

list1 = [1,2,3,2,1]
list2 = ["racecar"]
copy_list = list1.copy()
copy_list.reverse()

if(list1 == copy_list):
    print("List is palindrome")
else:
    print("List is not palindrome")
    

                             #check palindromic or not according to the user input         
                             
a = input("Enter your string :- ")

name = list(a)

# name.append(a)

copy_name = name.copy()

copy_name.reverse()

if(name == copy_name):
    print("Your input is palindromic")
else:
    print("Your input is not palindromic")
    
#WAP to count the number of students with the "A" grade in the following tuple


tup = ("C","D,","A","A","B","B","A")

print(tup.count("A"))

suple = tup.count("A")
print(suple)

#store the above value in a list and sort them from "A" to "B"

list21 = ["C","D,","A","A","B","B","A"]

list21.sort()
print(list21)

a = input("Enter your string :- ")

name = list(a)
copy_name = name.copy()

copy_name.reverse()

if name == copy_name:
    print("Your input is palindromic")
else:
    print("Your input is not palindromic")
