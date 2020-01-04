from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def method(self, n: int) -> int:
        return 0

    def test_1(self):
        self.assertEqual(3, self.method(4))

test_class.run()