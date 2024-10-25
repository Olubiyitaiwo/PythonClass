import math

latitude_coordination_one = float(input('Enter latitude 1: '))
longitude_coordination_one = float(input('Enter longitude 1: '))
latitude_coordination_two = float(input('Enter latitude 2: '))
longitude_coordination_two = float(input('Enter longitude 2: '))



latitude_coordination_one = math.radians(latitude_coordination_one)
longitude_coordination_one = math.radian(longitude_coordination_one)

latitude_coordination_two = math.radians(latitude_coordination_two)
longitude_coordination_two = math.radians(longitude_coordination_two)

distance = 6371.01*math.arcos(math.sin(latitude_coordination_one)*math.sin(latitude_coordination_two)+math.cos(longitude_coordination_one)*math.cos(longitude_coordination_two)*math.cos(longitude_coordination_one - longitude_coordination_two))

print(distance)