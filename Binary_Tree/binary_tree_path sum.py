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

    def get_path_sum_top_down(self, r_sum):
        self.r_sum = r_sum
        return self.get_sum_top_down(self.tree, 0)

    def get_sum_top_down(self, root, sum):
        if root:
            sum += root.value

            # leaf node
            if not root.left and not root.right:
                if sum == self.r_sum:
                    return True
                else:
                    return False

            return self.get_sum_top_down(root.left, sum) or self.get_sum_top_down(root.right, sum)
        else:
            return False

    def get_path_sum_itr(self):
        self.r_sum = r_sum
        return self.get_sum_itr(self.tree)

    def get_sum_itr(self, root, sum: int) -> bool:
        if root is None:
            return False

        nodes = [root]
        sums = [0]

        while nodes:
            currnode = nodes.pop()
            currsum = sums.pop()

            if not currnode.left and not currnode.right:  # this is a leaf
                if currsum + currnode.val == sum:
                    return True

            if currnode.left:
                nodes.append(currnode.left)
                sums.append(currsum + currnode.val)

            if currnode.right:
                nodes.append(currnode.right)
                sums.append(currsum + currnode.val)

        return False

def run(parms):
    sl = Solution()
    for item in parms[0]: sl.insert(item)
    print("inserted")

    res = sl.get_path_sum_top_down(parms[1])
    print(res)


input, r_sum = [1, 2, 3, 4, 5], 8
#input, r_sum = [1, 2], 1
input, r_sum = [-2, -3], -5

prof.profile(run, input, r_sum)
