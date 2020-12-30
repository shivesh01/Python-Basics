class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def get_perimeter(self):
        perimeter= self.a + self.b + self.c
        return perimeter


t1=Triangle(9,10,12)

perimeter=t1.get_perimeter()
print('Perimeter of triangle is' ,perimeter)


