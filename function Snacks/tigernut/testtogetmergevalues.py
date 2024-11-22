import unittest
import functionmergevariable

class TestOfSumInAList(unittest.TestCase):
	def test_to_get_merge_values(self):
			number1 =[1,2,3,4,5]
			number2 =[6,7,8]

			functionmergevariable.merge_value(number1, number2)

			actual = functionmergevariable.merge_value([number1] + [number2]) 

			expected = [1,2,3,4,5,6,7,8]

			self.assertEqual(actual,expected)

	def test_to_get_vowel(self):
		number = [1,2,3,4,5]
		actual = functionmergevariable.get_sum(number) 
	
		expected = 60

		self.assertEqual(actual,expected)  

	def test_to_check_palindrom(self):
		actual = functionmergevariable.get_palindrom(madam)
		expected = true
		self.assertEqual(actual, expected)

	def test_to_check_average_of_a_list(self):
		number = [10,20,30,40]
		actual = functionmergevariable.get_average(number)
		expected = 25
		self.assertEqual(actual, expected)

	def test_to_check_average_of_a_list(self):
		actual = functionmergevariable.get_reverse_string(hello)
		expected = olleh
		self.assertEqual(actual, expected)


def test_sum_of_even_number(self):
		actual = 	functionforsuminevennumber.get_sum({1,2,3,4,5,6})

		expected = 12