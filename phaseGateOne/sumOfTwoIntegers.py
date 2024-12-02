"""
prompt a user to enter a integer
collect the integer
save as userInput1
prompt a user to enter another integer
collect the integer
save as userInput2

sum userInput1 and  userInput1 

compare if the sum equals userInput1 and  userinput1 
print True
else 
print False
"""


user_input1 = int(input("Enter a number: "))

user_input2 = int(input("Enter another number: "))

sum = user_input1 + user_input2

if(user_input1 + user_input2 == sum):
	print(True)
else:
	print(False)



