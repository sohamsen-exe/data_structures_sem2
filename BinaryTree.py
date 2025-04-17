class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursively(self.root, value)
    def _insert_recursively(self, node, value):
        if value < node.value:
            if not node.left:
                self._insert_recursively(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._insert_recursively(node.right, value)
            else:
                node.right = Node(value)