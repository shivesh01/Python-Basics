#This is a outer enclosing function
def print_msg(msg):
    def printer():
        #This is nested function
        print(msg)
    printer()

    #msg is the non local variable function
#excuting function
print_msg("hello")