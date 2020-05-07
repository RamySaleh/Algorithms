from Helpers import profiler as prof
from Helpers import helper as hlp
from Helpers import node as nd

class Solution:

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        lookup = {}
        lookup_clone = []

        # initiation
        current = head
        index = 0

        while current:
            # build lookup
            lookup[current] = index

            # clone node and value
            node_clone = Node(current.val)
            node_clone.random = current.random

            # set next pointer
            if index > 0:
                lookup_clone[index - 1].next = node_clone

            # append the new node
            lookup_clone.append(node_clone)

            # next loop
            index += 1
            current = current.next

        # set the random pointer
        for node in lookup_clone:
            if node.random:
                random_index = lookup[node.random]
                node.random = lookup_clone[random_index]

        return lookup_clone[0]

    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None

        self.lookup = {}
        self.lookup_clone = []
        self.buildLookup(head)

        head_clone = self.copyNode(head)
        head_clone = self.assRandom(head, head_clone)
        return head_clone

    def buildLookup(self, node, index=0):
        self.lookup[node] = index
        if node.next:
            self.buildLookup(node.next, index + 1)

    def copyNode(self, node):
        node_clone = Node(node.val)
        self.lookup_clone.append(node_clone)

        if node.next:
            node_clone.next = self.copyNode(node.next)

        return node_clone

    def assRandom(self, node, node_clone):
        if node.random:
            random_index = self.lookup[node.random]
            node_clone.random = self.lookup_clone[random_index]

        if node.next:
            self.assRandom(node.next, node_clone.next)

        return node_clone

def run(parms):
    sl = Solution(parms[0])
    #for item in parms[0] : sl.insert(item)
    print("inserted")

prof.profile(run, input)

