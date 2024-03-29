class Restaurant:
    """A class to model a restaurant"""
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"Welcome to {self.name} restaurant")
        print(f"We are a {self.type} restaurant")
        
    def open_restaurant(self):
        print(f"{self.name} will open shortly.")
        
    def set_number_served(self, clients):
        self.number_served = clients
        return self.number_served
        
#Creating one instance and printing out the values
restaurant1 = Restaurant("La Pupuseria", "Salvadorian")

print(f'''{restaurant1.name}
{restaurant1.type}''')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print()

#Creating second instance and printing out the values
restaurant2 = Restaurant("La Taqueria", "Mexicana")

print(f'''{restaurant2.name}
{restaurant2.type}''')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

print()

#Creating third instance and printing out the values
restaurant3 = Restaurant("La Tamaleria", "Salvadorian")

print(f'''{restaurant3.name}
{restaurant3.type}''')
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

#Creating fourth instance
restaurant4 = Restaurant("La Taqueria", "Mexicana")
print(restaurant4.set_number_served(56))

class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ["Chocolate", "Vainilla", "Strawberry"]
        
    def display_flavors(self):
        print(self.flavors)
        
icecream = IceCreamStand("Jaime", "Garcia")
icecream.display_flavors()