# Python Program to convert Decimal to Binary Using Recursion

def convertToBinary(n):
    if n > 1:
        convertToBinary(n // 2)
    print(n % 2, end='')


decimal = int(input("enter a number"))

convertToBinary(decimal)
