class Circle(object):
    def __init__(self, radius):
        self.r = radius
    
    def area(self):
        return 3.14 * self.r * self.r

circle = Circle(2)
print(circle.r)
print(circle.area())
