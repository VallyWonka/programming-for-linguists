"""
Programming for linguists

Implementation of the data structure "Queue"
"""
from typing import Iterable
from collections import defaultdict


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    # pylint: disable=unused-argument,missing-module-docstring
    def __init__(self, data: Iterable = (), max_size: int = None):
        self.data = defaultdict(list)
        for element, priority in data:
            self.data[priority].insert(0, element)

    def put(self, element, priority: int):
        """
        Add the element ‘element’ at the end of queue_ with the priority value of ‘priority’
        :param element: element to add to queue_
        :param priority: priority of the element
        """
        self.data[priority].insert(0, element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        return self.data[self.top()[0]].pop(-1)

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return not self.data

    # pylint: disable=no-self-use
    def full(self) -> bool:
        """
        Return whether queue_ is full or not
        :return: True if queue_ is full.
                 False if queue_ is not full
        """
        return False

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        size = 0
        for value in self.data.values():
            size += len(value)
        return size

    def top(self):
        """
        Return the first element in queue_ and its priority
        :return: Item from queue_
        """
        for key, value in sorted(self.data.items()):
            if value:
                return key, self.data[key][-1]

    # pylint: disable=no-self-use
    def capacity(self) -> int:
        """
        Return the maximal size of queue_
        :return: Maximal size of queue_
        """
        return 0
