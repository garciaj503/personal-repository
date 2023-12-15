class Car:
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formated descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        """Reject the change if it attempts to roll the odomter back."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        
        else:
            print("You can't roll back an odometer!")
    
my_new_car = Car("Audi", "A4", 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

print()

#Updating an attribute's value directly
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

print()

#mModifying an Attribute's Value through a method
my_new_car.update_odometer(90897)
my_new_car.read_odometer()