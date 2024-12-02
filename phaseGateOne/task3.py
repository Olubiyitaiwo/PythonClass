"""
prompt a user to enter three integers
collect the integers
save as number1
save as number2
save as number3
compare each of the integers against themselves as:
if number1 is less than number2 and number2 is less than number 3
print number1,number2,number3

else if number2 is less than number1 AND number1 is less than number 3
print number1,number2,number3

else if number3 is less than number1 AND number1 is less than number 2
print number3,number1,number2
"""

number1 = int(input("Enter number: "))
number2 = int(input("Enter number: "))
number3 = int(input("Enter number: "))

if(number1 < number2 & number2 < number3):
	print(number1,number2,number3)

	if(number2 < number1 & number1 < number3):
		print(number2,number1,number3)

		if(number3 < number2 & number2 < number1):
			print(number3,number2,number1)