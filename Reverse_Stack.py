class Stack:
    def _init_(self):
        self.items = []

    def isempty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isempty():
            print("Stack Underflow")
            return None
        return self.items.pop()

    def peek(self):
        if self.isempty():
            print("Stack is empty")
            return None
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def display(self):
        if self.isempty():
            print("Stack is empty")
            return

        print("Stack elements (from top to bottom):")
        top = len(self.items)
        for i in range(top - 1, -1, -1):
            print(self.items[i])

    def reverse(self):
        if self.isempty():
            print("Stack is empty")
            return
        print('Reversed stack (From Bottom to Top):')
        for i in range(len(self.items)):
            print(self.items[i])

    def minimum(self):
        if self.isempty():
            print("Stack is empty")
            return
        print('Minimum Element:')
        print(min(self.items))


s = Stack()
while True:
    print("\nProgram to implement the stack using list")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Reverse")
    print("6. Minimum Element")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter the data: "))
        s.push(num)

    elif choice == 2:
        num = s.pop()
        if num is not None:
            print("Popped item =", num)

    elif choice == 3:
        num = s.peek()
        if num is not None:
            print("Item at the top of the stack:", num)

    elif choice == 4:
        s.display()

    elif choice == 7:
        print("\nQuitting .......")
        break
    elif choice == 5:
        s.reverse()
    elif choice == 6:
        s.minimum()

    else:
        print("Invalid choice! Enter a correct choice (1-5):")
        continue