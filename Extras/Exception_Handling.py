import sys                          # import module sys to get the type of exception

randomlist = ['a',0,2]

for entry in randomlist:
    try:                            #try block handles the exception
        print("The entry is ", entry )
        r=1/int(entry)
        break
    except:                         #except block catches exception
        print("Oops!",sys.exc_info()[0],"occured.")     #the exception using the exc_info() function inside sys module
        print("Next entry.")
        print()
print("The reciprocal of", entry,"is", r)