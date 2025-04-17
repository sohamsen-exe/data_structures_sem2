class StackUsingList:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackUsingLinkedList:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_node = self.top
            self.top = self.top.next
            return popped_node.data
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.top.data
        return "Stack is empty"

    def is_empty(self):
        return self.top is None


if __name__ == "__main__":
    print("Choose stack implementation:")
    print("1. Stack using List")
    print("2. Stack using Linked List")
    choice = int(input("Enter choice (1/2): "))

    if choice == 1:
        stack = StackUsingList()
    elif choice == 2:
        stack = StackUsingLinkedList()
    else:
        print("Invalid choice")
        exit()

    while True:
        print("\nOperations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Exit")
        op = int(input("Enter operation (1-5): "))

        if op == 1:
            item = input("Enter item to push: ")
            stack.push(item)
        elif op == 2:
            print("Popped item:", stack.pop())
        elif op == 3:
            print("Top item:", stack.peek())
        elif op == 4:
            print("Is stack empty?:", stack.is_empty())
        elif op == 5:
            print("Thank You!")
            break
        else:
            print("Invalid operation")
