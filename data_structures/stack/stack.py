"""
Programming for linguists

Implementation of the data structure "Stack"
"""

import math
from typing import Iterable


class Stack:
    """
    Stack Data Structure
    """
    # pylint: disable=missing-module-docstring
    def __init__(self, data: Iterable = (), max_size: int = math.inf):
        self.max_size = max_size
        if not data:
            self.data = []
        elif self.max_size >= len(data):
            self.data = list(data)
        else:
            raise IndexError(f"Size limit exceeded. Please review the parameters and try again.")

    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        if self.size() == self.max_size:
            raise IndexError(f"Size limit reached. Top element: {self.top()}. Max size: {self.max_size}.")
        self.data.append(element)

    def pop(self):
        """
        Delete the element on the top of stack
        """
        self.data.pop(-1)

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        return self.data[-1]

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        return len(self.data)

    def set_max_size(self, new_size: int):
        """
        Set a new size limit
        :param new_size: new size limit of the stack
        """
        self.max_size = new_size

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        return not bool(self.size())
