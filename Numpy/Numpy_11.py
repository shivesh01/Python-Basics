import numpy as np

#Slicing of the matrix

'''
Index Rule applies here too!
'''

letters  = np.array([1,4,5,12,-5,8,9,0,-6,7,11,19])

# 3rd to 5th elements
print(letters[2:5])

# 1st to 4th elements
print(letters[:-5])

# 6th to last elements
print(letters[5:])

# 1st to last elements
print(letters[:])

# reversing a list
print(letters[::-1])
