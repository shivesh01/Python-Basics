a = 2
# id  of (a) is = 4543843008

print("id  of (a) is =", id(a))

a = a + 1

# id of (3) is = 4543843040
print("id of (3) is =", id(3))
print("id of (a) is =", id(a))
# id of (a) is = 4543843040
b = 2

# id of (2) is = 4543843008
print("id of (2) is =", id(2))
print("id of (b) is =", id(b))
# id of (b) is = 4543843008

''' so you can conclude that same value have same id()
as the value increases the id number will also increases 
id number gives memory allocated id...


'''
