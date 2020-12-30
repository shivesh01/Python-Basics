#Generators can be implemented in a clear and concise way as compared to their iterator class counterpart.

# class powtwo:
#     def __init__(self, max=0):
#         self.n = 0
#         self.max = max
#
#     def __iter__(self):
#         return self
#
#     def _next_(self):
#         if self.n>self.max:
#             raise StopIteration
#
#         result = 2 ** self.n
#         self.n += 1
#         return result


def powtwogen(max=0):
    n=0
    while n < max:
        yield 2 ** n
        n +=1
        