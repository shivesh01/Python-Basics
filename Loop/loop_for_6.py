number =int(input("Enter an integer:"))

# Range(0,11) here 11 is excluded
for count in range(1,11):
    product = number * count
    print(number,"*",count,"=",product)
