class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("dequeue from an empty queue")
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("peek from an empty queue")
        return self.stack2[-1]

    def is_empty(self):
        return not self.stack1 and not self.stack2

def main():
    queue = QueueUsingStacks()
    
    while True:
        print("\nOptions:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            value = input("Enter the value to enqueue: ")
            queue.enqueue(value)
            print(f"Enqueued: {value}")
        
        elif choice == '2':
            try:
                dequeued_value = queue.dequeue()
                print(f"Dequeued: {dequeued_value}")
            except IndexError as e:
                print(e)
        
        elif choice == '3':
            try:
                front_value = queue.peek()
                print(f"Front value: {front_value}")
            except IndexError as e:
                print(e)
        
        elif choice == '4':
            if queue.is_empty():
                print("The queue is empty.")
            else:
                print("The queue is not empty.")
        
        elif choice == '5':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")
            continue
