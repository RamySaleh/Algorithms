# https://leetcode.com/problems/integer-to-english-words/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class
import re


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()
        self.map = {1: "One", 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                    9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                    16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty',
                    40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety', 0: 'Zero'}

        self.billion = 1000000000
        self.million = 1000000
        self.thousand = 1000
        self.hundred = 100

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return self.map[0]

        buckets = self.getBuckets(num)

        for i,n in enumerate(buckets):
            if n not in self.map:
                buckets[i] = self.getBuckets(n)

        res = self.getWords(buckets)

        return res.strip()

    def getBuckets(self, num):
        buckets = [0 for _ in range(6)]
        while True:
            if num >= self.billion:
                if num == self.billion:
                    billions = 1
                else:
                    billions = num // self.billion
                num = num % self.billion
                buckets[0] = billions
            elif num >= self.million:
                if num == self.million:
                    millions = 1
                else:
                    millions = num // self.million
                num = num % self.million
                buckets[1] = millions
            elif num >= self.thousand:
                if num == self.thousand:
                    thousands = 1
                else:
                    thousands = num // self.thousand
                num = num % self.thousand
                buckets[2] = thousands
            elif num >= self.hundred:
                if num == self.hundred:
                    hundreds = 1
                else:
                    hundreds = num // self.hundred
                num = num % self.hundred
                buckets[3] = hundreds
            elif 19 < num < self.hundred:
                tens = (num // 10) * 10
                num = num % tens
                buckets[4] = tens
                buckets[5] = num
                break
            elif num < 20:
                buckets[5] = num
                break
        return buckets

    def getWords(self, buckets):
        res = ""
        if buckets[0]:
            if isinstance(buckets[0], int):
                res += f'{self.map[buckets[0]]} Billion '
            else:
                res += f'{self.getWords(buckets[0]).strip()} Billion '
        if buckets[1]:
            if isinstance(buckets[1], int):
                res += f'{self.map[buckets[1]]} Million '
            else:
                res += f'{self.getWords(buckets[1]).strip()} Million '
        if buckets[2]:
            if isinstance(buckets[2], int):
                res += f'{self.map[buckets[2]]} Thousand '
            else:
                res += f'{self.getWords(buckets[2]).strip()} Thousand '
        if buckets[3]:
            res += f'{self.map[buckets[3]]} Hundred '
        if buckets[4]:
            res += f'{self.map[buckets[4]]} '
        if buckets[5]:
            res += f'{self.map[buckets[5]]}'
        return res

    def test_1(self):
        self.assertEqual("Twenty Three", self.numberToWords(23))

    def test_2(self):
        self.assertEqual("One Hundred Twenty Three", self.numberToWords(123))

    def test_3(self):
        self.assertEqual("One Thousand One Hundred Twenty Three", self.numberToWords(1123))

    def test_4(self):
        self.assertEqual("Eleven", self.numberToWords(11))

    def test_5(self):
        self.assertEqual("One Hundred", self.numberToWords(100))

    def test_5_1(self):
        self.assertEqual("Two Hundred", self.numberToWords(200))

    def test_5_2(self):
        self.assertEqual("Two Hundred Thirty Two Thousand", self.numberToWords(232000))

    def test_6(self):
        self.assertEqual("One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven", self.numberToWords(1234567))

    def test_8(self):
        self.assertEqual("One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One", self.numberToWords(1234567891))

    def test_9(self):
        self.assertEqual("Twenty Five Thousand", self.numberToWords(25000))

    def test_10(self):
        self.assertEqual("Twelve Thousand Three Hundred Forty Five", self.numberToWords(12345))