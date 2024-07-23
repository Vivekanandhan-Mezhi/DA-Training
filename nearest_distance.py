# Emergency Response System
# Scenario: You are developing an emergency response system for a city. 
# You need to dispatch the nearest available emergency vehicle to the location of an incident. 
# Vehicles are dispatched based on their distance to the incident and their availability status.

# Question: Write a function that takes a list of vehicles 
# (each vehicle is represented as a tuple of (vehicle_id, location_x, location_y, available)) 
# and the location of the incident, and returns the ID of the nearest available vehicle.

import math
vehicle_list=[(1,12.5,13.5,True),(2, 3, 6, False), (3, 15.5, 15, True), (4, 0, 0, True)]
incident_location = {'x': 15,
                     'y': 14}

def find_nearest_vechile(vehicle_list, incident_location):
    veh_id = 0
    near_distance = float('inf')
    for vehicle in vehicle_list:
        if vehicle[3]==True:
            distance = math.sqrt(((vehicle[1]-incident_location['x'])**2) + ((vehicle[2]-incident_location['y'])**2))
            if distance<near_distance:
                near_distance = distance
                veh_id = vehicle[0]
    return veh_id

print(find_nearest_vechile(vehicle_list, incident_location))    
        





