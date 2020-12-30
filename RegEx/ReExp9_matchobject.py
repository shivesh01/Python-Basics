import  re

string = '39801 356, 2102 1111'

#Three digit numbers are followed by space followed by two digits number
pattern = '(\d{3}) (\d{2})'

match = re.search(pattern, string)

if match:
    print(match.group())
    print(match.group(1,2))
    print(match.start())
    print(match.end())
    print(match.span())
    print(match.re)

else:
    print("pattern is not found")