#Explict type conversion
#Addition of string(higher) data type and integer(lower) datatype
a=457
b="789"
c=0.99
d="numbers"

print("Data type of a",type(a))
print("data type of b ",type(b))
print("data type of c",type(c))
print("data type od d",type(d))

a=str(a)
b=str(b)
c=str(c)

print("data type of a after type conversion",type(a))
print("data type of b after type conversion",type(b))
print("data type of c after typeconversion",type(c))

e=d+a+b+c

print("value of e",e)
print("data of e",type(e))