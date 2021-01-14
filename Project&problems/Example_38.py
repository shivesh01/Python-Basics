# # Program to multiply two matrices using nested loops
#
# # 3 * 3 matrix
#
# # method 1 by nested loops
#
# x = [
#     [12, 7, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# y = [
#     [5, 8, 1, 2],
#     [6, 7, 3, 0],
#     [4, 5, 9, 1]
# ]
#
# result = [
#     [0, 0, 0, 0],
#     [0, 0, 0, 0],
#     [0, 0, 0, 0]
# ]
#
# for i in range(len(x)):
#
#     for j in range(len(y[0])):
#
#         for k in range(len(y)):
#             result[i][j] += x[i][k] * y[k][j]
# for r in result:
#     print(r)

"""
For larger matrix operations we recommend optimized software packages like NumPy which is several (in the order of 1000) times faster than the above code.
"""

# method 2 nested lists

x = [
    [12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]
]

y = [
    [5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]
]

result = [[sum(a * b for a, b in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]

print(result)
