

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, x):
        new_node = Node(x)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.front is None:
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def is_empty(self):
        return self.front is None

    def contains(self, x):
        current = self.front
        while current is not None:
            if current.data == x:
                return True
            current = current.next
        return False

# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.contains(2))  # Output: True
print(queue.contains(4))  # Output: False

dequeued_value = queue.dequeue()
print(dequeued_value)  # Output: 1
print(queue.contains(1))  # Output: False
     
