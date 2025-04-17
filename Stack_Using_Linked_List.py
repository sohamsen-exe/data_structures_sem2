class StackLinkedList:
    def __init__(self, NewData, link):
        self.data = NewData
        self.next = link
class stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        return self.top is None
    def push(self, NewData):
        self.top = stackNode(NewData, self.top)
    def pop(self):
        node = self.top
        self.top = self.top.next
        return node.data
    def peek(self):
        return self.top.data
    def display(self):
        node = self.top
        while node is not None:
            print(node.data)
            node = node.next
        print()
    def size(self):
        count = 0
        node = self.top
        while node is not None:
            count += 1
            node = node.next
        return count
    def clear(self):
        self.top = None
        print("Stack cleared")
        return
    