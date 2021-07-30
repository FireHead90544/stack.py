"""
STACK - LIFO Implementation of Stack in Python
Author: Rudransh Joshi (https://github.com/FireHead90544)
"""

from __future__ import annotations
from typing import List, Union, Any
import copy

__author__ = "Rudransh Joshi"
__version__ = 1.0


class Stack:
    """
    LIFO Implementation of Stack in Python\n
    Creates a stack object
    """

    def __init__(self, stackLength: int = 5):
        """
        LIFO Implementation of Stack in Python\n
        Initialises a stack object with given stack length.\n
        Stack length defaults to 5
        """
        self.stackLength = stackLength
        self._top = -1
        self._stackList = []

    @property
    def top(self) -> int:
        """
        Returns the top value of the stack.
        """
        self._top = len(self._stackList) - 1
        return self._top

    @property
    def list(self) -> List[Any]:
        """
        Returns the values that the stack holds as a list
        """
        return self._stackList

    @property
    def get(self) -> Any:
        """
        Returns the value of top element from the stack
        """
        if self.top < 0:
            return None
        return self._stackList[self.top]

    def push(self, e: Any) -> None:
        """
        Pushes an element to the stack.\n
        If the stack is already full, then shows OverflowError.\n
        Returns None
        """
        if len(self._stackList) >= self.stackLength:
            raise OverflowError('The stack is already full. Unable to push any more elements.')
        self._stackList.append(e)

    def pop(self) -> Any:
        """
        Pops the last element from the stack.\n
        If the stack is already empty, then shows UnderflowError.\n
        Returns the value popped
        """
        if self.top < 0:
            raise Exception('UnderflowError: The stack is already empty. Unable to pop any elements.')
        else:
            return self._stackList.pop()

    def clear(self) -> None:
        """
        Clears the stack, removes every element from the stack.\n
        Returns None
        """
        self._stackList = []

    def copy(self) -> 'Stack':
        """
        Returns the copy of the stack as a Stack object
        """
        return copy.deepcopy(self)

    def __str__(self) -> str:
        """
        Overrides __str__ dunder method.
        Returns the stack as a list object
        """
        return f"{self._stackList}"

    def __repr__(self) -> str:
        """
        Overrides __repr__ dunder method.\n
        Returns the class object representation of the stack with the values it holds
        """
        return f"Stack(length={self.stackLength}, top={self.top}, stack={self._stackList})"
