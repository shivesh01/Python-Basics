# sort lexicographically

my_str = "Hello this Is an Example with cased letters"

words = [word.lower() for word in my_str.split()]

words.sort()

print("The sorted words are:")

for word in words:
    print(word)

'''
In this program, we store the string to be sorted in my_str. Using the split() method the string is converted into a list of words. The split() method splits the string at whitespaces.

The list of words is then sorted using the sort() method, and all the words are displayed
'''