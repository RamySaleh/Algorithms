import collections

import numpy as np
from Helpers import node as tree


def generate_array(random , length):
    return np.random.randint(random, size=length)


def array_to_tree(data):
    data.reverse()
    root = tree.node(data.pop())

    dq = collections.deque()
    dq.append(root)

    while data:
        node = dq.popleft()
        if not node.left:
            node.left = tree.node(data.pop())
            dq.append(node.left)

        if data and not node.right:
            node.right = tree.node(data.pop())
            dq.append(node.right)

    return root

def tree_to_array(root):
    res = []
    dq = collections.deque()
    dq.append(root)

    while dq:
        node = dq.popleft()
        if node:
            res.append(node.val)
            dq.append(node.left)
            dq.append(node.right)

    return res