from Helpers import profiler as prof
from Helpers import helper as hlp

class node:
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value

class Solution:

    def __init__(self):
        self.tree = None

    def insert_tree(self, value):
        if not self.tree:
            self.tree = node(value)
        else:
            self.insert(value, self.tree)

    def insert(self, value , curr_node = None):
        # left < root
        # right > root
        if value > curr_node.value:
            if not curr_node.right:
                curr_node.right = node(value)
            else:
                self.insert(value, curr_node.right)
        elif value < curr_node.value:
            if not curr_node.left:
                curr_node.left = node(value)
            else:
                self.insert(value, curr_node.left)

    def post_order_rec(self, root):
        res = []
        if root:
            # current, current.left, current.right
            res += self.post_order_rec(root.left)
            res += self.post_order_rec(root.right)
            res.append(root.value)
        return res

    def post_order_itr(self, root):
        res = []
        pre_stack = [(root, '')]
        while pre_stack:
            current = pre_stack.pop()
            if current[0]:
                # push right, push current, push left
                if current[1] == 'v':
                    res.append(current[0].value)
                else:
                    pre_stack.append((current[0].right, ''))
                    pre_stack.append((current[0].left, ''))
                    pre_stack.append((current[0], 'v'))
        return res

def run(parms):
    sl = Solution()
    for item in parms[0] : sl.insert_tree(item)
    print("inserted")

    #res = sl.post_order_rec(sl.tree)
    res = sl.post_order_itr(sl.tree)
    print(res)

input = [1, 2, 3]
prof.profile(run, input)