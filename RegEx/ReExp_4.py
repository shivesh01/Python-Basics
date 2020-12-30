import re

string = "Twelve:12 Eighty nine:89 Nine:9."
pattern = '\d+'

#The re.split method splits the string where there is a match and returns a list of strings where the splits have occurred.
result = re.split(pattern,string, 1)
print(result)