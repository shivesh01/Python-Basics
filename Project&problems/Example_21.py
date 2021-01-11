# Sum of natural numbers

num = int(input(" enter Sum to nth term"))

if num <= 0:
    print(" Please enter a positive number")

else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print("The sum is", sum)
