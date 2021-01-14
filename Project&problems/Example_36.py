# Add two matrices using nested loop

x = [
    [12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]
]

y = [
    [5, 8, 1],
    [6, 7, 3],
    [4, 5, 9]
]

result = [
    [0, 0, 0]
    , [0, 0, 0]
    , [0, 0, 0]
]

print('this only adds rows of X+Y becomes 6 rows')
print(x + y)

print("Actual addition")

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
print(result)
