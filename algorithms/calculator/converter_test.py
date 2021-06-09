"""
Programming for linguists

Tests for the Reverse Polish Notation Converter class.
"""
import unittest
from typing import Iterable

from parameterized import parameterized

from algorithms.calculator.converter import ReversePolishNotationConverter
from algorithms.calculator.reverse_polish_notation import ReversePolishNotation, Digit


# @unittest.skip('There is not implementation of ReversePolishNotationConverter yet')
class ConverterTestCase(unittest.TestCase):
    """
    Class with test cases for ReversePolishNotationConverter
    """

    @staticmethod
    def fill_rpn_with_data(rpn: ReversePolishNotation, data: Iterable):
        """
        Help method to fill the reference ReversePolishNotation object with data
        :param rpn: ReversePolishNotation object to fill
        :param data: data to fill from
        """
        for element in data:
            rpn.put(element)

    def assert_rpn_equal(self, first: ReversePolishNotation, second: ReversePolishNotation):
        """
        Help method to check a tested ReversePolishNotation to equal with reference a ReversePolishNotation object

        :param first: testable ReversePolishNotation object
        :param second: expected ReversePolishNotation object
        """
        for actual_element in first:
            expected_element = next(second)
            self.assertEqual(actual_element, expected_element)

    @parameterized.expand([
        ['234', 234],
        ['.234', 0.234],
        ['1.', 1],
        ['1.4', 1.4],
    ])
    def test_digit(self, actual: str, expected_digit: float):
        """
        Test case to check convert single number to RPN
        :param actual: number as string type
        :param expected_digit: the digit that expected after conversion in RPN
        """
        actual_rpn = ReversePolishNotationConverter.convert(actual)
        expected_rpn = ReversePolishNotation()
        self.fill_rpn_with_data(expected_rpn, [Digit(expected_digit)])
        self.assert_rpn_equal(actual_rpn, expected_rpn)
