"""
prompt a user to enter an integer between 1 and 1000
collect input
save as user_input
get first digit as user_input//10
save as fristdigit
get second digit as fristdigit//10
save as fristdigit
"""
user_input = int(input("Enter a number beteew 0 - 1000: "))

first_digit = user_input//10

second_digit = first_digit//10
second_digit2 =second_digit%10

third_digit1 = second_digit2//100
third_digit2 = third_digit1%100

fourth_digit = third_digit2%10

print(first_digit + second_digit2 + third_digit2 + fourth_digit)



