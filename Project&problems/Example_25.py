# Ascii value

input = input("enter a chararcter or number")

if type(input) == str:

    chr = str(input)

    print(f"The Ascii value of {chr} is ", ord(chr))

# There is irregularity of character in ascii value like for number 89 there is not a assigned a character but it is assigned for operation
# so it will give error

elif type(input) == int:

    ord = int(input)

    print(f"The character is {ord} represent", chr(ord))

else:
    print(" please try again")
