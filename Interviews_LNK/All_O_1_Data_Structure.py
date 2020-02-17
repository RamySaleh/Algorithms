# https://leetcode.com/problems/all-oone-data-structure/
import math
from collections import deque, defaultdict

from Helpers import helper as hlp
from Helpers import test_class
import re


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()
        self.table = {}
        self.inverseTable = {}
        self.stack = deque([])

    def inc(self, key: str) -> None:
        if key not in self.table:
            self.table[key] = 1
            self._addKeyToDic(1,key)
        else:
            self.table[key] += 1
            self.inverseTable[self.table[key] - 1].remove(key)
            self._addKeyToDic(self.table[key], key)

        if not self.stack or self.stack[-1] < self.table[key]:
            self.stack.append(self.table[key])

        if self.stack[0] > self.table[key]:
            self.stack.appendleft(self.table[key])

    def dec(self, key: str) -> None:
        if key not in self.table:
            return

        if self.table[key] == 1:
            del self.table[key]
            self.inverseTable[1].remove(key)
        else:
            self.table[key] -= 1
            self.inverseTable[self.table[key] + 1].remove(key)
            self.inverseTable[self.table[key]].add(key)

    def getMaxKey(self) -> str:
        if not self.stack:
            return ''

        while not self.inverseTable[self.stack[-1]]:
            self.stack.pop()

        max_bucket = self.inverseTable[self.stack[-1]]
        return self._getFirstItemFromSet(max_bucket)

    def getMinKey(self) -> str:
        if not self.stack:
            return ''

        while not self.inverseTable[self.stack[0]]:
            self.stack.popleft()

        min_bucket = self.inverseTable[self.stack[0]]
        return self._getFirstItemFromSet(min_bucket)

    def _addKeyToDic(self, dicKey, key):
        if dicKey not in self.inverseTable:
            self.inverseTable[dicKey] = set(key)
        else:
            self.inverseTable[dicKey].add(key)

    def _getFirstItemFromSet(self, itemsSet):
        return next(iter(itemsSet))

    def test_1(self):
        self.inc('a'), self.inc('b'), self.inc('b')
        self.assertEqual('a', self.getMinKey())
