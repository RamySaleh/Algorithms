from Helpers import test_class
from typing import List


class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def maxNumberCities(self, arr: List[str]) -> int:
        cities = {}
        self.maxPath = 0
        for i,city in enumerate(arr):
            if city != i:
                cities.setdefault(city,[]).append(i)

        self.dfs(0, cities, 1, 0)

        return self.maxPath

    def dfs(self, city, cities, path, odds):
        if city % 2 != 0:
            odds += 1

        print(f'c = {city}, p = {path}, o = {odds}')
        if odds > 1:
            return

        self.maxPath = max(self.maxPath, path)

        if city in cities:
            for city in cities[city]:
                self.dfs(city, cities, path + 1, odds)


    def test_1(self):
        self.assertEqual(4 ,self.maxNumberCities([0,9,0,2,6,8,0,8,3,0]))

    def test_2(self):
        self.assertEqual(3 ,self.maxNumberCities([0,0,0,1,6,1,0,0]))
