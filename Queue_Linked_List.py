class Node:
    def __init__(self, NewData, link):
        self.data = NewData
        self.next = link

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    def isempty(self):
        return self.front is None
    def enqueue(self, NewData):
        newNode = Node(NewData, None)
        if self.front is None:
            self.front = self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode
    def peek(self):
        return self.front.data
    def dequeue(self):
        frontNode = self.front
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = frontNode.next
        return frontNode.data
    def display(self):
        curNode = self.front
        while curNode is not None:
            print(curNode.data)
            curNode = curNode.next
            print()

q = Queue()
while (True):
    print("Queue Operations")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))
    if (choice == 1):
        data = input("Enter data: ")
        print()
        q.enqueue(data)
    elif (choice == 2):
        if q.isempty():
            print("Queue is empty\n")
        else:
            print("Dequeued element: ", q.dequeue())
            print()
    elif (choice == 3):
        if q.isempty():
            print("Queue is empty\n")
        else:
            print("Front element is: ", q.peek())
            print()
    elif (choice == 4):
        if q.isempty():
            print("Queue is empty\n")
        else:
            print("\nQueue elements: ")
            q.display()
    elif (choice == 5):
        print("Thank You!")
        break
    else:
        print("Invalid Choice\n")