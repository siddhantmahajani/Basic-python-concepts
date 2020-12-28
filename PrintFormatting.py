#Various printing formats

print('Hello')
print('World')
# By default the print function prints on new line

print('Hello \n world')
# \n is used to print the second string on the new line

a,b = 1, 10
print(a,b) # by default it adds a space between two numbers before printing them

print(a, b, sep="&") # it adds a custom seperator between two numbers before printing

name = 'Test'
marks = 74.13

print(name, marks) # print normal name and marks without strings
print("Name:",name,"and Marks:",marks) # print variables with string
print("Name:%s and Marks:%f"%(name, marks)) # %s for strings, %f for float and %i for integers
print("Name:%s and Marks:%.2f"%(name, marks)) # %.2f which will let you display only 2 decimals
print("Name:{} and Marks:{}".format(name, marks)) # use {} to print variables along with a string
print("Name:{0} and Marks:{1}".format(name, marks)) # add index to the {} bracket to display appropriate value from the variables