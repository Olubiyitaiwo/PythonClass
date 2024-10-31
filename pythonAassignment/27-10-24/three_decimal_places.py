
number = float(input("Enter number: "))

whole_number = number * 1000
decimal_number = number/1000

number2 = float(input("Enter another number: "))
       
whole_number2 = number2*1000
decimal_number2 = number2/1000

if(decimal_number == decimal_number2):
 print("Same")
elif(decimal_number != decimal_number2):
 print("Not the same")
 