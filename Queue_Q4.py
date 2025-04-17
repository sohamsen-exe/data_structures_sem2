

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

def merge_queues(queue1, queue2):
    merged_queue = Queue()
    while not queue1.is_empty() or not queue2.is_empty():
        if not queue1.is_empty():
            merged_queue.enqueue(queue1.dequeue())
        if not queue2.is_empty():
            merged_queue.enqueue(queue2.dequeue())
    return merged_queue

# Example usage
queue1 = Queue()
queue2 = Queue()

queue1.enqueue(1)
queue1.enqueue(3)
queue1.enqueue(5)

queue2.enqueue(2)
queue2.enqueue(4)
queue2.enqueue(6)

merged_queue = merge_queues(queue1, queue2)

while not merged_queue.is_empty():
    print(merged_queue.dequeue())
     
