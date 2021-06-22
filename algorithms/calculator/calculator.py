"""
Programming for linguists

Implementation of the Reverse Polish Notation Converter
"""
from algorithms.calculator.reverse_polish_notation import ReversePolishNotation, Digit
from data_structures.stack.stack import Stack


class ReversePolishNotationCalculator:
    """
    Calculator of expression in Reverse Polish Notation
    """
    def __init__(self):
        self.stack = Stack()

    def calculate(self, rpn_expression: ReversePolishNotation) -> float:
        """
        Main method of the ReversePolishNotationCalculator class.
        Calculating result of expression in Reverse Polish Notation.

        :param rpn_expression: expression in Reverse Polish Notation Format
        :return: result of the expression
        """
        for item in rpn_expression:

            if isinstance(item, Digit):
                self.stack.push(item)
                continue

            right_operand = self.stack.top()
            self.stack.pop()

            left_operand = self.stack.top()
            self.stack.pop()

            result = item(left_operand, right_operand)
            self.stack.push(result)

        final_result = self.stack.top()
        self.stack.pop()
        return final_result
