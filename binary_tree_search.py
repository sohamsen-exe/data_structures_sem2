class Stack:
    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self, item):
        if not self.isempty(self):
            return self.items.pop()
        return None

    def peek(self):
        if not self.isempty(self):
            return self.items[-1]
        return None

class TreeNode:
    def __init__(self, Newdata = None, lchild = None, rchild = None):
        self.left = lchild
        self.data = Newdata
        self.right = rchild

class BST:
    def __init__(self):
        self.root = None

    def insert(self, newData):
        newNode = TreeNode(newData)
        if self.root is None:
            self.root = newNode
        else:
            curNode = self.root
            parentNode = None
            while curNode is not None:
                parentNode = curNode
                if curNode.data > newData:
                    curNode = curNode.left
                else:
                    curNode = curNode.right
            if parentNode.data > newData:
                parentNode.left = newNode
            else:
                parentNode.right = newNode

    def preorder(self):
        st = Stack()
        curNode = self.root