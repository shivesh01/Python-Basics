# Python program to display all the prime numbers within lower and upper interval

lower = int(input("start"))

upper = int(input("end"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper+1):
    # all prime numbers are greater than one
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
