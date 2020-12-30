def outer_function():
    b=20
    def inner_fun():
        c=30
a = 10

""" 
    when we are in outer function
    a is global namespace 
    b is local namespace
    c is nested local namespace 
"""
'''
    when we are in inner function
    c is the local namespace 
    b is non-local namespace
    a is the global namespace
'''

(' \n'
 'If we try to assign as a value to b,\n'
 'A new variable b is created in the local namespace which is different than the nonlocal b.\n'
 'The same thing happens when we assign a value to a.\n')