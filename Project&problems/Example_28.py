# # Find the factors of a number
#
# num = int(input(" enter a number"))
# print("The factors of ",num, "are:")
# for i in range(1, num+1):
#     if num % i == 0:
#         print(i)
#
#

# 2nd method using functions


def print_factors(X):
    print("The factors of", num, "are:")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)


num = int(input("enter a number"))

print_factors(num)
