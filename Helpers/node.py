class node:
    def __init__(self, value=None):
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

    def buildTree(self, inorder, postorder):
        self.inorderLocator = {}

        for i in range(len(inorder)):
            self.inorderLocator.apoend(inorder[i], i)

        return self.build_tree_helper(inorder, 0, inorder.length - 1, postorder, 0, postorder.length - 1)

    def build_tree_helper(self, inorder, inorderStart, inorderEnd, postorder, postorderStart, postorderEnd):
        if inorderStart > inorderEnd:
            return None

        root = node(postorder[postorderEnd])
        if inorderStart == inorderEnd:
            return root

        inorder_index = self.inorderLocator.get(postorder[postorderEnd])
        left_subtree_count = inorder_index - inorderStart

        root.left = self.build_tree_helper(inorder, inorderStart, inorder_index - 1, postorder, postorderStart, postorderStart + left_subtree_count - 1)
        root.right = self.build_tree_helper(inorder, inorder_index + 1, inorderEnd, postorder, postorderStart + left_subtree_count, postorderEnd - 1)
        return root
