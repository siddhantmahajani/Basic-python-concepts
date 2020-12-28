# Work with strings

str1 = 'Python'
str2 = ' programming language'

print(str1 + str2) # concats both the strings
print(str1 * 3) # prints str1 3 times
print(str1[:2]) # returns first 2 characters of the string
print(str1[:-2]) # returns string without the last 2 characters
print(str1[2:]) # returns string without the first 2 characters
print(str1[-2:]) # returns last 2 characters of the string
print(str1[1::2]) # returns alternate characters of the string starting from index 1

# String methods
string1 = 'Python'
string2 = ' is a programming language'

print(string2.find('language')) # returns the position of the variable in the string
print(string2.find('i')) # you can also search for a single letter
print(string2.count('i')) # returns the count of the variable in the string
print(string2.split(' ')) # returns list of split string with a space
print(string2.replace('programming', 'coding')) # replaces programming with coding

