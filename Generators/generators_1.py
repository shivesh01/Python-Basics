#The difference is that while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.
def my_gen():
    n=1
    print("This is printed first")
    yield n

    n += 1
    print("This is printed second")
    yield n

    n += 1
    print("This is printed last")
    yield n