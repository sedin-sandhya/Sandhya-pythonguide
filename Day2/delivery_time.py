"""Delivery Time Estimator: 

Take distance (km), weather (clear/rain/storm), and time of day (peak/normal) as input. Calculate estimated delivery time and show a status message like Zomato does. 

Distance: 4.5 km 
Weather (clear/rain/storm): rain 
Time (peak/normal): peak 
--- 
Estimated delivery: 42 mins 
Status: "Running slightly late due to rain" """ 

wtime = {"clear" : 5, "rain" : 10, "storm" : 15}
hours = {"peak" : 10, "normal" : 5}
dis = input("Distance: ")
weather = input("Weather(clear/rain/storm): ")
time = input("Time (peak/normal): ")
dis.replace(" ", "")
dist = int(dis[:-2])
t = 0

if weather in wtime:
    t += wtime[weather]
if time in hours:
    t += hours[time]

tot_time = dist * t
print("Estimated delivery:", tot_time, "mins")

if weather == "clear":
    print('Status: "Your product will be delivered on time"')
elif weather == "rain":
    print('Status: "Running slightly late due to rain"')
elif weather == "storm":
    print('Status: "Running late due to storm, Sorry for the inconvenience"')