# Nested Dictionary Comprehension
dic = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)

}
print(dic)


# Without Dictionary comprehension

dictionary = dict()
for k1 in range(2, 5):
    dictionary[k1] = {k2: k2 * k1 for k2 in range(1, 6)}
print(dictionary)

# OR

dictionary = dict()
for k1 in range(2, 5):
    dictionary[k1] = dict()
    for k2 in range(1, 6):
        dictionary[k1][k2] = k1 * k2
print(dictionary)
