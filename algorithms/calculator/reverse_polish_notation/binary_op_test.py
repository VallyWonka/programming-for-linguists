"""
Programming for linguists

Tests for Binary operators
"""
import unittest

from algorithms.calculator.reverse_polish_notation import Digit
from algorithms.calculator.reverse_polish_notation.binary_op import Plus, Minus, Multiplier, Divider, Power


# @unittest.skip('There is not implementation of Operators yet')
class BinaryOpImplementationTestCase(unittest.TestCase):
    """
    Test cases for Binary operators
    """
    def test_plus(self):
        """
        Test case to check Plus operator
        """
        argument_1 = Digit(1)
        argument_2 = Digit(2)
        operator = Plus()

        self.assertEqual(operator(argument_1, argument_2).digit, operator(argument_2, argument_1).digit)
        self.assertEqual(operator(argument_2, argument_1).digit, argument_1.digit + argument_2.digit)

    def test_minus(self):
        """
        Test case to check Minus operator
        """
        argument_1 = Digit(1)
        argument_2 = Digit(2)
        operator = Minus()

        self.assertNotEqual(operator(argument_1, argument_2).digit, operator(argument_2, argument_1).digit)
        self.assertEqual(operator(argument_1, argument_2).digit, argument_1.digit - argument_2.digit)
        self.assertEqual(operator(argument_2, argument_1).digit, argument_2.digit - argument_1.digit)

    def test_multiple(self):
        """
        Test case to check Multiplier operator
        """
        argument_1 = Digit(3)
        argument_2 = Digit(2)
        operator = Multiplier()

        self.assertEqual(operator(argument_1, argument_2).digit, operator(argument_1, argument_2).digit)
        self.assertEqual(operator(argument_1, argument_2).digit, argument_1.digit * argument_2.digit)

    def test_division(self):
        """
        Test case to check Divider operator
        """
        argument_1 = Digit(4)
        argument_2 = Digit(2)
        operator = Divider()

        self.assertNotEqual(operator(argument_1, argument_2).digit, operator(argument_2, argument_1).digit)
        self.assertEqual(operator(argument_1, argument_2).digit, argument_1.digit / argument_2.digit)
        self.assertEqual(operator(argument_2, argument_1).digit, argument_2.digit / argument_1.digit)

    def test_power(self):
        """
        Test case to check Power operator
        """
        argument_1 = Digit(3)
        argument_2 = Digit(2)
        operator = Power()

        self.assertEqual(operator(argument_1, argument_2).digit, argument_1.digit ** argument_2.digit)
        self.assertEqual(operator(argument_2, argument_1).digit, argument_2.digit ** argument_1.digit)

    def test_divider_multiplier_feature(self):
        """
        Test case to check Divider and Multiplier feature
        """
        argument_1 = Digit(4)
        argument_2 = Digit(2)
        divider = Divider()
        multiplier = Multiplier()

        division_result = divider(argument_1, argument_2)
        self.assertEqual(multiplier(division_result, argument_2).digit, argument_1.digit)

    def test_plus_minus_feature(self):
        """
        Test case to check Plus and Minus feature
        """
        argument_1 = Digit(4)
        argument_2 = Digit(2)
        minus = Minus()
        plus = Plus()

        minus_result = minus(argument_1, argument_2)
        self.assertEqual(plus(minus_result, argument_2).digit, argument_1.digit)
