from Helpers import helper as hlp
from Helpers import test_class
import collections
import multiprocessing
from os import listdir

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def getSimilarDoc(self, mainDoc: str, docs) -> int:
        mainDoc_words = mainDoc.split(' ')
        mainDoc_vec = collections.Counter(mainDoc_words)

        match = None
        max_score = -1
        for doc in docs:
            doc_words = doc.split(' ')
            doc_vec = collections.Counter(doc_words)
            #doc_dot = sum(map(lambda w: mainDoc_vec[w] * doc_vec[w], mainDoc_words)) / (len(mainDoc_words) + len(doc_words))
            doc_dot = sum(map(lambda w: mainDoc_vec[w] * doc_vec[w], mainDoc_words))
            doc_dot /= (len(mainDoc_words) + len(doc_words))
            if doc_dot >= max_score:
                max_score = doc_dot
                match = doc

        return match

    def test_1(self):
        self.assertEqual('the code is good good', self.getSimilarDoc('the code is good good', ['the code is good good', 'the code is nice', 'the code is good good nice']))

    def test_2(self):
        files = self.read_files('../resources/docs')
        self.assertEqual(files[0], self.getSimilarDoc(files[0], files))

    def test_3_big(self):
        files = self.read_files('../resources/docs/big')
        self.assertEqual(files[0], self.getSimilarDoc(files[0], files))

    def read_files(self, folder):
        def read_file(path):
            f = open(path, 'r')
            x = f.read()
            f.close()
            return x

        files = [read_file(f'{folder}/{file}') for file in listdir(folder)]
        return files
