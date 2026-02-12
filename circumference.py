def circ(radius,pi=3.14):
    circ = 2*radius*pi
    print(f"The approximate circumference of a circle with a radius of {radius} cm is {circ} cm")

circ(int(input("Type the radius of the circle (in centimeters): ")))