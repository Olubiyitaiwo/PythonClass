def get_cube(number):
	return number**3

def give_two_integers(number1,number2):
	number1 = int(input("Enter number: "))

	number2 = int(input("Enter number: "))
	
	for counter in range(number1,number2,2):
		if counter == number2:
			return counter

		
