import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)
    
circle_1 = Circle(42)
circle_2 = Circle(7)

print(circle_1)