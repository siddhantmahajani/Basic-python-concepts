# Functions
# def keyword is used to declare a function
def message():
    print("Hello")

message()

# returning a value from the function
def addition(a, b):
    return a + b

sum = addition(1, 2)
print(sum)

# return multiple values from a function
# returns a list of values from the function
def calculate(a, b):
    return a + b, a * b

cal = calculate(2, 3)
print(cal)

# def add(a, b = 2) : this will add a default value to b incase you don't pass anything as input

# assign keyword arguements
def display(a ,b):
    print(a)
    print(b)

display(b = 3, a = 4)
# the above code will map the value 3 to variable b and 4 to variable a
# if you don't specify, by default the value 3 is mapped to a and 4 is mapped to b

# assign function to variable
def printHello():
    print("Hello")

func = printHello

func()
# here we assigned the function printHello to variabe func and then used the variable to call the function

# global functions
a = 4
def displayGlobal():
    a = 3
    print(a)
    print(globals()['a'])
# here the function globals() will fetch the global variables declared in the program. The variable name is passed in [] brackets
displayGlobal()

# local functions
# here we have defined a function printName and inside the function declared a local function printWelcome
# here printWelcome returns "Welcome" and the printName function will print name
def printName(name):
    def printWelcome():
        return "Welcome "
    return printWelcome() + name

print(printName("Python"))

# return function from another function
# here we defined one function with name returnFunction and returned a value and called that function from another function
def returnFunction():
    return "Welcome"

def callingFunction():
    return returnFunction()

print(callingFunction())

# send a function as a parameter to another function
def function1(msg):
    return "Hello " + msg

def function2():
    return "World"

print(function1(function2()))
# here we passed the function2 as an input parameter to the function1

# RECURSION
# it is a process of calling itself
def recursiveFunction(n):
    if n == 1:
        return 1
    return n + recursiveFunction(n - 1)

print(recursiveFunction(3))

# Fibonacci series example
n = 100
def fibonacci(a, b):
    if a > n:
        return 1
    print(a)
    return fibonacci(b, b + a)
fibonacci(1, 1)

# generator functions
def func():
    a = 1
    while a <= 10:
        yield a
        a += 1

print(list(func()))
# the function returns a generator object which needs to be type casted to list
# yield keyword is used to return a function without destroying the states of its local variables when the function is called
# the execution starts from the last yield statement
# any function that contains the yield keyword is defined as generator

