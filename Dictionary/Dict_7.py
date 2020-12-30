synonyms = {"mountain": "peak", "forest": "jungle"}
print("1.", synonyms["mountain"])

# add item
synonyms["terrain"] = "land"
print("2", synonyms)

# remove item
synonyms.pop("forest")
print("3", synonyms)

# clear
synonyms.clear()
print(synonyms)

# del dict
# del synonyms
# print(synonyms)

