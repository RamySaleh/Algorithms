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

    def is_sym(self):
        if not self.tree:
            return True

        return self.is_sym_rec(self.tree.left, self.tree.right)

    def is_sym_rec(self, left, right):
        if left and not right:
            return False
        elif right and not left:
            return False
        elif not right and not left:
            return True
        else:
            if left.value != right.value:
                return False

            return self.is_sym_rec(left.left, right.right) and self.is_sym_rec(left.right , right.left)


def run(parms):
    sl = Solution()
    #for item in parms[0] : sl.insert(item)
    sl.tree = parms[0]
    print("inserted")

    res = sl.is_sym()
    print(res)

def build_sym_tree():
    tree = nd.node(1)
    tree.left = nd.node(2)
    tree.left.left = nd.node(3)
    tree.left.right = nd.node(4)

    tree.right = nd.node(2)
    tree.right.left = None#nd.node(4)
    tree.right.right = nd.node(3)
    return tree

input = [1, 2, 3]
input = [1,2,2,3,4,4,3]
input = build_sym_tree()
prof.profile(run, input)

