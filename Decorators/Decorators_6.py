def works_for_all(func):
    def inner(*args,**kwargs):
        print("I can decorate any function")
        return func(*args,**Kwargs)
    return inner

#, args will be the tuple of positional arguments and kwargs will be the dictionary of keyword arguments. An example of such a decorator will be: