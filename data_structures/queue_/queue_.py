"""
Programming for linguists

Implementation of the data structure "Queue"
"""
import math
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
        for element in data:
            try:
                element, priority = element
            except TypeError:
                self.data[math.inf].insert(0, element)
            else:
                self.data[priority].insert(0, element)
        self.min_priority = self._set_min_priority()

    def put(self, element, priority: int = math.inf):
        """
        Add the element ‘element’ at the end of queue_ with the priority value of ‘priority’
        :param element: element to add to queue_
        :param priority: priority of the element
        """
        self.data[priority].insert(0, element)
        if priority < self.min_priority:
            self.min_priority = priority

    def get(self):
        """
        Remove and return an item from queue_
        """
        item = self.top()
        self.data[self.min_priority].pop(-1)
        if not self.data[self.min_priority]:
            del self.data[self.min_priority]
            self.min_priority = self._set_min_priority()
        return item

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
        return len(self.data.values())

    def top(self):
        """
        Return the first element in queue_
        :return: Item from queue_
        """
        return self.data[self.min_priority][-1]

    # pylint: disable=no-self-use
    def capacity(self) -> int:
        """
        Return the maximal size of queue_
        :return: Maximal size of queue_
        """
        return 0

    def _set_min_priority(self):
        return min(self.data.keys()) if self.data else math.inf
