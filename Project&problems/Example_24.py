# Convert Decimal to Binary, Octal and Hexadecimal

"""

A number with the prefix 0b is considered binary, 0o is considered octal and 0x as hexadecimal. For example:

"""

dec = int(input(" Enter a number"))

print("The decimal value of ", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal")
print(hex(dec), "in hexadecimal")