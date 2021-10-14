class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        '''assuming the given values are sides of right angled traingle.
        a is base and b is height'''
        return (1/2)*self.a*self.b

    def perimeter(self):
        '''Return the perimeter of triangle'''
        return self.a + self.b + self.c

    def __str__(self):
        '''return the sides of triangle'''
        return f'The sides are {self.a} {self.b} {self.c}'

trng = Triangle(10, 20, 30)
print('Perimeter: ', trng.perimeter())
print('Area: ', trng.area())

