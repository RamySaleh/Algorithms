# https://leetcode.com/problems/merge-k-sorted-lists/

from Helpers import profiler as prof
from Helpers import test_class
from typing import List
from Helpers import LList as ll

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def mergeKLists(self, lists):
        if not lists:
            return
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        dummy = cur = ll.Node(0)
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r
        return dummy.next

    def mergeKLists2(self, lists: List[ll.Node]):
        head = tail = None
        while lists:
            val = self.getMinInLists(lists)
            if val is not None:
                if not head:
                    head = ll.Node(val)
                    tail = head
                else:
                    node = ll.Node(val)
                    head.next = node
                    head = node
        self.print(tail)
        return tail

    def getMinInLists(self, lLists: List[ll.Node]):
        minIndex = None
        minValue = float('inf')
        for i, head in enumerate(lLists):
            if head and head.val <= minValue:
                minValue = head.val
                minIndex = i

        if minIndex is not None:
            if lLists[minIndex].next:
                lLists[minIndex] = lLists[minIndex].next
            else:
                lLists.remove(lLists[minIndex])
            return minValue
        else:
            lLists.clear()
            return None

    def test_1(self):
        self.assertEqual(None, self.mergeKLists(self.buildLists()))

    def test_2(self):
        self.assertEqual(None, self.mergeKLists([None]))

    def buildLists(self):
        head = ll.Node(1)
        head.next = ll.Node(4)
        head.next.next = ll.Node(5)

        head2 = ll.Node(1)
        head2.next = ll.Node(3)
        head2.next.next = ll.Node(4)

        head3 = ll.Node(2)
        head3.next = ll.Node(6)

        return [head,head2,head3]

    def print(self, head: ll.Node):
        res = ''
        current = head
        while current:
            res += ' ' + str(current.val)
            current = current.next
        print(res)
