import unittest
from Helpers import profiler as prof
import yappi

class test_class(unittest.TestCase):

    def setUp(self):
        self.prof_start = prof.start()
        yappi.start(builtins=False)

    def tearDown(self):
        prof.stop(self.id(), self.prof_start)
        #if self.profile:
        #    self.printProfile(3)

    def printProfile(self, lines):
        print('\n')
        stats = yappi.get_func_stats().sort(sort_type='tsub', sort_order='desc')  # .print_all()
        i = 0
        print(f'{"function".ljust(30, " ")} {"calls".ljust(10, " ")} time')
        for stat in stats:
            print(f'{stat[0].ljust(30," ")} {str(stat[3]).ljust(10," ")} {round(stat[7],3)}')
            i += 1
            if i == lines:
                break

def run():
    unittest.main()