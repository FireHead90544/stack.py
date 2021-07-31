
# Stack.py

Stack.py is the LIFO Stack & FIFO Queue Implementation in Python. It is not a different data type, but can be treated as one.

**LIFO** - *Last In, First Out*. The last element to get in will be the first to get out.

**FIFO** - *First In, First Out*. The first element to get in will be the first to get out.
## Badges

Provided By: [shields.io](https://shields.io/)

[![PyPI Version](https://img.shields.io/pypi/v/stack.py?style=for-the-badge)](https://pypi.org/project/stack.py/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/stack.py?color=red&style=for-the-badge)](https://pypi.org/project/stack.py/)
[![Apache License 2.0](https://img.shields.io/pypi/l/stack.py?color=lime&style=for-the-badge)](https://opensource.org/licenses/)
[![Connect On Discord](https://img.shields.io/discord/710909601356447805?color=yellow&style=for-the-badge)](https://discord.gg/dN66r3D)
[![Code Lines](https://img.shields.io/tokei/lines/github/FireHead90544/stack.py?color=orange&style=for-the-badge)](https://github.com/FireHead90544/stack.py)
[![Code Size](https://img.shields.io/github/languages/code-size/FireHead90544/stack.py?style=for-the-badge)](https://github.com/FireHead90544/stack.py)
[![Pull Requests](https://img.shields.io/github/issues-pr/FireHead90544/stack.py?style=for-the-badge)](https://github.com/FireHead90544/stack.py/pulls)
[![Issues](https://img.shields.io/github/issues/FireHead90544/stack.py?color=teal&style=for-the-badge)](https://github.com/FireHead90544/stack.py/issues)
[![Contributors](https://img.shields.io/github/contributors/FireHead90544/stack.py?style=for-the-badge)](https://github.com/FireHead90544/stack.py/graphs/contributors)

## Acknowledgements

 - [Issues](https://github.com/FireHead90544/stack.py/issues)
 - [Pull Requests](https://github.com/FireHead90544/stack.py/pulls)
 - [View Project On PyPI](https://pypi.org/project/stack.py/)

  
## Authors

- [@Rudransh Joshi](https://www.github.com/FireHead90544)

  
## Installation

Easiest way is to install stack.py with pip

```shell
  pip install stack.py
```
## Usage / Examples
### Stack
```py
from stack import Stack
s = Stack(6)  # Create a LIFO stack with stack length 6
s.put(1)  # Pushing some elements to the stack
s.put(2)
s.put(3)
s.get()  # Gets an element from the stack, pops it
s.list  # Returns the elements of stack as a list
s.top  # Returns the index of top pointer of the stack
s.list[s.top] # Returns the value of the element at top
s.empty  # Returns True if the stack is empty else returns False
s.clear()  # Clears the stack, and makes it empty
p = s.copy()  # Creates a copy of stack as an independent object
print(s)  # Prints the element of stacks as a stringified list
print(repr(s))  # Returns the class object representation of the stack with the values it holds
```

### Queue
```py
from stack import Queue
q = Queue(10)  # Create a FIFO queue with queue length 6
q.enqueue(1)  # Enqueues elements to the queue
q.enqueue(2)
q.enqueue(3)
q.dequeue()  # Gets an element from the queue, pops it
q.list  # Returns the elements of queue as a list
q.front  # Returns the index of front pointer of the stack
q.rear  # Returns the index of rear pointer of the stack
q.list[s.rear] # Returns the value of the rear element
q.empty  # Returns True if the queue is empty else returns False
q.clear()  # Clears the queue, and makes it empty
t = q.copy()  # Creates a copy of stack as an independent object
print(q)  # Prints the element of queue as a stringified list
print(repr(q))  # Returns the class object representation of the queue with the values it holds
```
## Contributing

Contributions are always welcome!

- Fork this repository.
- Make the changes in your forked repositry.
- Generate a pull request.

Please adhere to the GitHub's `code of conduct`.

  
## License

[Apache License 2.0](https://choosealicense.com/licenses/apache-2.0/)
