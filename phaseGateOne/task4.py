"""
prompt user to enter a number between 1 to 10
collect input
save as userinput
using a loop generate a question for each of the number inputed 
for each question give it a starting value and an ending value
display result
"""

import random

result = 0
user_input = int(input("Enter number; "))

for count in range(1,11):
	result1 = random.randrange(1,10)
print(result1)