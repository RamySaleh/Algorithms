from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()
        self.lookup = {}

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        if n - 1 not in self.lookup:
            self.lookup[n - 1] = self.fib(n - 1)

        if n - 2 not in self.lookup:
            self.lookup[n - 2] = self.fib(n - 2)

        return self.lookup[n - 1] + self.lookup[n - 2]

    def test_1(self):
        self.assertEqual(self.fib(4) , 3)

    def test_2(self):
        self.assertEqual(self.fib(163) , 5193981023518027157495786850488117)

test_class.run()

