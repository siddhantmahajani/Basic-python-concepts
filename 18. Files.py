# Files
# you can read, write and append to a file in python

#f = open("name or path", "mode", "buffer")
# here the open method has 3 parameters, name or path of the file, mode in which you want to open the file and buffer
# the third buffer parameter is optional to set the buffer size
# modes: w - when you want to write to the file, r - read only mode, a - if there is data in the file, use append to add the data to existing data
# w+ - helps you to read and write, r+ - helps you to read, write and append, a+ - helps you to read and append

#f.close() - used to close the opened file

# open a file and write data to the file

f = open("test.txt", "w")
a = input("Enter data to be written in the file: ")

f.write(a)
f.close()

# append multiple lines to the file
fruits = ["apple", "banana", "pineapple", "orange", "mango", "watermelon"]
f = open("test.txt", "a")
for i in fruits:
    f.write("\n" + i)

f.close()

# read the contents from the file
f = open("test.txt", "r")
print(f.read())
f.close()

# check if the file exists

import os, sys
if os.path.isfile("test.txt"):
    print("File found")
else:
    print("File does not exist")
    sys.exit()

# sys exit will terminate the code from further executions