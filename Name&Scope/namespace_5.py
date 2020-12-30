def outer_function():
    global a
    a = 20

    def inner_function():
        global a
        a=30
        print("a  =",a)
    inner_function()
    print("a  =",a)

a=10
outer_function()
print('a  =',a)

#all references and assignments are to the global a due to the use of keyword global