"""
Programming for linguists

Tests for Digits
"""
import unittest

from algorithms.calculator.reverse_polish_notation import Digit


# @unittest.skip('There is not implementation of Digits yet')
class DigitTestCase(unittest.TestCase):
    """
    Test cases for Digits operators
    """

    def test_initialize_digit_from_sting(self):
        """
        Test case to check creating digit from string
        """
        digit = Digit('1.4')

        self.assertEqual(digit.digit, 1.4)

    def test_initialize_digit_from_float(self):
        """
        Test case to check creating digit from float
        """
        digit = Digit(1.4)

        self.assertEqual(digit.digit, 1.4)

    def test_initialize_digit_from_normalized_string(self):
        """
        Test case to check creating digit from normalized string
        """
        digit = Digit('1e-4')

        self.assertEqual(digit.digit, 1 * 10 ** -4)
