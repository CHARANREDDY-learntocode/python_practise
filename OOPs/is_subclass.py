class Shape:
    def __init__(self, name):
        print('In super')
        self.name = name
    
class Circle(Shape):
    def __init__(self, name, radius):
        self.radius = radius
        super().__init__(name)
        print('After executing super')

cir = Circle('circle', 10)
assert not issubclass(Circle, Shape)