# Find the factorial of a number

def fact(num):
    a = 1
    for i in range(1, num + 1):
        a = a * i
    return a


num = int(input("enter a factorial number"))

print(fact(num))
