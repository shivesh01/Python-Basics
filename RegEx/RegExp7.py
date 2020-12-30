import re


# Program to remove all whitespaces
string ='abc 12\de 23 \ f45 6'

pattern = r'\s+'

replace = ""

#The re.subn() is similar to re.sub() expect it returns a tuple of 2 items containing the new string and the number of substitutions made.

new_string =re.subn(pattern, replace, string,1)

print(new_string)