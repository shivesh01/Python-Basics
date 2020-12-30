# if-else Conditional Dictionary Comprehension

orginal_dict = {'jack': 28, 'micheal': 48, 'guido': 57, 'john': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young')
              for (k, v) in orginal_dict.items()}
print(new_dict_1)
