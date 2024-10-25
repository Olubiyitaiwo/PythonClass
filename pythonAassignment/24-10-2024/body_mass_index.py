weight = float(input('Enter weight in pounds: '))
weight_in_kilogram = float(weight * 0.45359237)

height = float(input('Enter height in inches: '))
height_in_meter = height * 0.0254

square_of_height = float(height_in_meter*height_in_meter)

body_mass_index = weight_in_kilogram/square_of_height
print('Body Mass Index: ', body_mass_index)



