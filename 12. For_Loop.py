# FOR loop
# while declaring range, if you want to print number from 1 to 10 make sure the till parameter is 11
# The range requires +1 number than the required output hence the till parameter is 11
for number in range(1, 11):
    print(number)

# here the third parameter is incremental value, the loop will increment by 2 and the output will be 1, 3, 5, 7, 9 i.e. only the odd numbers
for number in range(1, 11, 2):
    print(number)


# using for loop with list
_list = [True, 1, 2, 3, 4, 5, 6, 7, 8, "abc", "lmn", "pqr", "xyz"]
for item in _list:
    print(item)

# Slicing with foor loop
# for item in _list[:5] - prints the first 5 elements in the list
# for item in _list[5:] - prints the list without the first 5 elements
# for item in _list[1:5] - prints the element from index 1 to 4