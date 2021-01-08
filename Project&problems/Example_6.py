# Swapping two variable

x = int(input(" Enter the value of x"))
y = int(input(" Enter the value of y"))

temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))
