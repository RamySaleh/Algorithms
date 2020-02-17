# https://leetcode.com/problems/max-stack/
import math
from collections import deque, defaultdict

from Helpers import helper as hlp
from Helpers import test_class
import re

class Node():
    def __init__(self, val = None):
        self.next = None
        self.prev = None
        self.val = val


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()
        self.head = None

    def push(self, x: int) -> None:
        if not self.head:
            self.head = Node(x)
        else:
            node = Node(x)
            self.head.next = node
            node.prev = self.head
            self.head = node

    def pop(self) -> int:
        res = None
        if self.head:
            res = self.head.val
            if self.head.prev:
                self.head = self.head.prev
                self.head.next = None
        return res

    def top(self) -> int:
        return self.head.val

    def peekMax(self) -> int:
        res = float('-inf')
        current = self.head
        while current:
            res = max(res, current.val)
            current = current.prev
        return res

    def popMax(self) -> int:
        res = float('-inf')
        maxNode = None

        current = self.head
        while current:
            if current.val > res:
                res = max(res, current.val)
                maxNode = current
            current = current.prev

        # remove max node
        if maxNode:
            # if head
            if maxNode == self.head:
                return self.pop()
            else:
                if maxNode.next:
                    maxNode.next.prev = maxNode.prev
                if maxNode.prev:
                    maxNode.prev.next = maxNode.next
        return res

    def test_1(self):
        self.push(5),self.push(1),self.push(5)
        self.assertEqual(5, self.top())
        self.assertEqual(5, self.peekMax())
        self.assertEqual(5, self.popMax())
        self.assertEqual(1, self.top())
        self.assertEqual(5, self.peekMax())
        self.pop()
        self.assertEqual(5, self.top())

