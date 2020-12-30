import numpy as np

# Slicing of the multi_dim matrix

A = np.array([[1, 4, 5, 12, 14],
             [-5, 8, 9, 0, 17],
             [-6, 7, 11, 19, 21]])

print(A[:2, :4], "\n")

print(A[:1, ], "\n")

print(A[:, 2], "\n")

print(A[:, 2:5], "\n")