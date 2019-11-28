from Helpers import profiler as prof
from Helpers import helper as hlp
import numpy as np


class node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class stack:
    def __init__(self):
        self._top = None

    def push(self, value):
        self._top = node(value, self._top)

    def pop(self):
        top = self._top
        self._top = top.next
        return top

    def is_empty(self):
        return self._top is None


stack = stack()


def run(parms):
    arr = parms[0]
    for item in arr: stack.push(item)

    while not stack.is_empty():
        stack.pop().value


input = hlp.generate_array(10, 1000000)

#print(input)
print("push & popping")
prof.profile(run, input)



