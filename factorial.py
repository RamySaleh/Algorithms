from Helpers import profiler as prof
from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def factorial(self, n):
        if n == 1:
            return 1

        return n * self.factorial(n - 1)

    def test_1(self):
        self.assertEqual(self.factorial(5) , 120)

test_class.run()