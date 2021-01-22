# Define a dictionary using {}
# Dictionary are nothing but key value pairs

dict = {"red":"apple", "yellow":"banana", "orange":"orange", "green":"watermelon"}
print(dict)

print(dict.keys()) # This returns only the keys from the dictionary
print(dict.values()) # This returns only the values from the dictionary
print(dict["red"]) # Pass the key as input to fetch the appropriate value associated with the key

dict["peach"] = "lychee" # adds a new key pair to the dictionary

print(dict)

# To delete a key value pair from the dictionary simply use
# del dict["red"] # this will delete the key value pair for the key red