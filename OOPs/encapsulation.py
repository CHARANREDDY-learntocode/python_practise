class Shape:
    _len = 10
    _bre = 0
    
    @property
    def bre(self):
        print('get')
        return self._bre

    @bre.setter
    def bre(self, value):
        print('set')
        self._bre = value
        return self._bre

    @bre.deleter
    def bre(self):
        print('delete')
        del self._bre
        return

    def print_sides(self):
        print(self._len, self._bre)

shp = Shape()
shp.print_sides()
print( shp._len)
print(shp.bre)
shp.bre = 100
print(shp.bre)
del shp.bre
print(shp.bre)


class Sample:
    def __init__(self,a,b):
        self.a = a
        self.__b  = b

    def print_private(self):
        return self.__b

class Derived(Sample):
    def __init__(self, a, b):
        super().__init__(a, b)
    def print_private(self):
        return self.a

samp1 = Sample(10,20)
samp2 = Sample(30,40)
der1 = Derived(60, 80)


print(samp1.print_private())
print(der1.print_private())
print(samp1.__b)
print(der1.a)