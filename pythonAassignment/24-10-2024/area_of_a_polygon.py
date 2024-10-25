import math   
length = int(input('Enter length: '))

side = int(input('Enter side: '))

area = (side * length**2)/(4* math.tan(3.147/side))
print('Area: ',area)
