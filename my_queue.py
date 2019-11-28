from Helpers import profiler as prof
from Helpers import helper as hlp
import numpy as np


class node:
    def __init__(self, value, next = None , prev = None):
        self.value = value
        self.next = next
        self.prev = prev


class my_queue:
    def __init__(self):
        self._top = None
        self._end = None

    def push(self, value):
        new_node = node(value)
        if self.is_empty():
            self._top = new_node
            self._end = new_node
        else:
            self._end.next = new_node
            new_node.prev = self._end
            self._end = new_node

    def pop(self):
        top = self._top
        self._top = top.next
        return top

    def is_empty(self):
        return self._top is None


my_queue = my_queue()


def run(parms):
    arr = parms[0]
    for item in arr: my_queue.push(item)

    #while not my_queue.is_empty():
    #    item = my_queue.pop().value


input = hlp.generate_array(10, 1000000)

#print(input)
print("push & popping")
prof.profile(run, input)



