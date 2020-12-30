marks ={}.fromkeys(['math','english', 'science'],0)

print(marks)

for items in marks.items():
    print(items)

print(list(sorted(marks.keys())))