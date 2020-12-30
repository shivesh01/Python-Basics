#Find the sum of number from  1 to 100?
#1. By using for loop : Done
#2. By using while loop : Done

# sum = 0
#
# # i iterating over again and again till 101 it's value is added to sum
# for i in range(1,101):
#
#     sum = sum + i
#
# print("The sum of numbers between 1 to 100 :",sum)



sum =0
count = 0
while count<=100:
    sum = sum + count
    count = count + 1
print("The sum of numbers between 1 to 100 :",sum)