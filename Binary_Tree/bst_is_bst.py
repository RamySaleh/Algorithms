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

    def is_Valid_BST(self):
        return self.is_bst(self.tree, float('inf'), float('-inf'))

    def is_bst(self, root, lessThan, largerThan):
        if not root:
            return True
        if root.val <= largerThan or root.val >= lessThan:
            return False
        return self.is_bst(root.left, root.val, largerThan) and \
               self.is_bst(root.right, lessThan, root.val)


def run(parms):
    sl = Solution()
    #for item in parms[0] : sl.insert(item)
    sl.tree = parms[0]
    print("inserted")

    res = sl.is_Valid_BST()
    print(res)

def build_sym_tree():
    tree = nd.node(2)
    tree.left = nd.node(1)
    tree.right = nd.node(3)
    return tree


def build_sym_tree2():
    tree = nd.node(5)
    tree.left = nd.node(1)
    #tree.left.left = nd.node(3)
    #tree.left.right = nd.node(4)

    tree.right = nd.node(4)
    tree.right.left = nd.node(3)
    tree.right.right = nd.node(6)
    return tree

def build_sym_tree3():
    tree = nd.node(5)
    return tree

input = [1, 2, 3]
input = build_sym_tree()
prof.profile(run, input)

