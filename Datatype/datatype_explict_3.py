num_int = 123
num_str = "456"

print("data type of num_int",type(num_int))
print("data type of num_str",type(num_str))

num_str = int(num_str)
print("data type of num integer after typecasting:",type(num_str))

num_sum= num_int + num_str

print("sum of num_int and num_str ",num_sum)
print("data type of num_sum",type(num_sum))