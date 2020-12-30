# 1. From list comprehension
h_letters = [letter for letter in 'human']
print(h_letters)

# 2.From loop
#
# h_letters = []
#
# for letter in 'human':
#
#     h_letters.append(letter)
#
# print(h_letters)


# Points
# List comprehension is an elegant way to define and create lists based on existing lists.
# List comprehension is generally more compact and faster than normal functions and loops for creating list.
# However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
# Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension
