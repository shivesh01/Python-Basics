import re


# Program to remove all whitespaces
string ='abc 12\de 23 \ f45 6'

pattern = '\s+'

replace = ""

new_string =re.sub(pattern, replace, string)

print(new_string)