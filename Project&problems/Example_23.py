# Find the numbers divisible by another number from a list

num = int(input("Enter a number"))

my_list = [12, 65, 54, 39, 102, 339, 221]

result = list(filter(lambda x: (x % num == 0), my_list))

print(f"Numbers divisible by {num} are", result)

##  Find factors

# num = int(input(" Enter a num to find it's factor"))
#
#
# for i in range(1, num):
#     if num % i == 0:
#         print(f"{num} is divisible by ", i)
