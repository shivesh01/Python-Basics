# Python matrix

A = [[1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

print("A =", A)
print("A[1] =", A[1])
print("A[1][2] =",  A[1][2])
print("A[0][-1] =", A[0][-1])

column = []
for row in A:
    column.append(row[2])

print("3rd column =", column)