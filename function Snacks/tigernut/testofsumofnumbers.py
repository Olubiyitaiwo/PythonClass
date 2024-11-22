import unittest
import function_sum_of_even_number

class TestSumOfListOfAFunction(unittest.TestCase):

	def Test_that_grade_exist(self):
		function_sum_of_even_number.get_sum(number)
		number = [1,2,3,4,5]
		function_sum_of_even_number.get_sum(number)

	def function_sum_of_even_number(self):
		number = [1,2,3,4,5]
		actual = function_sum_of_even_number.get_sum(numbers)
		expected = 15
		self.assertEqual(actual,expected)	