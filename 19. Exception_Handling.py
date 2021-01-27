# exception handling
a = 2
b = 10
try:
    c = a/b
except Exception as ex:
    print(ex)

print("Hello")

# exception handling is useful to avoid program from stopping abruptly and continuing the further process and functions

# multiple exception handling
# for this you will need to know the exceptions which are thrown accordingly else the parent Exception will handle all the exceptions thrown
try:
    c = a/b
except TypeError:
    print("you cannot add variables of two different types")
except ZeroDivisionError:
    print("you cannot divide a number by zero")
print("successful execution")

# else block in exception handling
# this will execute if there are no errors thrown by the try block
try:
    print(a + b)
except TypeError:
    print("type error")
except ZeroDivisionError:
    print("zero division error")
else:
    print("no exception thrown")
print("successful execution")


# finally statement/block
# this block is execute everytime when the try block is executed (if it throws an exception or not)
x = 2
y = 1
try:
    division = x/y
    print(division)
except ZeroDivisionError:
    print("zero division error")
finally:
    print("finally block printed with/without exception")

# finally block is useful while working with files, it is easy to close the opened file in finally if it throws an exception or not

# assert keyword
# The assert keyword is used when debugging code.
# The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError
assert int(7) > 5, "number should be greater than 5"
# if the number is less than 5 it will throw an assertion error and the code will exit, if the number is greater than 5 then it won't