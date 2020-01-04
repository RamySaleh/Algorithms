import numpy as np
import unittest

def generate_array(random , length):
    return np.random.randint(random, size=length)

class code_tests(unittest.TestCase):

    # set up method for the whole class
    def setUp(self):
        from fib import Solution as sl
        self.sl = sl()

    # test constructor
    def test_run(self):
        self.assertEqual(self.sl.fib(4) , 3)

def assert_equal():
    runner = unittest.TextTestRunner()
    suite = unittest.TestLoader().loadTestsFromTestCase(code_tests)
    runner.run(suite)
