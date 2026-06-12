"""Train Ticket Fare Calculator: 

Take passenger age, class (Sleeper/3AC/2AC), and distance (km). Apply senior citizen discount (60+), children's fare (under 12), and calculate GST. Print a ticket summary. 

 

Passenger name: Rahul 
Age: 63 | Class: 3AC | Distance: 850 km 
--- 
Base fare: ₹1,105.00 
Sr. discount: - ₹110.50 (10%) 
GST (5%): + ₹49.73 
Total: ₹1,044.23  
"Booking confirmed for Rahul — Bon voyage!"  """

name = input("Passenger name: ")
age = int(input("Enter the age: "))
train_class = input("Enter the class(Sleeper/3AC/2AC): ")
distance = input("Enter the distance in km: ")
distance.replace(" ", "")
new_distance = int(distance[:-2])
base_fare = 0
discount = 0
fare_per_km = {
    "Sleeper" : 1.0,
    "3AC" : 1.5,
    "2AC" : 2
}

if train_class in fare_per_km:
    base_fare = new_distance * fare_per_km[train_class]
    print("Base fare: Rs", base_fare)

if age > 60 or age < 12:
    discount = base_fare/10
    print(f"Discount: Rs + {discount:.2f} (10%)")

total_fare = base_fare - discount
gst = total_fare/20

print(f"GST (5%): + Rs{gst:.2f}")
print(f"Total: Rs{total_fare + gst:.2f}")
print("Booking confirmed for " + name + " -- Bon voyage!!")

