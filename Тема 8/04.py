class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

class AVLNode(TreeNode):
    def __init__(self, key):
        super().__init__(key)
        self.height = 1


class AVLTree(BinaryTree):
    def __init__(self):
        super().__init__()
        
    @staticmethod
    def _height(node):
        return node.height if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        return self._height(node.right) - self._height(node.left) if node else 0

    def right_rotate(self, y):
        x = y.left
        B = x.right

        x.right = y
        y.left = B

        self._update_height(y)
        self._update_height(x)
        return x

    def left_rotate(self, x):
        y = x.right
        B = y.left

        y.left = x
        x.right = B

        self._update_height(x)
        self._update_height(y)
        return y

    def rebalance(self, node):
        self._update_height(node)
        bf = self._balance_factor(node)

        if bf < -1:
            if self._balance_factor(node.left) > 0:
                node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        if bf > 1:
            if self._balance_factor(node.right) < 0:
                node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def insert(self, key):
        self.root = self._insert_avl(self.root, key)

    def _insert_avl(self, node, key):
        if node is None:
            return AVLNode(key)

        if key < node.key:
            node.left = self._insert_avl(node.left, key)
        elif key > node.key:
            node.right = self._insert_avl(node.right, key)
        else:
            return node

        return self.rebalance(node)