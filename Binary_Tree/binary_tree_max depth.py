from Helpers import profiler as prof
from Helpers import helper as hlp
from Helpers import node as nd

class Solution:
    def __init__(self):
        self.tree = None
        self.max_depth = 0
    def insert(self, value):
        if not self.tree:
            self.tree = nd.node(value)
        else:
            self.tree.insert_level(value)

    def get_max_depth_top_down(self):
        self.max_depth = 0
        self.get_depth_top_down(self.tree, 0)
        return self.max_depth

    def get_depth_top_down(self, root, depth):
        if root:
            if depth > self.max_depth:
                self.max_depth = depth

            self.get_depth_top_down(root.left, depth + 1)
            self.get_depth_top_down(root.right, depth + 1)

    def get_max_depth_bottom_up(self):
        return self.get_depth_bottom_up(self.tree)

    def get_depth_bottom_up(self, root):
        if not root:
            return 0

        l_depth = self.get_depth_bottom_up(root.left)
        r_depth = self.get_depth_bottom_up(root.right)
        depth = max(l_depth, r_depth) + 1

        return depth

def run(parms):
    sl = Solution()
    for item in parms[0] : sl.insert(item)
    print("inserted")

    res = sl.get_max_depth_bottom_up()
    res = sl.get_max_depth_top_down()
    print(res)

input = [1, 2, 3]
input = [3,9,20,5,9,15,7]
prof.profile(run, input)