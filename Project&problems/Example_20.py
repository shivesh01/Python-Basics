# Find a Armstrong numbers in a certain interval

lower = int(input(" enter lower number"))
upper = int(input(" enter upper number"))

for num in range(lower, upper + 1):

    order = len(str(num))

    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)
