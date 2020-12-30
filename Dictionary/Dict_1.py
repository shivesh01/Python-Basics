person1 = {"name": "linus", "age": 21}
print(person1)

# Python Dictionary Methods Methods that are available with a dictionary are tabulated below. Some of them have
# already been used in the above examples.
#
# Method	Description
# clear()	Removes all items from the dictionary.
# copy()	Returns a shallow copy of the dictionary.
# fromkeys(seq[, v])	Returns a new dictionary with keys from seq and value equal to v (defaults to None).
# get(key[,d])	Returns the value of the key. If the key does not exist, returns d (defaults to None).
# items()	Return a new object of the dictionary's items in (key, value) format.
# keys()	Returns a new object of the dictionary's keys.
# pop(key[,d])	Removes the item with the key and returns its value or d if key is not found. If d is not provided and the key is not found, it raises KeyError.
# popitem()	Removes and returns an arbitrary item (key, value). Raises KeyError if the dictionary is empty.
# setdefault(key[,d])	Returns the corresponding value if the key is in the dictionary. If not, inserts the key with a value of d and returns d (defaults to None).
# update([other])	Updates the dictionary with the key/value pairs from other, overwriting existing keys.
# values() Returns a new object of the dictionary's values
