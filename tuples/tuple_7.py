# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])


# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 9

# However, item of mutable element can be changed
my_tuple[3][0] = 9
print(my_tuple)

# Tuples can be reassigned
my_tuple = ('p', 'r', 'o')

print(my_tuple)