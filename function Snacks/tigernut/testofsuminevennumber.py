import unittest
import functionforsuminevennumber

class TestOfSumInAList(unittest.TestCase):
	def test_that_even_number_exists(self):
		functionforsuminevennumber.get_sum(3)

	def test_sum_of_even_number(self):
		actual = functionforsuminevennumber.get_sum({1,2,3,4,5,6})

		expected = 12

	self.assertEqual(actual,expected)
"""""
	def test_to_get_vowel(self):
		actual = functionforsuminevennumber.get_vowel("pythonissweet") 

		expected = 4

	self.assertEqual(actual,expected)
"""""
	def test_to_get_vowel(self):
		actual = functionforsuminevennumber.get_missing_value([1,2,3,4,5]) 

		expected = 60

	self.assertEqual(actual,expected)
"""""
	def test_to_get_merge_values(self):

		number1 =[1,2,3,4,5]
		number2 =[6,7,8,9]
		actual = functionforsuminevennumber.merge_value(number1,number2) 

		expected = [1,2,3,4,5,6,7,8,9]

	self.assertEqual(actual,expected)