import re


# Program to remove all whitespaces
string ='abc 12\de 23 \ f45 6'

pattern = r'\s+'

replace = ""

new_string =re.sub(pattern, replace, string,1)

print(new_string)