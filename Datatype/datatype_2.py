num_int=123
num_str="1.23"

num_new = num_int +num_str

print("datatype of num_int:",type(num_int))
print("datatype of num_float:", type(num_str))

print("value of num_new",num_new)
print("data type num_new",type(num_new))

#As we can see from the output, we got TypeError. Python is not able to use Implicit Conversion in such conditions.
#However, Python has a solution for these types of situations which is known as Explicit Conversion.
