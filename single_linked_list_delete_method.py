class Node:
    def __init__(self, data):
        self.data = data # data in the node
        self.next = None # pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None # initially, the list is empty

    def append(self, data): # add a new node at the end
        new_node = Node(data)
        if not self.head: # if the list is empty
            self.head = new_node
            return
        last = self.head
        while last.next: # traverse to the last node
            last = last.next
        last.next = new_node # update next of the last node to the new node

    def delete(self, key): # delete a node by value
        if not self.head: # if the list is empty
            print("List is empty")
            return
        if self.head.data == key: #if head node itself has the key to be deleted
            self.head = self.head.next
            return
        current = self.head # search for key to be deleted
        while current.next:
            if current.next.data == key:
                current.next = current.next.next
                return
            current = current.next
            print(f"Node with the data {key} not found.")

    def print_list(self): # print the linked list
        temp = self.head
        while temp: # traverse through the list
            print(temp.data, end = " -> ")
            temp = temp.next
        print("None")

# creating a LinkedList & perform operations
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

# print the linked list before deletion
print("Original List: ")
linked_list.print_list()

# delete a node
linked_list.delete(3)