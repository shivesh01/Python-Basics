try:
    num=int(input(" Enter a number"))
    assert num%5==0
except:
    print("num is not divisible by 5")
else:
    print("num is  divisible by 5", num)