class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        if current is None:
            print("Linked list is empty.")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
   
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    

    def delete_by_value(self, key):
        current = self.head
        if current is None:
            print("Linked list is empty.")
            return
        
        if current.data == key:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        
        if current is None:
            print(f"Node with value {key} not found.")
            return
        
        prev.next = current.next
        current = None
    
def menu():
    ll = LinkedList()
    
    while True:
        print("\nMenu:")
        print("1. Display Linked List")
        print("2. Insert Node")
        print("3. Delete Node")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            ll.display()
        
        elif choice == 2:
            data = int(input("Enter the data to insert at the end: "))
            ll.insert_end(data)
        
        elif choice == 3:
            key = int(input("Enter the value to delete: "))
            ll.delete_by_value(key)
        
        elif choice == 4:
            break
        
        else:
            print("Invalid choice, please try again.")
menu()
