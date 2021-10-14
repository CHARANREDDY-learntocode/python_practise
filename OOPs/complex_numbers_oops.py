class Custom_Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __add__(self, other):
        real = self.a + other.a
        imag = self.b + other.b
        return Custom_Complex(real, imag)
    
    def __sub__(self, other):
        real = self.a - other.a
        imag = self.b - other.b
        return Custom_Complex(real, imag)

    def __mul__(self, other):
        real = (self.a * other.a) - (self.b * other.b)
        imag = (self.a * other.b) + (self.b * other.a)
        return Custom_Complex(real, imag)
    def __truediv__(self, other):
        real = ((self.a * other.a) + (self.b + other.b))/(other.a**2 + other.b**2)
        imag = ((self.b * other.a) - (self.a * other.b))/(other.a**2 + other.b**2)
        return Custom_Complex(real, imag)

    def __str__(self):
        return f'{self.a}+{self.b}i' if self.b>0 else f'{self.a}{self.b}i'

num1 = Custom_Complex(1, 2)
num2 = Custom_Complex(3, 4)
print(num1, num2)
print('Add: ', num1+num2)
print('Sub: ', num1-num2)
print('Mul: ', num1*num2)
print('Div: ', num1/num2)