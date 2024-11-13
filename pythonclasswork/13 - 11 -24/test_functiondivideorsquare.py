import unittest
import functiondivideorsquare


class TestDivideOrSquareFunction(unittest.TestCase):
	def test_the_product_value_exist(self):
		functiondivideorsquare.divide_or_square(3)

	def test_the_division_or_square(self):
		actual = functiondivideorsquare.divide_or_square(5)
		expected = 25
		self.assertEqual(actual, expected)
		actual = functiondivideorsquare.divide_or_square(5)
		expected = 5
		self.assertEqual(actual, expected)


	