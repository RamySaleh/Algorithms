from Helpers import profiler as prof
from Helpers import helper as hlp
from Helpers import node as nd

class Solution:
    def __init__(self, root):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        if self.stack:
            root = self.stack.pop()
            cur = root.right

            while cur:
                self.stack.append(cur)
                cur = cur.left
            return root.val


    def hasNext(self):
        return len(self.nodes) > 0

def run(parms):
    sl = Solution(parms[0])
    #for item in parms[0] : sl.insert(item)
    print("inserted")

    print(sl.next())
    print(sl.next())
    print(sl.next())

def build_tree():
    tree = nd.node(2)
    tree.left = nd.node(1)
    tree.right = nd.node(3)
    return tree


def build_tree2():
    tree = nd.node(7)
    tree.left = nd.node(3)
    #tree.left.left = nd.node(3)
    #tree.left.right = nd.node(4)

    tree.right = nd.node(15)
    tree.right.left = nd.node(9)
    tree.right.right = nd.node(20)
    return tree

input = build_tree2()
prof.profile(run, input)

