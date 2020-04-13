# https://leetcode.com/discuss/interview-question/451422/microsoft-oa-2019-fair-indexes?fbclid=IwAR3e5B4VIqluCQjpEC2aVtPHMMq_JkQ4uHgT4o9bUKuH51rn8DZ7YfGq-Qo

from Helpers import test_class
from typing import List


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def getFairIndices(self, A: List[str], B: List[str]) -> int:
        res = []
        sum_after_a = sum(A)
        sum_before_a = 0
        sum_after_b = sum(B)
        sum_before_b = 0

        for i in range(1, len(A)):
            # sum before : 0 -> k - 1
            # sum after : k -> n - 1
            sum_before_a += A[i - 1]
            sum_after_a -= A[i - 1]

            sum_before_b += B[i - 1]
            sum_after_b -= B[i - 1]

            if sum_before_a == sum_after_a == sum_before_b == sum_after_b:
                res.append(i)
        return res

    def test_1(self):
        self.assertEqual([2, 3], self.getFairIndices([4, -1, 0, 3], [-2, 5, 0, 3]))

    def test_2(self):
        self.assertEqual([], self.getFairIndices([4, -1, 0, 3], [-2, 6, 0, 4]))

    def test_3(self):
        self.assertEqual([2, 4], self.getFairIndices([1, 4, 2, -2, 5], [7, -2, -2, 2, 5]))
