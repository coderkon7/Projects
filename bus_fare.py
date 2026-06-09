class Vehicle():

    def __init__(self, seating):
        self.seating = seating
    
    def display_fare(self):
        fare = self.seating*100 + 0.10*(self.seating*100)
        print("Default fare for vehicles: $", fare)

class Bus(Vehicle):

    def __init__(self, seating):
        super().__init__(seating)
        self.seating = seating
    

    def fare(self, seating):
        self.seating = seating
        fare = self.seating*100 + 0.10*(self.seating*100)
        return fare

car1 = Vehicle(6)
bus1 = Bus(50)
car1.display_fare()
bus1.display_fare()