my_list = [1, 2, 4, 5]

a = (x**2 for x in my_list)



print(sum(x**2 for x in my_list))
print(max(x**2 for x in my_list))