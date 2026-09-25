
#List 
                       
mark = [94,67,54,67,98,87,78]
print(type(mark))
print(mark[4])

student = ["Mayank" , 22 , 98.6, "Delhi"]
print(student[0]) 
student[0] = "Rahul"
print(student)

# str = "name"
# print(str[0])
# str[0] = "name1"
#its show error because string doesnot support item assignment and it is immutable

str1 = "Hello my name is mayank"
print(str1.replace("mayank" , "amay"))

#slicing in list 

mark1 = [23,54,67,54,56,87,56]
print(mark1[1:6])
print(mark1[-4:-1])

                                      #function in list
mark2 = [34,56,43,455,6,2,87,90]

mark2[0] = 43  

mark2.append(45) #append add element from the last in list
print(mark2)

mark2.sort()                                  
print(mark2)       #sort helps to arrange elemment in ascending order of the list

mark2.sort(reverse=True) #this helps to arrange elements in descending orders
print(mark2)

mark2.reverse() #it reverse the element according to above statment
print(mark2)    #Answer is [2, 6, 34, 43, 45, 56, 87, 90, 455]

mark2.insert(0 , 80) #here 0 is our position where we wanted to add element
print(mark2)

mark2.remove(80) #this will remove the first (80 from the list)
print(mark2)    

mark2.pop(0)    #this will pop the (0) position element
print(mark2)


  #In list all function actions applied on new list 