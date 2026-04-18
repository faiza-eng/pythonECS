import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

r = float(input("Enter radius: "))
my_circle = Circle(r)
print(f"Area: {my_circle.area():.2f}")
print(f"Circumference: {my_circle.circumference():.2f}")