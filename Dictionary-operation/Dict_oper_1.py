# We can test if a key
# is in a dictionary or not using the keyword in. Notice that the membership test is only for the keys and not for the values.

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print(1 in squares)

print(2 not in squares)

print(49 in squares)

# all()	Return True if all keys of the dictionary are True (or if the dictionary is empty).
# any()	Return True if any key of the dictionary is true. If the dictionary is empty, return False.
# len()	Return the length (the number of items) in the dictionary.
# cmp()	Compares items of two dictionaries. (Not available in Python 3)
# sorted()	Return a new sorted list of keys in the dictionary.
