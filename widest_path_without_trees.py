#

from Helpers import helper as hlp
from Helpers import test_class
import re

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def widestPath(self, x, y):
        x.sort()
        max_width = 0
        for i in range(1,len(x)):
            max_width = max(max_width, x[i] - x[i - 1])
        return max_width

    def test_1(self):
        self.assertEqual(4, self.widestPath([6,10,1,4,3],[2,5,3,1,6]))

    def test_2(self):
        self.assertEqual(3, self.widestPath([4,1,5,4],[4,5,1,3]))

    def test_3(self):
        self.assertEqual(2, self.widestPath([5,5,5,7,7,7],[3,4,5,1,3,7]))