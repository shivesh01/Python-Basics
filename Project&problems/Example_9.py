# convert celsius to Fahrenheit

celsius = float(input("Enter temp in celsius"))

conv_factor = 9/5

fahren = (celsius * conv_factor) + 32

print("{0} Celsius temp is equal to {1} Fahrenheit".format(celsius,fahren))
