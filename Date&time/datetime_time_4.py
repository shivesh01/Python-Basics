from datetime import time

# time(hour = 0, minute = 0, second = 0)
a=time()
print(a)

# time(hour, minute and second)
b=time(12,36,23)
print(b)

# time(hour, minute and second)
c=time(hour=1,minute=50,second=56)
print(c)

# time(hour, minute, second, microsecond)
d=time(11,32,23,4343)
print(d)

a=time(11,20,30,232)