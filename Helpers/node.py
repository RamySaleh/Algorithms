class node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert_binary(self, val):

        # Compare the new val with the parent node
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert_binary(val)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert_binary(val)
        else:
            self.val = val

    def insert_level(self, val):
        if not self.left:
            self.left = node(val)
        elif not self.right:
            self.right = node(val)
        else:
            if not self.left.left:
                self.left.insert_level(val)
            else:
                self.right.insert_level(val)

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

        # we can build the tree by the fact that:
        # 1. the last element in the postorder list is the root of the tree
        # 2. if we took this element and search it in the inorder list we find that the number of elements
        # on the left of it is the size of the left subtree (leftSize) in the postorder traversal and the same for the right (rightSize).
        # 3. here the root (laste lement in the postorder list) will be preceeded by rightSize nodes preceeded by leftSize nodes in the postorder list
        # 3. we can recursively get the left and right nodes of each root using this way
        # 4. this takes O(n^2) runtime but we can make it O(n) by buidling a hashtable for the locations of every element in the inorder list