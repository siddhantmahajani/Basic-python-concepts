# changing a type of a variable

a = 'Number'
b = 7

#print(a + b) # this will throw an error saying can only concatinate str not int

print(a + str(b)) # this will conver the int variable into str and then concatinate 2 strings and return a result

print(type(b)) # will return int as it is a variable of type int
print(type(str(b))) # will return str as it is typecasted to str

x = '7'
y = 9

print(int(x) + y) # changed the type of x from str to int for addition of 2 numbers

print(x + str(y)) # changed the type of y from int to str for concatination of 2 strings

# Type casting can be done for all the types int(), str() and float()
m = '3.145667'
n = 9

print(float(m) + n) # converted m from str to float for addition of two numbers