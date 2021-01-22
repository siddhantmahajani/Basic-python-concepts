# List Comprehension

#_list1 = []
#for i in range (1, 11):
#    _list1.append(i)

# another method of declaring list is:
_list1 = [i for i in range(1, 11)]
print(_list1)

# Value validation using list comprehension
data = ['1', '2', '3', '4', True, None, None, '5', '6', '7', '8', False, None, None]
#result = []
# same can be done using list comprehension as follows
# it will just reduce the line of code
result = [i if i != None else 0 for i in data]
# here we replaced the value None with 0
#for i in data:
#    if i != None:
#        result.append(i)
#    else:
#        result.append(0)

# another way of doing the without using if condition
result1 = [i or 0 for i in data]
# here None is automatically considered as a False value and False is marked as 0, hence the element with False is also marked 0
# If loop way is generally considered if you want a typical type of output which needs to be inserted in the list
print(data)
print(result)
print(result1)