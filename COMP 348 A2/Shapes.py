import math

class Shape:
    shape_count = 0
    
    def __init__(self):
        Shape.shape_count +=1
        
    def print(self):
        shape_name = self.__class__.__name__
        return f"{shape_name}, perimeter: {self.perimeter()}, area: {self.area()}"
    def perimeter(self):
        return None
    def area(self):
        return None  
    def __eq__(self, other):
        if isinstance(other, Shape):
            return vars(self) == vars(other)
        return False

    def __hash__(self):
        return hash(tuple(sorted(vars(self).items())))

class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius  
    def perimeter(self):
        return 2 * math.pi * self.radius
    def area(self):
        return 2 * math.pi * self.radius * self.radius
    def print(self):
        shape_name = self.__class__.__name__
        return f"{shape_name}, perimeter: {self.perimeter()}, area: {self.area()}"
    
class Ellipse(Shape):
    def __init__(self, a, b):
        super().__init__()
        self.a = max(a,b)
        self.b = min(a,b)
    def area(self):
        return math.pi * self.a * self.b
    def eccentricity(self):
        return math.sqrt(self.a **2 - self.b **2)
    def print(self):
        shape_name = self.__class__.__name__
        return f"{shape_name}, area: {self.area()}, linear eccentricity: {self.eccentricity()}"

class Rhombus(Shape):
    def __init__(self, d1,d2):
        super().__init__()
        self.d1 = d1
        self.d2 = d2
    def perimeter(self):
        return 4 * math.sqrt((self.d1 ** 2 + self.d2 ** 2) / 2)
    def area(self):
        return (self.d1 * self.d2) /2
    def side(self):
        return (math.sqrt(self.d1 **2 + self.d2 **2)) /2
    def inradius(self):
        return (self.d1 * self.d2) / (2 * math.sqrt(self.d1 ** 2 + self.d2 **2))
    def print(self):
        shape_name = self.__class__.__name__
        return f"{shape_name}, perimeter: {self.perimeter()}, area: {self.area()}, side: {self.side()}, in-radius: {self.inradius()}"
    
    

