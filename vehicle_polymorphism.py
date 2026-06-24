class BMW():
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed
    
    def getFuelType(self):
        print(f"Fuel Type: {self.fuel_type}")
    
    def getMaxSpeed(self):
        print(f"Max Speed: {self.max_speed}")



class Ferrari():
    def __init__(self, fuel_type, max_speed):
        self.fuel_type = fuel_type
        self.max_speed = max_speed
    
    def getFuelType(self):
        print(f"Fuel Type: {self.fuel_type}")
    
    def getMaxSpeed(self):
        print(f"Max Speed: {self.max_speed} km/h")

car1 = BMW("Gasoline", 170)
car2 = Ferrari("Gasonline", 320)

for vehicle in [car1,car2]:
    vehicle.getFuelType()
    vehicle.getMaxSpeed()