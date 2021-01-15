# count each vowel

vowels = "aeiou"

my_str = " Hello, have you tried our tutorial section yet?"

my_str = my_str.casefold()

count = {}.fromkeys(vowels,0)

for char in my_str:
    if char in count:
        count[char] += 1

print(count)


# # 2nd method by list and dictionary comprehension c=
#
# my_str = " Hello i m shivesh"
#
# my_str = my_str.casefold()
#
# count = {x: sum([1 for char in my_str if char == x]) for x in 'aeiou'}
#
# print(count)