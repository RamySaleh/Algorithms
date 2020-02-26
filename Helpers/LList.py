class Node():
    def __init__(self, val = None):
        self.next = None
        self.prev = None
        self.val = val

class LList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, x: int) -> None:
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
        else:
            node = Node(x)
            self.head.next = node
            node.prev = self.head
            self.head = node
        self.length += 1

    def pushleft(self, x: int) -> None:
        if not self.head:
            self.head = Node(x)
            self.tail = self.head
        else:
            node = Node(x)
            node.next = self.tail
            self.tail.prev = node
            self.tail = node
        self.length += 1

    def pop(self) -> int:
        res = None
        if self.head:
            res = self.head.val
            if self.head.prev:
                self.head = self.head.prev
                self.head.next = None
            else:
                self.head = self.tail = None
        self.length -= 1
        return res

    def insert(self,val):
        if val >= self.tail.val:
            self.pushleft(val)
        else:
            current = self.tail
            while current:
                if val < current.val:
                    current = current.next
                else:
                    current = current.prev
                    break

            if current:
                node = Node(val)
                node.next = current.next
                current.next.prev = node
                current.next = node
                node.prev = current

        self.length += 1
        self.print()

    def top(self) -> int:
        return self.head.val

    def len(self):
        return self.length

    def print(self):
        res = ''
        current = self.tail
        while current:
            res += ' ' + str(current.val)
            current = current.next
        print(res)