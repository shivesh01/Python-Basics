class Complex:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag

    def add(self,number):
        real=self.real + number.real
        imag=self.imag + number.imag
        result=Complex(real,imag)
        return result

n1 = Complex(10,9)
n2 = Complex(-1,5)
result = n1.add(n2)
print("real =",result.real)
print("imag =",result.imag)
