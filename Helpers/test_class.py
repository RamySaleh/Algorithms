import unittest
from Helpers import profiler as prof

class test_class(unittest.TestCase):

    def setUp(self):
        self.prof_start = prof.start()

    def tearDown(self):
        prof.stop(self.id(), self.prof_start)

def run():
    unittest.main()