# Frozenset

A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

print(A.intersection(B))

print(A.difference(B))

print(A.symmetric_difference(B))

print(A.isdisjoint(B))

print(A.issuperset(B))

print(A.difference(B))

print(A | B)

# its elements cannot be changed once assigned.

# copy(), difference(), intersection(), isdisjoint(), issubset(), issuperset(), symmetric_difference() and union()
