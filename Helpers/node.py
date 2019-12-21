class node:
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.value = value

    def insert_binary(self, value):

        # Compare the new value with the parent node
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = node(value)
                else:
                    self.left.insert_binary(value)
            elif value > self.value:
                if self.right is None:
                    self.right = node(value)
                else:
                    self.right.insert_binary(value)
        else:
            self.value = value

    def insert_level(self, value):
        if not self.left:
            self.left = node(value)
        elif not self.right:
            self.right = node(value)
        else:
            if not self.left.left:
                self.left.insert_level(value)
            else:
                self.right.insert_level(value)