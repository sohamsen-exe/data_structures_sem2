

class Queue:
    def __init__(self):
        self.queue = []
        self.max_queue = []

    def enqueue(self, x):
        self.queue.append(x)
        while self.max_queue and self.max_queue[-1] < x:
            self.max_queue.pop()
        self.max_queue.append(x)

    def dequeue(self):
        if not self.queue:
            raise IndexError("dequeue from an empty queue")
        value = self.queue.pop(0)
        if value == self.max_queue[0]:
            self.max_queue.pop(0)
        return value

    def max(self):
        if not self.max_queue:
            raise IndexError("max from an empty queue")
        return self.max_queue[0]

# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(2)
print(queue.max())  
queue.dequeue()
print(queue.max())  
queue.dequeue()
print(queue.max())  
