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
        self.tail = None
        self.maxStack = deque()

    def push(self, x: int) -> None:
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
        else:
            node = Node(x)
            self.head.next = node
            node.prev = self.head
            self.head = node
        if not self.maxStack or (self.maxStack and self.head.val >= self.maxStack[-1].val):
            self.maxStack.append(self.head)
        elif self.maxStack and self.head.val < self.maxStack[-1].val:
            self.maxStack.appendleft(self.head)
        self.print()

    def pop(self) -> int:
        res = None
        if self.head:
            res = self.head.val
            if self.head.prev:
                self.head = self.head.prev
                self.head.next = None
            else:
                self.head = self.tail = None

        if self.maxStack and self.maxStack[-1].val == res:
            self.maxStack.pop()
        self.print()
        return res

    def top(self) -> int:
        return self.head.val

    def peekMax2(self) -> int:
        res = float('-inf')
        current = self.head
        while current:
            res = max(res, current.val)
            current = current.prev
        return res

    def peekMax(self) -> int:
        if self.maxStack:
            return self.maxStack[-1].val
        else:
            return None

    def popMax(self) -> int:
        if self.maxStack:
            maxNode = self.maxStack[-1]

        # remove max node
        if maxNode:
            # if head
            if maxNode == self.head:
                return self.pop()
            else:
                maxNode = self.maxStack.pop()
                if maxNode.next:
                    maxNode.next.prev = maxNode.prev
                if maxNode.prev:
                    maxNode.prev.next = maxNode.next
        self.print()
        return maxNode.val

    def popMax2(self) -> int:
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
        self.print()
        return res

    def print(self):
        res = ''
        current = self.tail
        while current:
            res += ' ' + str(current.val)
            current = current.next
        print(res)

    def test_1(self):
        self.push(5),self.push(1),self.push(5)
        self.assertEqual(5, self.top())
        self.assertEqual(5, self.peekMax())
        self.assertEqual(5, self.popMax())
        self.assertEqual(1, self.top())
        self.assertEqual(5, self.peekMax())
        self.pop()
        self.assertEqual(5, self.top())

    def test_2(self):
        self.push(-2)
        self.assertEqual(-2, self.popMax())
        self.push(-45), self.push(-82), self.push(29)
        self.assertEqual(29, self.pop())
        self.assertEqual(-45, self.peekMax())
        self.push(40)
        self.assertEqual(40, self.pop())

    def test_3(self):
        self.push(5)
        self.push(1)
        self.assertEqual(5, self.popMax())
        self.assertEqual(1, self.peekMax())

