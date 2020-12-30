import re
pattern = '^a...s$'
test_string = 'abyss'

#The re.findall() method returns a list of strings containing all matches.
result = re.match(pattern,test_string)

if result:
    print("Search Successful.")
else:
    print("Search unsuccessful.")