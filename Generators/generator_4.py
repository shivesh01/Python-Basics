my_list = [1, 2, 4, 5]

list_ = [x**2 for x in my_list]

generator = (x**2 for x in my_list)

print(list_)
print(generator)