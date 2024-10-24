number = int(input('Enter a number: '))

first_digit = number// 100

number2 = number // 10
second_number = number2 % 10

third_number = number % 10

sum = first_digit + second_number + third_number 
print('Sum of digits:', sum)
