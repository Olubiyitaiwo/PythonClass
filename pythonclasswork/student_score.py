student_scores = int(input('Enter scores: '))

for student in range(0,15):
	student_scores = input('Enter scores: ')
	

	if student_scores > 45:
		print('Pass')

	elif student_scores < 45:
		print('Fail')

	else:
		print('Wronge input')


