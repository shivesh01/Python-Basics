# If Conditional Dictionary Comprehension

orginial_dict = {'jack': 38, 'micheal': 48, 'guido': 57, 'john': 33}

even_dict = {k: v for (k, v) in orginial_dict.items() if v % 2 == 0}
print(even_dict)
