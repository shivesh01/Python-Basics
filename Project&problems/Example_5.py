# Quadratic roots

import cmath

a = int(input("Enter the value of a"))
b = int(input("Enter the value of b"))
c = int(input("Enter the value of c"))

d = (b**2)-(4*a*c)

sol1 = (-b + cmath.sqrt(d))/2*a
sol2 = (-b - cmath.sqrt(d))/2*a

print(f"Roots of the quadratic are {sol1} and {sol2}")
