class first():
    def mul(self,a,b):
        c=a*b;
        return c;
class second(first):
    pass
obj1=second()
print(obj1.mul(9,9))