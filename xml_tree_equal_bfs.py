from Helpers import helper as hlp
from Helpers import test_class
import xml.etree.ElementTree as et

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def is_equal(self, file1, file2):
        tree_1 = et.parse(file1)

        tree_2 = et.parse(file2)

        matched = self.compare_trees(tree_1, tree_2)

        return matched

    def compare_trees(self, tree1, tree2):
        matched = False
        root1 = tree1.getroot()
        queue1 = [[root1]]

        root2 = tree2.getroot()
        queue2 = [[root2]]

        while queue1:
            list1 = queue1.pop(0)
            list2 = queue2.pop(0)
            matched = self.compare_lists(list1, list2)

            for node in list1:
                children = []
                for child in node:
                    children.append(child)
                queue1.append(children)

            for node in list2:
                children = []
                for child in node:
                    children.append(child)
                queue2.append(children)

        return matched

    def compare_lists(self, list1, list2):
        match = True
        for node1 in list1:
            found = False
            for node2 in list2:
                if self.compare_nodes(node1, node2):
                    found = True
                    break
            if not found:
                if self.print_log:
                    print(f'{node1} in file 1 is missing or not matching')
                match = False
                break
        return match

    def compare_nodes(self, node1, node2):
        if node1.tag == node2.tag:
            if node1.text and node2.text:
                if node1.text.strip() == node2.text.strip():
                    return True
            else:
                return True
        return False


    def test_match(self):
        self.print_log = False
        self.assertEqual(True, self.is_equal('resources/test.xml', 'resources/test.xml'))

    def test_not_match(self):
        self.print_log = False
        self.assertEqual(False, self.is_equal('resources/test.xml', 'resources/test2.xml'))

    def test_not_match_big(self):
        self.print_log = False
        self.assertEqual(False, self.is_equal('resources/SAF-T Financial__20200106022432_1_1 2.xml', 'resources/SAF-TNorway_CompletedWithWarnings_ExpectedOutput.xml'))

    #def test_match_big(self):
    #    self.print_log = True
    #    self.assertEqual(True, self.is_equal('resources/SAF-TNorway_CompletedWithWarnings_ExpectedOutput.xml', 'resources/SAF-TNorway_CompletedWithWarnings_2.xml'))