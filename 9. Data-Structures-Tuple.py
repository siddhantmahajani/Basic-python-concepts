# Tuple
# to define a tuple use () and add elements to the tuple

_tuple = (1, 2, 3, "abc", "lmn", "xyz", 2.5, [3.4, 4.3, 5.2]) # You can add any datatype inside tuple
# we can also add a list inside tuple
print(_tuple)
print(_tuple[2]) # to fetch element present on index 2 of the tuple
print(_tuple * 2) # prints the tuple twice
print(_tuple.count(2.5)) # counts the number of times 2.5 is present in tuple
_tuple[7].append(6.3) # this adds element in the list on position 7
print(_tuple)