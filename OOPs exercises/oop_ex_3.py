class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    def info(self):
        print("Vehicle name:",self.name,"Speed:",self.max_speed,"Mileage:",self.mileage)
        
class Bus(Vehicle):

    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)
school_bus = Bus('School Volvo',180,12)
school_bus.info()