"""
using a match case
make    Sunday = 0
        Tuesday = 1
	Wednessday = 2
	Thursday = 3
	Friday = 4
	Saturday = 5
	Sunday = 6
prompt user to enter number in range 1 to 6
if userinput = and of the days stated above
print of the date
else
display invalid input
"""

user_input = int(input("Enter a number between 0 to 6 \n0. Sunday\n 1. Monday\n 2.Tuesday\n3.Wednessday\n4.Thursady\n5.Frinday\n6. Saturday"))

match(user_input):
	case 0:
		print("Sunday")
	case 1:
		print("Monday")
	case 2:
		print("Tuesday")
	case 3:
		print("Wednessday")
	case 4:
		print("Thursady")
	case 5:
		print("Friday")
	case 6:
		print("Saturday")

	if(user_input == case 3):
		print("display 3 day left to the end of the week")
	
