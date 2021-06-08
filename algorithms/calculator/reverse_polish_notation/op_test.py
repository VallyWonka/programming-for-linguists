"""
Programming for linguists

Tests for creating of operators
"""
import unittest

from algorithms.calculator.reverse_polish_notation import OpFactory
from algorithms.calculator.reverse_polish_notation.binary_op import Plus, Minus, Multiplier, Divider, Power


# @unittest.skip('There is not implementation of OperatorFactory yet')
class OperatorCreationTestCase(unittest.TestCase):
    """
    Class with test cases for creating of operators
    """

    def test_create_plus(self):
        """
        Test case to create Plus operator
        """
        operator = '+'
        self.assertIsInstance(OpFactory.get_op_by_symbol(operator), Plus)

    def test_create_minus(self):
        """
        Test case to create Minus operator
        """
        operator = '-'
        self.assertIsInstance(OpFactory.get_op_by_symbol(operator), Minus)

    def test_create_multiplier(self):
        """
        Test case to create Multiplier operator
        """
        operator = '*'
        self.assertIsInstance(OpFactory.get_op_by_symbol(operator), Multiplier)

    def test_create_divider(self):
        """
        Test case to create Divider operator
        """
        operator = '/'
        self.assertIsInstance(OpFactory.get_op_by_symbol(operator), Divider)

    def test_create_power(self):
        """
        Test case to create Power operator
        """
        operator = '^'
        self.assertIsInstance(OpFactory.get_op_by_symbol(operator), Power)

    def test_create_wrong_operator(self):
        """
        Test case raise error if cannot create operator for unsupported symbol
        """
        operator = '.'
        self.assertRaises(AssertionError, OpFactory.get_op_by_symbol, operator)


# @unittest.skip('There is not implementation of Operators yet')
class OperatorPriorityTestCase(unittest.TestCase):
    """
    Class with test cases for priority of operators
    """
    def test_priority(self):
        """
        Test case to check priority of Operators
        """
        plus = OpFactory.get_op_by_symbol('+')
        minus = OpFactory.get_op_by_symbol('-')
        multiplier = OpFactory.get_op_by_symbol('*')
        divider = OpFactory.get_op_by_symbol('/')
        power = OpFactory.get_op_by_symbol('^')
        self.assertFalse(plus > minus)
        self.assertFalse(minus > plus)
        self.assertFalse(minus > multiplier)
        self.assertTrue(multiplier > minus)
        self.assertFalse(multiplier > divider)
        self.assertFalse(divider > multiplier)
        self.assertFalse(divider > power)
        self.assertTrue(power > divider)
