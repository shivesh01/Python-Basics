#Python Decorators

def first(msg):
    print(msg)

first("Hello")

second = first
second("Hello")

#Such functions that take other functions as arguments are also called higher order functions. Here is an example of such a function.

