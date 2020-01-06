from Helpers import helper as hlp
from Helpers import test_class
import xml.etree.ElementTree as et

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()
        #self.lookup = {}

    def is_equal(self, file1, file2):
        xml_1 = et.parse(file1)
        lookup_1 = self.build_lookup(xml_1)

        xml_2 = et.parse(file2)
        lookup_2 = self.build_lookup(xml_2)

        matched = self.compare_lookups(lookup_1, lookup_2)

        return matched

    def build_lookup(self, xml):
        root = xml.getroot()
        queue = [(root, '')]
        lookup = {}

        while queue:
            curr, path = queue.pop(0)
            if curr.tag:
                node_name = self.get_key(curr)
                node_text = curr.text.strip()
                path = f'{path}/{node_name}({node_text})'
                lookup[path] = curr

                for child in curr:
                    queue.append((child, path))
        return lookup

    def get_key(self, node):
        prefix, has_namespace, postfix = node.tag.partition('}')
        node_name = node.tag
        if has_namespace:
            node_name = postfix
        return node_name

    def compare_lookups(self, lookup_1, lookup_2):
        matched = True
        for key in lookup_1:
            if key not in lookup_2:
                matched = False
                print(f'{key}')

        for key in lookup_2:
            if key not in lookup_1:
                matched = False
                print(f'{key}')
        return matched

    def generate_key(self, node):
        key = node.tag
        for att in node.attrib:
            # string builder
            key += att
        return hash(key)


    def test_match(self):
        #self.assertEqual(True, self.is_equal('resources/SAF-T Financial__20200106022432_1_1 2.xml', 'resources/SAF-TNorway_CompletedWithWarnings_ExpectedOutput.xml'))
        self.assertEqual(True, self.is_equal('resources/test.xml',
                                             'resources/test.xml'))

    def test_not_match(self):
        #self.assertEqual(True, self.is_equal('resources/SAF-T Financial__20200106022432_1_1 2.xml', 'resources/SAF-TNorway_CompletedWithWarnings_ExpectedOutput.xml'))
        self.assertEqual(True, self.is_equal('resources/test.xml',
                                             'resources/test2.xml'))