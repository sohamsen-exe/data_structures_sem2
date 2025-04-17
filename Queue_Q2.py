class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            raise IndexError("dequeue from an empty queue")
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def is_empty(self):
        return self.front is None

    def reverse(self):
        if self.is_empty():
            return
        data = self.dequeue()
        self.reverse()
        self.enqueue(data)

# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.reverse()

while not queue.is_empty():
    print(queue.dequeue())
