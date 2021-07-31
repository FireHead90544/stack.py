"""
Stack.py - LIFO Stack & FIFO Queue Implementation in Python
For Docs, Visit The GitHub Repo: https://github.com/FireHead90544/stack.py
Author: Rudransh Joshi (https://github.com/FireHead90544)
Issues: https://github.com/FireHead90544/stack.py/issues
"""

from __future__ import annotations
from typing import List, Any
import copy

__author__ = "Rudransh Joshi"
__version__ = 2.0


class Stack:
    """
    LIFO Implementation of Stack in Python\n
    Last element to get in will be the first to get out
    Creates a Stack object
    """

    def __init__(self, stackLength: int = 5) -> None:
        """
        LIFO Implementation of Stack in Python\n
        Last element to get in will be the first to get out.
        Initialises a stack object with given stack length.\n
        Stack length defaults to 5
        """
        self.stackLength = stackLength
        self._top = -1
        self._stackList = []

    @property
    def top(self) -> int:
        """
        Returns the top index of the stack.
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
    def empty(self) -> bool:
        """
        Returns True if the stack is empty, else returns False
        """
        return False if not self.top == -1 else True


    def put(self, e: Any) -> None:
        """
        Pushes an element to the stack.\n
        If the stack is already full, then shows OverflowError.\n
        Returns None
        """
        if len(self._stackList) >= self.stackLength:
            raise OverflowError('The stack is already full. Unable to push any more elements.')
        self._stackList.append(e)

    def get(self) -> Any:
        """
        Pops/Gets the last element from the stack.\n
        If the stack is already empty, then shows UnderflowError.\n
        Returns the value popped
        """
        if self.top < 0:
            raise Exception('UnderflowError: The stack is empty. Unable to pop/get any elements.')
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
        Returns the stack as a stringified list object
        """
        return f"{self._stackList}"

    def __repr__(self) -> str:
        """
        Overrides __repr__ dunder method.\n
        Returns the class object representation of the stack with the values it holds
        """
        return f"Stack(length={self.stackLength}, top={self.top}, stack={self._stackList})"


class Queue:
    """
    FIFO Implementation of Queue in Python\n
    First element to get in will be the first to get out
    Creates a Queue object
    """

    def __init__(self, queueLength: int = 5):
        """
        FIFO Implementation of Queue in Python\n
        First element to get in will be the first to get out.
        Initialises a queue object with given queue length.\n
        Queue length defaults to 5
        """
        self.queueLength = queueLength
        self._front = 0
        self._rear = -1
        self._queueList = []

    @property
    def front(self) -> int:
        """
        Returns the front index of the queue.
        """
        return self._front

    @property
    def rear(self) -> int:
        """
        Returns the rear index of the queue.
        """
        self._rear = len(self._queueList) - 1
        return self._rear

    @property
    def list(self) -> List[Any]:
        """
        Returns the values that the queue holds as a list
        """
        return self._queueList

    @property
    def empty(self) -> bool:
        """
        Returns True if the queue is empty, else returns False
        """
        return False if not self.rear == -1 else True


    def enqueue(self, e: Any) -> None:
        """
        Enqueues an element to the queue.\n
        If the queue is already full, then shows OverflowError.\n
        Returns None
        """
        if len(self._queueList) >= self.queueLength:
            raise OverflowError('The queue is already full. Unable to enqueue any more elements.')
        self._queueList.append(e)

    def dequeue(self) -> Any:
        """
        Dequeues the first element from the queue.\n
        If the queue is already empty, then shows UnderflowError.\n
        Returns the value dequeued
        """
        if self.rear < 0:
            raise Exception('UnderflowError: The queue is empty. Unable to dequeue any element.')
        else:
            return self._queueList.pop(self.front)

    def clear(self) -> None:
        """
        Clears the queue, removes every element from the queue.\n
        Returns None
        """
        self._queueList = []

    def copy(self) -> 'Queue':
        """
        Returns the copy of the queue as a Queue object
        """
        return copy.deepcopy(self)

    def __str__(self) -> str:
        """
        Overrides __str__ dunder method.
        Returns the queue as a stringified list object
        """
        return f"{self._queueList}"

    def __repr__(self) -> str:
        """
        Overrides __repr__ dunder method.\n
        Returns the class object representation of the queue with the values it holds
        """
        return f"Queue(length={self.queueLength}, front={self.front}, rear={self.rear}, queue={self._queueList})"
