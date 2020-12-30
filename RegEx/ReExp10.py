import re
string = '\n and \r are escape sequences.'

#Raw string using r prefix
result = re.findall(r'[\n\r]',string)
print(result)
