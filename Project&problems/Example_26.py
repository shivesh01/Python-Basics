# Python program to find H.C.F of two numbers

def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            HCF = i
    return HCF


num1 = 54
num2 = 24

print(" The H.C.F is ", compute_hcf(num1, num2))


# # 2nd Meth is very efficient
#
# def compute_hcf(x, y):
#     while (y):
#         x, y = y, x % y
#     return x
#
#
# num1 = int(input(" enter num1 value"))
# num2 = int(input(" enter num2 value"))
#
# hcf = compute_hcf(num1, num2)
# print("The HCF is", hcf)
