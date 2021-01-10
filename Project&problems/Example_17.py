# Multiplication table

def table(a):
    for i in range(1,11):
        print(a, "*", i, "=", a*i)

a = int(input("Enter a number"))
table(a)


# # without using functions
# num = int(input("enter a number"))
# for i in range(1,11):
#     print(num, "*", i, "=", i*num)
