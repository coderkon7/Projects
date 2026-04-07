speed = float(input("Type how fast you are going (in km/h): "))
time = float(input("Type how long it took you to reach your destination (in hours): "))


def distance_calculator (speed, time):
    distance=speed*time
    return distance

print("The distance you traveled: ", distance_calculator(speed, time), "km")