"""
Programming for linguists

Tests for Brackets operators
"""
import unittest

from algorithms.calculator.reverse_polish_notation.bracket import OpenBracket, CloseBracket


# @unittest.skip('There is not implementation of Brackets yet')
class BracketsTestCase(unittest.TestCase):
    """
    Test cases for Brackets operators
    """

    def test_open_bracket_symbol(self):
        """
        Simple test for OpenBracket operator
        """
        open_bracket = OpenBracket()

        self.assertEqual(open_bracket.symbol, '(')

    def test_close_bracket_symbol(self):
        """
        Simple test for CloseBracket operator
        """
        close_bracket = CloseBracket()

        self.assertEqual(close_bracket.symbol, ')')
