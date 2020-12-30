def main(str):
    print(" Your entered string \n",str)
    print(" your string contains alphanumeric\digits",str.isalnum())
    print(" your string contains all alphabet ",str.isalpha())
    print(" your string contains all digits",str.isdigit())
    print(" your string contains all uppercase",str.isupper())
    print(" your string contains alll lowercase",str.islower())

main("welcomeabroad")
main("123456789")
main("HELLO")
main("world")

