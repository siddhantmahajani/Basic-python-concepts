# Lambda expression
# it is an anonymous function which does not require a specific name

# simple cube of the variable using lambda
cube = lambda a: a * a * a
print(cube(3))

# simple addition of two variables
sum = lambda a, b: a + b
print(sum(3, 4))

# maximum between two numbers
max = lambda a, b: a if a > b else b
print(max(2, 3))

# odd and even
result = lambda a: "even" if a % 2 == 0 else "odd"
print(result(2))

# in the above if else conditions, if the value is even it will return even else it will return odd

# filter the elements from a given list
# if the numbers in the list are below 10, return and add it to the list
li = [1, 2, 44, 55, 3, 7, 9, 3, 56, 99, 0, 21]
response = list(filter(lambda a: a < 10, li))
print(response)
# the filter() method constructs an iterator from elements of an iterable for which a function returns true

# replace the elements in the list with the square of that number
l2 = [2, 3, 4, 5, 6, 7, 8]
square = list(map(lambda a: a * a, l2))
print(square)
# the map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results

# add numbers from the list using reduce function
from functools import reduce
# the above statement is used to import the reduce function from the functools library
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = reduce(lambda a, b: a + b, l1)
print(sum)
# this will return the sum of all the elements present in the list
# the reduce(fun,seq) function is used to apply a particular function passed in
# its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module

# sort the ranks according to percentage using sorted function
students = [["ABC", 91.5], ["LMN", 97.3], ["PQR", 95.8], ["XYZ", 94.3]]
result = sorted(students, key = lambda a: a[1])
print(result)
# the sorted() function returns a sorted list from the items in an iterable
# it will sort the variables in ascending order according to the marks

