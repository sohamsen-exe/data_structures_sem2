class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def create_list(self):
        if self.head is not None:
            print("List already created!")
            return

        data = int(input("Enter data for first node: "))
        new_node = Node(data)
        self.head = new_node
        current = self.head

        while True:
            choice = input("Do you want to add another node? (yes/no): ").strip().lower()
            if choice == "yes":
                data = int(input("Enter data: "))
                new_node = Node(data)
                current.next = new_node
                current = new_node
            else:
                current.next = self.head  # Make it circular
                break

    def display_list(self):
        if self.head is None:
            print("List is empty!")
            return

        current = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")


# Example usage
cll = CircularLinkedList()
cll.create_list()
cll.display_list()
