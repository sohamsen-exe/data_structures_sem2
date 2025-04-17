import numpy as np

class Queue:
    def __init__(self, size):
        self.front = -1
        self.rear = -1
        self.arr = np.array([0] * size)  # initialize the array..

    def isempty(self):
        return self.front == -1

    def isfull(self):
        return self.front == 0 and self.rear == self.size() - 1

    def size(self):
        return len(self.arr)

    def peek(self):
        if self.isempty():
            print("\nQueue is empty")
        else:
            print("\nFront element is:", self.arr[self.front])

    def enqueue(self, item):
        if self.isfull():
            print("\nQueue is Full")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.arr[self.rear] = item
            print(f"{item} added to the queue")

    def dequeue(self):
        if self.isempty():
            print("\nQueue is empty")
        else:
            dequeue_item = self.arr[self.front]
            if self.front == self.rear:
                self.front = self.rear = - 1
            else:
                self.front += 1
            print(f"\n{dequeue_item} removed from the queue")
            return dequeue_item

    def display(self):
        if self.isempty():
            print("\nQueue is empty")
        else:
            print("\nQueue elements:")
            for i in range(self.front, self.rear + 1):
                print(self.arr[i])


len_arr = int(input("Enter the length of the queue: "))
q = Queue(len_arr)
while True:
    print("\nOperations:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    op = int(input("Enter your choice (1-5): "))
    if op == 1:
        item = input("\nEnter the item to enqueue: ")
        q.enqueue(item)
    elif op == 2:
        q.dequeue()
    elif op == 3:
        q.peek()
    elif op == 4:
        q.display()
    elif op == 5:
        print("Thank You!")
        break
    else:
        print("Invalid choice")