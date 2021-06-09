"""
Programming for linguists

Interfaces for digits
"""
from typing import Union

from algorithms.calculator.reverse_polish_notation.element import Element


class Digit(Element):
    """
    Interface for presenting a digit
    """

    def __init__(self, digit_as_string: Union[float, str]):
        if not digit_as_string:
            self.digit = None
        elif isinstance(digit_as_string, (float, int)):
            self.digit = digit_as_string
        elif "." in digit_as_string:
            self.digit = float(digit_as_string)
        else:
            self.digit = int(digit_as_string)

    def __repr__(self) -> str:
        """
        Magic method to present an instance of this class as string
        """
        return str(self.digit)

    def __eq__(self, other: 'Digit') -> bool:
        """
        Magic method to compare instances of Digit class
        """
        if self.digit == other.digit:
            return True
        return False
