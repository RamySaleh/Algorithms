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

    def insert(self, value):
        if not self.tree:
            self.tree = node(value)
        else:
            self.insert_tree(value, self.tree)

    def insert_tree(self, value , curr_node = None):
        if not curr_node.left:
            curr_node.left = node(value)
        elif not curr_node.right:
            curr_node.right = node(value)
        else:
            self.insert_tree(value, curr_node.left)

    def breadth_first(self, root):
        from queue import Queue
        res = []
        queue = Queue()
        queue.put([root])

        # print left , print right , print root
        while not queue.empty():
            current_level = queue.get()
            children = []
            out = []
            for item in current_level:
                if item:
                    if item.value:
                        out.append(item.value)
                    children.append(item.left)
                    children.append(item.right)

            if children:
                queue.put(children)
            if out:
                res.append(out)
        return res

def run(parms):
    sl = Solution()
    for item in parms[0] : sl.insert(item)
    print("inserted")

    res = sl.breadth_first(sl.tree)
    print(res)

input = [3,9,20,None,None,15,7]
#input = [1,2,3,4,5,6,7]
prof.profile(run, input)