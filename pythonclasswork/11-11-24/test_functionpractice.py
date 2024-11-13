from unittest import TestCase
import functionpractice


class TestCubeFunction(TestCase):
	def test_that_cube_function_exists(self):
		functionpractice.get_cube(3)

	def test_cube_function_returns_correct_value(self):
		actual = functionpractice.get_cube(3)
		expected = 27
		self.assertEqual(actual, expected)
		actual = functionpractice.get_cube(10)
		expected = 1000
		self.assertEqual(actual, expected)

class TestMultipleFunction(TestCase):
	def test_that_mutiple_function_works(check):
		actual = functionpractice.give_two_integers(2,3)
		expected = 6
		check.assertEqual(actual,expected)

	#def test_that_multiple_function_works():

	