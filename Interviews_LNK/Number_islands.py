#https://leetcode.com/problems/number-of-islands/
from typing import List

from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def numIslands(self, grid):
        if not grid:
            return 0
        count = 0
        h, w = len(grid), len(grid[0])
        visited = [[False for _ in range(w)] for _ in range(h)]
        for r in range(w):
            for c in range(w):
                if grid[r][c] == 1 and not visited[r][c]:
                    count += 1
                    self.dfs(grid, r, c, visited)
        return count

    def dfs(self, grid, r, c, visited):
        if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])) or grid[r][c] == "0" or visited[r][c]:
            return
        visited[r][c] = True
        self.dfs(grid, r + 1, c, visited) # down
        self.dfs(grid, r - 1, c, visited) # up
        self.dfs(grid, r, c + 1, visited) # right
        self.dfs(grid, r, c - 1, visited) # left

    def numIslands2(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))  # map in python3 return iterator
                return 1
            return 0

        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

    def test_1(self):
        self.assertEqual(3, self.numIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]))

    def test_2(self):
        self.assertEqual(3, self.numIslands([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]))

    def test_3(self):
        self.assertEqual(1, self.numIslands([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]))

    def test_4(self):
        self.assertEqual(1, self.numIslands([[1,1,0],[3,4,0],[0,0,0]]))

    def test_5(self):
        self.assertEqual(1, self.numIslands([[1,1,0],[1,1,0],[0,0,0]]))