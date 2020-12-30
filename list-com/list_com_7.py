# Transpose of Matrix using Nested loops
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 7]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

# Now using list_comprehension

matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]

transpose = [[row[i] for row in matrix] for i in range(2)]

print(transpose)

