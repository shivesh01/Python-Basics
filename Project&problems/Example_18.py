# Fibonacci sequence

def fib(Num):
    a, b = 0, 1

    if Num == 1:
        print(a)
    elif Num >= 1:
        print(a)
        print(b)

        for i in range(2, Num):
            c = a + b
            a = b
            b = c
            print(c)
    else:
        print("please enter a positive number")


n = int(input("How many terms"))

fib(n)


# using Second method by while loop


# n = int(input("How many terms?"))
#
# # first two terms
# n1, n2 = 0, 1
# count = 0
#
# # check if the number of terms is valid
#
# if n <= 0:
#     print("please enter a positive number")
# elif n == 1:
#     print(n1)
# else:
#     print("Fibonacci sequence:")
#     while count < n:
#         print(n1)
#         nth = n1 + n2
#         # update values
#         n1 = n2
#         n2 = nth
#         count += 1
#
