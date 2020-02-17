# https://leetcode.com/problems/all-oone-data-structure/
import math
from collections import deque, defaultdict

from Helpers import helper as hlp
from Helpers import test_class
import re


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()
        self.buckets = {}
        self.keyCounts = {}
        self.stack = deque()

    def inc(self, key: str) -> None:
        # update the count of the key
        if key in self.keyCounts:
            self.keyCounts[key] += 1
        else:
            self.keyCounts[key] = 1

        # update the counts buckets
        keyCount = self.keyCounts[key]

        if keyCount not in self.buckets:
            self.buckets[keyCount] = set()

        self.buckets[keyCount].add(key)

        # remove the key from the previous bucket
        if keyCount - 1 in self.buckets and key in self.buckets[keyCount - 1]:
            self.buckets[keyCount - 1].remove(key)

        # update the max stack
        if not self.stack or keyCount > self.stack[-1]:
            self.stack.append(keyCount)

        if keyCount <= self.stack[0]:
            self.stack.appendleft(keyCount)

    def dec(self, key: str) -> None:
        # update the count of the key
        if key in self.keyCounts:
            if self.keyCounts[key] > 1:
                self.keyCounts[key] -= 1
                keyCount = self.keyCounts[key]

                # add the key to the correct bucket
                self.buckets[keyCount].add(key)

                # remove the key from the next bucket
                if keyCount + 1 in self.buckets and key in self.buckets[keyCount + 1]:
                    self.buckets[keyCount + 1].remove(key)
            else:  # remove item
                del self.keyCounts[key]
                # remove the key from the 1 bucket
                if 1 in self.buckets:
                    self.buckets[1].remove(key)

    def getMaxKey(self) -> str:
        if not self.stack:
            return ''

        while self.stack:
            maxCount = self.stack[-1]
            if maxCount in self.buckets and self.buckets[maxCount]:
                return next(iter(self.buckets[maxCount]))
            else:
                self.stack.pop()
        return ''

    def getMinKey(self) -> str:
        if not self.stack:
            return ''

        while self.stack:
            minCount = self.stack[0]
            if minCount in self.buckets and self.buckets[minCount]:
                return next(iter(self.buckets[minCount]))
            else:
                self.stack.popleft()
        return ''

    def test_1(self):
        self.inc('a'), self.inc('b'), self.inc('b'), self.inc('b'), self.dec('b')
        self.assertEqual('a', self.getMinKey())
        self.assertEqual('b', self.getMaxKey())

    def test_2(self):
        self.inc('hello')
        self.assertEqual('hello', self.getMinKey())
        self.assertEqual('hello', self.getMaxKey())

    def test_3(self):
        self.inc('hello'),self.inc('hello')
        self.assertEqual('hello', self.getMinKey())
        self.assertEqual('hello', self.getMaxKey())
        self.inc('leet')
        self.assertEqual('leet', self.getMinKey())
        self.assertEqual('hello', self.getMaxKey())
