# Display the powers of 2

terms = int(input("enter a number"))

result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:", terms)
for i in range(terms):
    print("2 raised to power", i, "is", result[i])