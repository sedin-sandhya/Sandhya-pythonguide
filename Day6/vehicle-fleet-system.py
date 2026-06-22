#  Vehicle (base) defines trip_summary(). 
# Child classes Car, Bike, Auto each override fare(distance) with their own base + per-km formula. 
# Calling v.trip_summary() automatically uses the correct child fare() -- polymorphism in action. 
# This is how Ola and Uber switch between vehicle types in their pricing engine.
# Base Vehicle class. Child classes Car, Bike, Auto each override fare(). 
# trip_summary() defined once in Vehicle

class Vehicle:

    def __init__(self, vehicle_no, driver):
        self.vehicle_no = vehicle_no
        self.driver = driver

    def fare(self, distance):
        return 0
    
    def trip_summary(self, distance):
        return (
            f"""Driver : {self.driver}
                Vehicle: {self.vehicle_no}
                Distance: {distance} km
                Fare: ₹{self.fare(distance)}
            """
        )


class Car(Vehicle):

    def fare(self, distance):
        return 50 + distance * 15
    
class Bike(Vehicle):

    def fare(self, distance):
        return 20 + distance * 8
    
class Auto(Vehicle):

    def fare(self, distance):
        return 30 + distance * 12
    
car = Car(
    "TN0564",
    "Sandhya"
    )

bike = Bike(
    "TN8967",
    "Arun"
    )

auto = Auto(
    "TN2853",
    "Sanjana"
)

print(car.trip_summary(10))

print(bike.trip_summary(10))

print(auto.trip_summary(10))