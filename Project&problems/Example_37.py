# Transpose a matrix using nested loops

x = [

    [12, 7],
    [4, 5],
    [3, 8]

]

result = [
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i] = x[i][j]

print(result)

#
# '''
#  2nd method Program to transpose a matrix using list comprehension
# '''
#
# x = [
#     [12, 7],
#     [4, 5],
#     [3, 8]
#     ]
#
# result = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
#
# print(result)
