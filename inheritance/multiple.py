# Question:

# You are designing a system to model vehicles with different propulsion types and fuel sources. Create a set of classes representing vehicles, where
#  each vehicle can have multiple characteristics. Use multiple inheritance to model the different aspects of a vehicle.

# Create a base class called Vehicle with attributes make, model, and year. Include a method display_info() to display information about the vehicle.

# Create a class called Engine that represents the propulsion system of a vehicle. It should have attributes fuel_type and horsepower. Include a
#  method start_engine() that prints a message indicating that the engine is starting.

# Create a class called FuelTank that represents the fuel source of a vehicle. It should have attributes fuel_capacity and current_fuel_level. 
# Include a method refuel(amount) that refuels the vehicle by the specified amount.

# Finally, create a class called Car that inherits from both Vehicle, Engine, and FuelTank. The Car class should have additional attributes such as
#  num_doors and color. Include a method drive() that prints a message indicating that the car is being driven.

# Demonstrate the usage of these classes by creating an instance of the Car class, displaying its information, starting the engine, driving it, and
#  refueling it.

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"make: {self.make} model: {self.model} year: {self.year}")

class Engine:
    def __init__(self,fuel_type,horsepower):
        self.fuel_type = fuel_type
        self.horsepower = horsepower

    def start_engine(self):
        print(f"the engine is starting")

class Fuel_tank:
    def __init__(self,fuel_capacity,current_fuel_level):
        self.fuel_capacity = fuel_capacity
        self.current_fuel_level = current_fuel_level
    
    def refuel(self,amount):
        if amount>0:
            print(f"the amount is {amount} litres")
            print(f"the fuel amount is {self.current_fuel_level}")
            self.current_fuel_level += amount
        else:
            print(f"Invalid amount")

class Car(Vehicle, Engine, Fuel_tank):
    def __init__(self, make, model, year, fuel_type, horsepower, fuel_capacity, num_doors, color):
        Vehicle.__init__(self,make, model, year)
        Engine.__init__(self,fuel_type,horsepower)
        Fuel_tank.__init__(self,fuel_capacity,fuel_capacity)
        self.num_doors = num_doors
        self.color = color

    def drive(self):
        print(f"The {self.color} car is being driven.")


car = Car('Maruti','VXI',15,'petrol',1200,50,4,'White')

car.display_info()
car.start_engine()
car.drive()
car.refuel(5)
car .refuel(10)


