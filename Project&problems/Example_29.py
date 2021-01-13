# Program make a simple calculator

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print("Select operation")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")

while True:

    choice = input("Enter choice(1/2/3/4): ")

    if choice in ("1", "2", "3", "4"):
        num1 = int(input("Enter first number"))
        num2 = int(input("Enter second number"))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))
        break

    else:
        print("Invalid Input")
