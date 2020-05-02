# https://leetcode.com/problems/sort-list/

from Helpers import profiler as prof
from Helpers import test_class
from typing import List
from Helpers import LList as ll

class Solution(test_class.test_class):

    def setUp(self):
        super().setUp()

    def sortList(self, head, length = None):
        if not length:
            length = self.len(head)

        if not head:
            return
        if length == 1:
            return head

        mid = length // 2
        l,r = self.split(head,mid)
        l = self.sortList(l, mid)
        r = self.sortList(r, length - mid)
        return self.merge(l, r)

    def len(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

    def split(self, head, idx):
        counter = 0
        l = head
        prev = None
        while counter < idx:
            prev = head
            head = head.next
            counter+=1
        prev.next = None
        r = head
        return l,r

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

    def test_1(self):
        res = self.sortList(self.buildList())
        self.print(res)
        self.assertEqual(None, res)

    def test_2(self):
        self.assertEqual(None, self.sortList([None]))

    def buildList(self):
        head = ll.Node(4)
        head.next = ll.Node(2)
        head.next.next = ll.Node(1)
        head.next.next.next = ll.Node(3)

        return head

    def print(self, head: ll.Node):
        res = ''
        current = head
        while current:
            res += ' ' + str(current.val)
            current = current.next
        print(res)
