# print multiplication table  1 (--10 instead of 1---)10

number = int(input("Enter a number"))

count = 10
while count >= 0:

    product = number * count

    print(number, "X", count, "=", product)

    count = count - 1

