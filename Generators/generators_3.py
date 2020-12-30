def rev_str(my_str):
    length = len(my_str)
    for i in range(length -1, -1, -1):
        yield my_str[i]


for char in rev_str("hello"):
    print(char)

# This generator function not only works with strings, but also with other kinds of iterables like list, tuple, etc.

#The major difference between a list comprehension and a generator expression is that a list comprehension produces the entire list while the generator expression produces one item at a time.