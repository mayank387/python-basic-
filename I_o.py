# file input output

# read method
f = open("hello.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close ()

f = open("hello.txt", "r")
line1 = f.readline()
print(line1)

line2 = f.readline() #this will print next line 
print(line2)

# print(f.readline()) this will also print next line
# print(f.readline())

f.close ()

# write to a file

f = open("sample.txt","a")#if file is not exists then writr and append create a file automatically

f.write("\nHello my name is mayank")

f.write("\nprogramming is going well")

f.close

# append in file

#how to open a txt file 

with open("python.txt","r") as f: #with syntax doesnt need to close the file
    data = f.read()        
    print(data)         
    
import os

os.remove("sample.txt")