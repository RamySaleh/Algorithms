
from Helpers import helper as hlp
from Helpers import test_class

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def longestColor(self, grid):
        w = len(grid[0])
        h = len(grid)
        v = [[False for _ in range(w)] for _ in range(h)]
        l_color = 0
        for r in range(h):
            for c in range(w):
                if not v[r][c]:
                    l_color = max(l_color, self.getColorSum_itr(r, c, grid, v))
        return l_color

    def getColorSum(self, r, c, color, grid, v, sum = 0):
        if not (0 <= r < len(grid)) or not (0 <= c < len(grid[0])) or v[r][c] or grid[r][c] != color:
            return sum

        v[r][c] = True  # visited
        sum += 1
        s1 = self.getColorSum(r, c + 1, color, grid, v, sum)  # right
        s2 = self.getColorSum(r, c - 1, color, grid, v, sum)  # left
        s3 = self.getColorSum(r + 1, c, color, grid, v, sum)  # down
        s4 = self.getColorSum(r - 1, c, color, grid, v, sum)  # up
        return max(s1, s2, s3, s4)

    def getColorSum_itr(self, row, col, grid, v):
        stack = [(row,col)]
        color = grid[row][col]
        w = len(grid[0])
        h = len(grid)
        sum = 0
        while stack:
            curr = stack.pop()
            r, c = curr[0], curr[1]
            if not (0 <= r < h) or not (0 <= c < w) or v[r][c] or grid[r][c] != color:
                continue

            v[r][c] = True  # visited
            sum += 1
            stack.append((r, c + 1))  # right
            stack.append((r, c - 1))  # left
            stack.append((r + 1, c))  # down
            stack.append((r - 1, c))  # up
        return sum


    def test_1(self):
        self.assertEqual(3, self.longestColor([[1,2,3],[3,2,3],[4,1,3]]))

    def test_2(self):
        self.assertEqual(9, self.longestColor([[1,4,4,4,4,3,3,1],[2,1,1,4,3,3,1,1],[3,2,1,1,2,3,2,1],[3,3,2,1,2,2,2,2],[3,1,3,1,1,4,4,4],[1,1,3,1,1,4,4,4]]))

    def test_z(self):
        arr = hlp.generate_array(1000,1000)
        self.assertEqual(3, self.longestColor([arr for _ in range(100)]))