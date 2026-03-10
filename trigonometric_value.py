import math
try:
    num = float(input("Enter the number you wish to find the sin, cos, and tan values for (measured in radians): "))
    print(f"The sine of {num} radians : ", math.sin(num), f"\nThe cosine of {num} radians : ", math.cos(num), f"\nThe tangent of {num} radians : ", math.tan(num))
except ValueError:
    print("Error: Please make sure you enter a valid number with no spaces or letters.")