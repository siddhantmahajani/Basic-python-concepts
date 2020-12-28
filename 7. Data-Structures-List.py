# List

# declaring a list
# The list starts with index 0
_list1 = [1,2,3,4,5,4.5,"Abc", True] # you can define variables of any type in a list without defining a proper datatype
print(_list1) # print the whole list
print(_list1[1]) # fetch the element on index 1
print(_list1[1:5]) # print elements from index 1 to 4
print(_list1 * 3) # repetition: we repeated the list elements 3 times
print(len(_list1)) # returns length of the list

# List indexing and slicing
_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(_list)
print(_list[0]) # returns the first element of the list
print(_list[-1]) # returns the last element of the list
print(_list[-2]) # returns the second last element of the list
print(_list[2:]) # returns the list without the first 2 elements
print(_list[-2:]) # returns the last 2 elements of the list
print(_list[:2]) # returns the first 2 elements of the list
print(_list[:-2]) # returns the list without the last 2 elements
print(_list[::2]) # returns alternate element from the list, the interval is set with the value 2
print(_list[0:6:2]) # returns every alternate element from the list from index 0 to 5
print(_list[0:5]) # print elements from 0 to 5
print(_list[5:0:-1]) # prints the elements in reverse order

# Add and remove elements from the list
list1 = [1, 2, 3, 4, 5, 6, "Python", "Java"]
list1.append("C") # add a new variable at the end of the list
print(list1)
list1.insert(6, "Ruby") # added a new string ruby at index 6
print(list1)
list1[2] = 7 # changed the element on index 2 from 3 to 7
print(list1)
list1.remove("C") # remove C from the list
print(list1)
# del list1[index] will also remove an element from the list on the given index
# del list1 will delete the list completely
# list1.pop() will remove the last element from the list, you can also pass index to the pop function list1.pop(2)
# you can also store the variable returned by the pop method in a variable or print the popped variable

# List and Range
# list2 = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10] this can be used to define a hard coded list
# You can also use the range function to define the list from 1 to 10
list2 = list(range(1, 11)) # this will create a list with elements 1 to 10
print(list2)
list2 += [11, 12, 13, 14, 15, 16] # added 2nd list to the first list
print(list2)
print(max(list2)) # returns the maximum element from the list
print(min(list2)) # returns the minimum element from the list
list2.sort(reverse=True) # this will sort the list in the descending order, If no parameter is passed the default mechanism is ascending order
print(list2)
# The sorting functions and max min functions can only work with the list of same datatypes. Mixed datatype sorting is not supported
list2.reverse() # this can be used to reverse the list
print(list2)

# Reverse and sort list of strings
data = ["abc", "lmn", "pqr", "xyz", "efg", "hij"]
data.reverse() # this will reverse the list
print(data)
# If you want to reverse the list and assign it to a different variable you can use
result = reversed(data) # this method will store a reversed object of the data in result
print(list(result)) # to view the elements in the list you will have to typecast it to the list object and then print the elements
data.sort() # this will sort the list, by default the sorting is in ascending order
print(data)
# if you want to store the sorted list in a different list you can use
result = list(sorted(data)) # this will sort the list in a sorted order and store it in the result variable
print(result)
len_sort = list(sorted(data, key=len)) # this will sort the list length wise in ascending order and not alphabetically
# len_sort = list(sorted(data, key=len, reverse=True)) this will help you sort the list length wise in descending order
print(len_sort)

# List of lists
lists = [["abc", "efghi", "jkl"], ["lmn", "opqr", "stu"], ["vwx", "yz", "d"]] # Here we have defined 3 lists in one single list
print(lists) # this will print 3 lists present in one list, it is called Nested List
print(lists[0]) # will return the list present on the index mentioned
print(lists[1][2]) # this will return the element present on the 2nd index of the list present on the 1st index: stu
print(lists[1][2][:2]) # this will return the first two characters of the element present on 2nd index of the list on the 1st index: st
lists[0].append("def") # this will append the element def to the list present on index 0
print(lists)
del lists[2] # this will delete the list present on the 2nd index
print(lists)