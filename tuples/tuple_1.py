# A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a
# tuple once it is assigned whereas we can change the elements of a list.

# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed data types
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)

'''
# advantages:
# 
# We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types. 
# Since tuples are immutable,iterating through a tuple is faster than with list. So there is a slight performance 
# boost.
# Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not 
# possible.
# If you have data that doesn't change, implementing it as tuple will guarantee that it remains 
# write-protected. 
'''