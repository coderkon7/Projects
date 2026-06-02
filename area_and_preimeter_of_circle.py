class circle:

    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        area = 3.14*radius.radius*radius.radius
        return area
    def perimeter(self):
        perimeter = 2*3.14*radius.radius
        return perimeter


radius = circle(float(input("Enter the radius of the circle (in inches) to get the perimeter and area of the circle: ")))
print("Area (in inches): ", radius.area())
print("Perimeter (in inches): ", radius.perimeter())