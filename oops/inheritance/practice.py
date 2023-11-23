# Question:
# Suppose you have a class called Vehicle with attributes make and model, and a method display_info() that prints information about the vehicle.
# Now, you want to create a subclass called Car that inherits from the Vehicle class. The Car class should have an additional attribute num_doors
# and a method display_car_info() that displays information about the car, including the number of doors.

# Write the Vehicle class and the Car subclass in Python, and demonstrate how you would create an instance of the Car class and call its methods.

class vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model
    
    def display_info(self):
        print(f"make:{self.make} model:{self.model}")

class car(vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_car_info(self):
        
        super().display_info()
        print(f"num_doors: {self.num_doors}")

my_car = car("suzuki","vxi",4)
my_car.display_car_info()