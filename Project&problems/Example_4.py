# Area of triangle
import math


def triangle(a, b, c):
    s = (a + b + c) / 2
    return float(math.sqrt(s*((s - a) * (s - b) * (s - c))))


a = int(input(" length of side a"))
b = int(input(" length of side b"))
c = int(input(" length of side c"))

print("Triangle whose side a={0} b={1} and c={2}     area =".format(a, b, c), float(triangle(a,b,c)))
