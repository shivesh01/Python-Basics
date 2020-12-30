class first():
    def sum(self,a,b):
        c=a+b;
        return c;
class second():
    def sub(self,a,b):
        c=a-b;
        return c;
class third(first,second):
    pass

obj1=third()
print(obj1.sub(2,4))
print(obj1.sum(2,4))