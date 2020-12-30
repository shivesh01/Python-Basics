import re
string = "Python is fun"

#check if  'python' is at the beginning
match = re.search('\APython', string)

if match:
    print("Pattern found inside the string")
else:
    print("Python is not found")