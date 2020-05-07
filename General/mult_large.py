from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def mult_large(self, num1: str, num2:str) -> int:
        idx = len(num1)-1
        out = ''
        carry = 0

        while idx >= 0:
            n = int(num1[idx])
            m = int(num2)

            res = (n * m) + carry
            out = str(res % 10) + out
            carry = int(res / 10)

            idx -= 1

        return out

    def test_1(self):
        self.assertEqual('32', self.mult_large('16', '2'))

    def test_2(self):
        self.assertEqual('398', self.mult_large('199', '2'))

    def test_3(self):
        self.assertEqual('891', self.mult_large('99', '9'))

#test_class.run()